import numpy as np

def nrz_unipolar(bits, A, apb):
  print("Codificando com NRZ Unipolar...")
  nrz_unipolar = np.repeat(bits * A, apb)
  return nrz_unipolar

def manchester(bits, A, apb):
  print("Codificando com Manchester IEEE 802.3...")
  manchester_half = np.where(bits[:, None] == 1, [-A, A], [A, -A])
  manchester = np.repeat(manchester_half, apb // 2m axis=1).reshape(-1)
  return manchester
