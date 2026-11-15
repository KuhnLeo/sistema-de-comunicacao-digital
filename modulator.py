import numpy as np

def ask(bits, A, apb, fp, t):
  print("Efetuando modulação ASK...")
  ask = np.repeat(bits, apb) * (A * np.sin(2 * np.pi * fp * t))
  print("Modulação ASK feita com sucesso!")
  return ask

def bpsk(bits, A, apb, fp, t):
  print("Efetuando modulação BPSK...")
  bit_stream = np.repeat(bits, apb)
  bpsk_phase = np.where(bit_stream == 1, 0, np.pi)
  bpsk = A * np.sin(2 * np.pi * fp * t + bpsk_phase)
  print("Modulação BPSK feita com sucesso!")
  return bpsk

def qam16(bits, A, apb, fp, t):
  print("Efetuando modulação 16-QAM...")
  if len(bits) % 4 != 0:
    raise ValueError("A quantidade de bits deve ser múltipla de 4")

  grupos = bits.reshape(-1, 4)

  niveis = np.array([-3, -1, 3, 1])
  ind_i = grupos[:, 0] * 2 + grupos[:, 1]
  ind_q = grupos[:, 2] * 2 + grupos[:, 3]
  i = niveis[ind_i]
  q = niveis[ind_q]

  amostras_simbolo = apb * 4
  i = np.repeat(i, amostras_simbolo)
  q = np.repeat(q, amostras_simbolo)


  portadora_i = np.cos(2 * np.pi * fp * t)
  portadora_q = np.sin(2 * np.pi * fp * t)

  sinal = A * (i * portadora_i - q * portadora_q)
  print("Modulação 16-QAM feita com sucesso!")
  return sinal



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
    referencia = portadora[inicio:fim]
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

  portadora_i = np.cos(2 * np.pi * fp * t)
  portadora_q = np.sin(2 * np.pi * fp * t)

  bits_rx = []

  for i in range(0, len(sinal_rx), amostras_simbolo):
    fim = i + amostras_simbolo
    trecho = sinal_rx[i:fim]

    ref_i = portadora_i[i:fim]
    ref_q = portadora_q[i:fim]

    i = np.mean(trecho * ref_i) * 2 / A
    q = -np.mean(trecho * ref_q) * 2 / A

    ind_i = np.argmin(np.abs(niveis - i))
    ind_q = np.argmin(np.abs(niveis - q))

    bits_i = format(ind_i, '02b')
    bits_q = format(ind_q, '02b')

    bits_rx.extend(int(bit) for bit in bits_i + bits_q)
    
  print("16-QAM demodulado com sucesso!")
  return np.array(bits_rx, dtype=int)
