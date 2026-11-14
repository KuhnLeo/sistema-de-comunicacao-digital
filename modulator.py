import numpy as np

def ask(bits, A, apb, fp, t):
  ask = np.repeat(bits, apb) * (A * np.sin(2 * np.pi * fp * t))
  return ask

def bpsk(bits, A, apb, fp, t):
  bit_stream = np.repeat(bits, apb)
  bpsk_phase = np.where(bit_stream == 1, 0, np.pi)
  bpsk = A * np.sin(2 * np.pi * fp, * t + bpsk_phase)
  return bpsk

def qam16(bits, A, apb, fp, t):
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

  normalizacao = A / np.sqrt(10)

  portadora_i = np.cos(2 * np.pi * fp * t)
  portadora_q = np.sin(2 * np.pi * fp * t)

  sinal = normalizacao * (i * portadora_i - q * portadora_q)
  return sinal
