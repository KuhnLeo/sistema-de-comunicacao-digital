import contextlib
import csv
import io

import numpy as np

import modulator as mod
from channel import awgn, awgn_rajadas

#Configuração do experimento
N_BITS = 100_000                        
EBN0_DB = [0, 2, 4, 6, 8, 10, 12, 14]   
SEMENTES = [0, 1, 2, 3, 4]              
A, APB, FP = 1.0, 16, 2                

MODULACOES = {
    "ASK": (mod.ask, mod.demo_ask),
    "BPSK": (mod.bpsk, mod.demo_bpsk),
    "16-QAM": (mod.qam16, mod.demo_16qam),
}

CANAIS = ["AWGN", "Rajadas"]
BLOCO = APB * 10                       

t = np.arange(N_BITS * APB) / APB      


def passar_pelo_canal(tx, canal, ebn0, rng):
    if canal == "AWGN":
        return awgn(tx, ebn0, N_BITS, rng)
    return awgn_rajadas(tx, ebn0, N_BITS, rng, BLOCO)


def silencioso(funcao, *args):
    """Roda a função escondendo os prints dela (senão saem centenas de linhas)."""
    with contextlib.redirect_stdout(io.StringIO()):
        return funcao(*args)


with open("resultados.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["canal", "tecnica", "ebn0_db", "semente", "n_bits", "erros", "ber"])

    for canal in CANAIS:
        for nome, (modular, demodular) in MODULACOES.items():
            for ebn0 in EBN0_DB:
                bers = []
                for semente in SEMENTES:
                    rng = np.random.default_rng(semente)

                    bits = rng.integers(0, 2, N_BITS)
                    tx = silencioso(modular, bits, A, APB, FP, t)
                    rx = passar_pelo_canal(tx, canal, ebn0, rng)
                    bits_rx = silencioso(demodular, rx, A, APB, FP, t)

                    erros = int(np.sum(bits != bits_rx))
                    w.writerow([canal, nome, ebn0, semente, N_BITS, erros, erros / N_BITS])
                    bers.append(erros / N_BITS)
                print(f"{canal:7s} {nome:7s} Eb/N0={ebn0:2d} dB  BER média = {np.mean(bers):.5f}")