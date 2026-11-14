import numpy as np


def demo_ask(sinal_rx, A, apb, fp, t):
  print("Demodulando ASK...")

  portadora = np.sin(2 * np.pi * fp * t)
  n_bits = len(sinal_rx) // apb
  bits_rx = []

  for i in range(n_bits):
    inicio = i * apb
    fim = inicio + apb

    trecho = sinal_rx[inicio:fim]
    referencia = portadora[inicio:fim]
    correlacao = np.mean(trecho * referencia)

    if correlacao > A / 4:
      bits_rx.append(1)
    else:
      bits_rx.append(0)
      
  print("ASK demodulado com sucesso!")
  return np.array(bits_rx, dtype=int)


def demo_bpsk(sinal_rx, A, apb, fp, t):
  print("Demodulando BPSK...")
  
  portadora = np.sin(2 * np.pi * fp * t)
  n_bits = len(sinal_rx) // apb
  bits_rx = []

  for i in range(n_bits):
    inicio = i * apb
    fim = inicio + apb

    trecho = sinal_rx[inicio:fim]
    rerferencia = portadora[inicio:fim]
    correlacao = np.mean(trecho * referencia)

    if correlacao >= 0:
      bits_rx.append(1)
    else:
      bits_rx.append(0)

  print("BPSK demodulado com sucesso!")
  return np.array(bits_rx, dtype=int)


def demo_16qam(sinal_rx, A, apb, fp, t):
  print("Demodulando 16-QAM...")

  amostras_simbolo = apb * 4
  if len(sinal_rx) % amostras_simbolo != 0:
    raise ValueError("Tamanho do sinal inválido")

  niveis = np.array([-3, -1, 3, 1])
  normalizacao = A / np.sqrt(10)

  portadora_i = np.cos(2 * np.pi * fp * t)
  portadora_q = np.sin(2 * np.pi * fp * t)

  bits_rx = []

  for i in range(0, len(sina_rx), amostras_simbolo):
    fim = i + amostras_simbolo
    trecho = sinal_rx[i:fim]

    ref_i = portadora_i[i:fim]
    ref_Q = portadora_Q[i:fim]

    i = np.mean(trecho * ref_i) * 2 / normalizacao
    q = -np.mean(trecho * ref_q) * 2 / normalizacao

    ind_i = np.argmin(np.abs(niveis - i))
    ind_q = np.argmin(np.abs(niveis - q))

    bits_i = format(ind_i, '02b')
    bits_q = format(ind_q, '02b')

    bits_rx.extend(int(bit) for bit in bits_i + bits_q)
    
  print("16-QAM demodulado com sucesso!")
  return np.array(bits_rx, dtype=int)
