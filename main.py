import binary_manipulation as bm
import channel as c
import line_encoding as le
import modulator as mod
import numpy as np

MODO_TRANSMISSAO = "MODULACAO" # "LINHA", "MODULACAO"
CODIFICACAO_LINHA = "MANCHESTER" # "NRZ", "MANCHESTER"
MODULACAO = "ASK" # "ASK", "BPSK", "16QAM"
CANAL = "RAJADAS" # "AWGN", "RAJADAS"

A = 1.0            # AMPLITUDE
APB = 20           # AMOSTRAS POR BIT (COM MANCHESTER DEVE SER PAR)
FP = 2.0           # FREQUENCIA DA PORTADORA
SNR = 10.0         # SNR
SEED = 42


def executar_validacao_unica():
  rng = np.random.default_rng(SEED)
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

  pad_16qam = 0
  if MODO_TRANSMISSAO == "MODULACAO" and MODULACAO == "16QAM":
    resto = len(bits_tx) % 4
    if resto != 0:
      pad_16qam = 4 - resto
      bits_tx = np.append(bits_tx, np.zeros(pad_16qam, dtype=int))

  n_bits_transmissao = len(bits_tx)

  
  # Codificação de linha ou Modulação
  t = np.arange(len(bits_tx) * APB) / APB

  if MODO_TRANSMISSAO == "LINHA":
    print("----- Codificação de Linha -----")
    if CODIFICACAO_LINHA == "NRZ":
      sinal_tx = le.nrz_unipolar(bits_tx, A, APB)
    elif CODIFICACAO_LINHA == "MANCHESTER":
      sinal_tx = le.manchester(bits_tx, A, APB)
    else:
      raise ValueError("Codificação inválida!")
  elif MODO_TRANSMISSAO == "MODULACAO":
    print("----- Modulação -----")
    if MODULACAO == "ASK":
      sinal_tx = mod.ask(bits_tx, A, APB, FP, t)
    elif MODULACAO == "BPSK":
      sinal_tx = mod.bpsk(bits_tx, A, APB, FP, t)
    elif MODULACAO == "16QAM":
      sinal_tx = mod.qam16(bits_tx, A, APB, FP, t)
    else:
      raise ValueError("Modulação inválida!")
      
  print("\n")

  
  # Canal de transmissão
  print("----- Canal de Transmissão ----- ")
  if CANAL == "AWGN":
    print(f"Transmitindo por canal AWGN ({SNR} dB)...")
    sinal_rx = c.awgn(sinal_tx, SNR, n_bits_transmissao, rng)
  elif CANAL == "RAJADAS":
    print(f"Transmitindo por canal AWGN com rajadas ({SNR} dB)...")
    sinal_rx = c.awgn_rajadas(sinal_tx, SNR, n_bits_transmissao, rng, bloco = APB * 10)
  else:
    raise ValueError("Canal inválido!")
    
  print("Sinal recebido do receptor\n")

  
  # Decodificação de linha ou Demodulação
  if MODO_TRANSMISSAO == "LINHA":
    print("----- Decodificação de Linha -----")
    if CODIFICACAO_LINHA == "NRZ":
      bits_rx = le.decode_nrz_unipolar(sinal_rx, A, APB)
    elif CODIFICACAO_LINHA == "MANCHESTER":
      bits_rx = le.decode_manchester(sinal_rx, A, APB)

  elif MODO_TRANSMISSAO == "MODULACAO":
    t = np.arange(n_bits_transmissao * APB) / APB
    print("----- Demodulação -----")
    if MODULACAO == "ASK":
      bits_rx = mod.demo_ask(sinal_rx, A, APB, FP, t)
    elif MODULACAO == "BPSK":
      bits_rx = mod.demo_bpsk(sinal_rx, A, APB, FP, t)
    elif MODULACAO == "16QAM":
      bits_rx = mod.demo_16qam(sinal_rx, A, APB, FP, t)

  if pad_16qam > 0:
    bits_rx = bits_rx[:-pad_16qam]
  print("\n")
  

  print("----- Decodificação de Canal -----")
  bits_rx_str = "".join(str(b) for b in bits_rx)
  bits_recuperados_str = bm.decodificar_mensagem(bits_rx_str, tam_original)
  bits_recuperados = np.array([int(b) for b in bits_recuperados_str], dtype=int)
  print(f"Decodificação com Hamming concluída: {len(bits_recuperados)} bits recuperados")

  binario_rx_formatado = " ".join(bits_recuperados_str[i:i + 8] for i in range(0, len(bits_recuperados_str), 8))
  mensagem_final = bm.binary_to_ascii(binario_rx_formatado)
  print("Mensagem final: ", mensagem_final)

executar_validacao_unica()
