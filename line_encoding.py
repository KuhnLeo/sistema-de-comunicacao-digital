import numpy as np

def nrz_unipolar(bits, A, apb):
  print("Codificando com NRZ Unipolar...")
  nrz_unipolar = np.repeat(bits * A, apb)
  print("NRZ Unipolar codificado com sucesso!")
  return nrz_unipolar

def manchester(bits, A, apb):
  print("Codificando com Manchester IEEE 802.3...")
  manchester_half = np.where(bits[:, None] == 1, [-A, A], [A, -A])
  manchester = np.repeat(manchester_half, apb // 2, axis=1).reshape(-1)
  print("Manchester codificado com sucesso!")
  return manchester


def decode_nrz_unipolar(sinal, A, apb):
  print("Decodificando NRZ Unipolar...")

  blocos = np.asarray(sinal).reshape(-1, apb)
  medias = np.mean(blocos, axis=1)
  bits = np.where(medias > A / 2, 1, 0)

  print("NRZ Unipolar decodificado com sucesso!")
  return bits.astype(int)


def decode_manchester(sinal, A, apb):
  print("Decodificando Manchester...")

  blocos = np.asarray(sinal).reshape(-1, apb)

  metade1 = blocos[:, :apb // 2]
  metade2 = blocos[:, apb // 2:]
  media1 = np.mean(metade1, axis=1)
  media2 = np.mean(metade2, axis=1)

  bits = np.where(media2 > media1, 1, 0)

  print("Manchester decodificado com sucesso!")
  return bits.astype(int)
