import binary_manipulation as bm
import channel as c
import line_encoding as le
import metrics
import modulator as mod

CODIFICACAO_LINHA = "MANCHESTER" # "NRZ", "MANCHESTER", None
MODULACAO = "ASK" # "ASK", "BPSK", "16QAM"
CANAL = "AWGN" # "AWGN", "RAJADAS"

A = 1.0            # AMPLITUDE
APB = 20           # AMOSTRAS POR BIT (COM MANCHESTER DEVE SER PAR)
FP = 2.0           # FREQUENCIA DA PORTADORA
EBN0_DB = 10.0     # SNR
SEED = 42

def executar_validacao_unica():
  rmg = np.random.default_rng(SEED)
  print("======== Iniciando simulação ========\n")

  # Fonte de informação
  print("----- Fonte e Codificação ASCII -----")
  mensagem = "Inter maior do mundo"
  binario_str = bm.ascii_to_binary(mensagem)
  bits_fonte = np.array([int(b) for b in binario_str.replace(" ", "")], dtype=int)

  # Codificador de fonte
  print("----- Codificação de Canal -----")
  bits_canal_str, tam_original = bm.codificar_mensagem("".join(map(str, bits_fonte)))
  bits_tx = np.array([int(b) for b in bits_canal_str], dtype=int)
  print(f"Hamming (7,4) aplicado: {tam_original} bits -> {len(bits_tx)} bits.\n")

  # Codificação de linha
  print("----- Codificação de Linha -----")
  if CODIFICACAO_LINHA == "NRZ":
    sinal_linha = le.nrz_unipolar(bits_tx, A, APB)
  elif CODIFICACAO_LINHA == "MANCHESTER":
    sinal_linha = le.manchester(bits_tx, A, APB)
  elif CODIFICACAO_LINHA == "None"
    sinal_linha = bits_tx
    print("Codificação de linha ignorada. Passando bits para modulação...")
  print("\n")

  print("----- Modulação ----- ")

  print("----- Canal de Transmissão ----- ")

  print("----- Demodulação -----")

  print("----- Decodificação de Linha -----")

  print("----- Decodificação de Canal -----")

executar_validacao_unica()
