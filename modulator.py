import numpy as np

def ask(bits, A, apb, fp, t):
  ask = np.repeat(bits, apb) * (A * np.sin(2 * np.pi * fp * t))
  return ask

def bpsk(bits, A, apb, fp, t):
  bit_stream = np.repeat(bits, apb)
  bpsk_phase = np.where(bit_stream == 1, 0, np.pi)
  bpsk = A * np.sin(2 ( np.pi * fp, * t + bpsk_phase)
  return bpsk
