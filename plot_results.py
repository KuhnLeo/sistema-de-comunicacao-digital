import csv
from collections import defaultdict
from math import log10

import matplotlib.pyplot as plt
import numpy as np

TECNICAS = ["ASK", "BPSK", "16-QAM"]
EFICIENCIA = {"ASK": 1, "BPSK": 1, "16-QAM": 4}   # bits/s/Hz nominal (bits por símbolo)

# 1) Ler o CSV e agrupar as BER de cada (canal, técnica, Eb/N0)
dados = defaultdict(list)
with open("resultados.csv", encoding="utf-8") as f:
    for linha in csv.DictReader(f):
        chave = (linha["canal"], linha["tecnica"], float(linha["ebn0_db"]))
        dados[chave].append(float(linha["ber"]))


# 2) Para um canal e uma técnica, calcular média e desvio-padrão entre as sementes
def curva(canal, tecnica):
    ebn0s = sorted({k[2] for k in dados if k[0] == canal and k[1] == tecnica})
    medias = np.array([np.mean(dados[(canal, tecnica, e)]) for e in ebn0s])
    desvios = np.array([np.std(dados[(canal, tecnica, e)]) for e in ebn0s])
    return np.array(ebn0s), medias, desvios


def desenhar(ax, canal, tecnica, rotulo=None):
    """Desenha a curva (com barras de erro) de uma técnica num canal."""
    x, media, desvio = curva(canal, tecnica)
    ok = media > 0                                   # BER = 0 não aparece em escala log
    erro_baixo = np.minimum(desvio, media * 0.99)    # evita barra que passa de zero
    ax.errorbar(x[ok], media[ok], yerr=[erro_baixo[ok], desvio[ok]],
                marker="o", capsize=3, label=rotulo or tecnica)


def formatar(ax, titulo):
    ax.set_yscale("log")
    ax.set_ylim(1e-5, 1)
    ax.set_xlabel("Eb/N0 (dB)")
    ax.set_ylabel("BER")
    ax.set_title(titulo)
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()


# 3) Gráficos 1 e 2: BER x Eb/N0, um arquivo por canal
for canal, arquivo, titulo in [
    ("AWGN", "ber_awgn.png", "BER x Eb/N0 - canal AWGN (média e desvio de 5 sementes)"),
    ("Rajadas", "ber_rajadas.png", "BER x Eb/N0 - canal com rajadas (média e desvio de 5 sementes)"),
]:
    fig, ax = plt.subplots(figsize=(7, 5))
    for tecnica in TECNICAS:
        desenhar(ax, canal, tecnica)
    formatar(ax, titulo)
    fig.tight_layout()
    fig.savefig(arquivo, dpi=150)

# 4) Gráfico 3: AWGN x rajadas, um painel por modulação
fig, axs = plt.subplots(1, 3, figsize=(15, 4.5), sharey=True)
for ax, tecnica in zip(axs, TECNICAS):
    desenhar(ax, "AWGN", tecnica, "AWGN")
    desenhar(ax, "Rajadas", tecnica, "Rajadas")
    formatar(ax, tecnica)
fig.suptitle("Efeito das rajadas na BER")
fig.tight_layout()
fig.savefig("ber_awgn_vs_rajadas.png", dpi=150)

# 5) Tabela de compromisso BER x eficiência espectral
def eb_n0_para_ber(canal, tecnica, alvo=1e-3):
    """Eb/N0 (dB) em que a BER média cruza o alvo (interpolação em log10(BER))."""
    x, media, _ = curva(canal, tecnica)
    for i in range(len(x) - 1):
        if media[i] > alvo >= media[i + 1]:
            if media[i + 1] == 0:
                return f"≤ {x[i + 1]:.0f}"
            frac = (log10(media[i]) - log10(alvo)) / (log10(media[i]) - log10(media[i + 1]))
            return f"{x[i] + frac * (x[i + 1] - x[i]):.1f}"
    return f"> {x[-1]:.0f}"          # nunca chega ao alvo no intervalo testado


def ber_em(canal, tecnica, ebn0):
    x, media, _ = curva(canal, tecnica)
    return f"{media[list(x).index(ebn0)]:.2e}"


linhas = [
    "| Modulação | Eficiência espectral (bits/s/Hz) | Eb/N0 p/ BER=1e-3, AWGN (dB) | BER em 6 dB, AWGN "
    "| Eb/N0 p/ BER=1e-3, rajadas (dB) | BER em 6 dB, rajadas |",
    "|---|---|---|---|---|---|",
]
for tecnica in TECNICAS:
    linhas.append(f"| {tecnica} | {EFICIENCIA[tecnica]} | {eb_n0_para_ber('AWGN', tecnica)} "
                  f"| {ber_em('AWGN', tecnica, 6)} | {eb_n0_para_ber('Rajadas', tecnica)} "
                  f"| {ber_em('Rajadas', tecnica, 6)} |")

with open("tabela_compromisso.md", "w", encoding="utf-8") as f:
    f.write("\n".join(linhas) + "\n")
print("\n".join(linhas))

plt.show()