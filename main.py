import binary_manipulation as bm
import channel as c
import line_encoding as le
import metrics
import modulator as mod

# ------------ Fonte de Informação -------------
mensagem = "Inter maior do mundo"

# ------------ Codificador de Fonte --------------
binario = bm.ascii_to_binary(mensagem)

# ------------ Codificação de Canal --------------

# ------------ Modulação -------------

# ------------- Meio de Transmissão ------------

# ----------- Demodulação -------------

# ------------- Decodificador de Canal --------------

# ------------ Decodificador de Fonte -------------

# ------------- Receptor de Informação --------------
ascii = bm.binary_to_ascii(binario)
