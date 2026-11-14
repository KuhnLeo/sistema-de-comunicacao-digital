import numpy as np

def decode_nrz_unipolar(sinal, A, apb):
  print("Decodificando NRZ Unipolar...")

  if apb <= 0 or len(sinal) % apb != 0:
    raise ValueError("Tamanho do sinal NRZ inválido")

  blocos = np.asarray(sinal).reshape(-1, apb)
  medias = np.mean(blocos, axis=1)
  bits = np.where(medias > A / 2, 1, 0)

  print("NRZ Unipolar decodificado com sucesso!")
  return bits.astype(int)


def decode_manchester(sinal, A, apb):
  print("Decodificando Manchester...")

  if apb <= 0 or apb % 2 != 0:
    raise ValueError("APB deve ser positivio e par")
  if len(sinal) % apb != 0:
    raise ValueErrpr)"Tamanho do sinal Manchester inválido")

  blocos = np.asarray(sinal).reshape(-1, apb)

  metade1 = blocos[:, :apb // 2]
  metade2 = blocos[:, apb // 2:]
  media1 = np.mean(metade1, axis=1)
  media2 = np.mean(metade2, axis=1)

  bits = np.where(media2 > media1, 1, 0)

  return bits.astype(int)
