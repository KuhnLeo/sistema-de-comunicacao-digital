import binary_manipulation as bm
import channel as c
import line_encoding as le
import metrics
import modulator as mod

# ------------ Fonte de Informação -------------
print("Fase 1: Fonte de informação\n")
mensagem = "Inter maior do mundo"
print("Mensagem definida: ", mensagem)

# ------------ Codificador de Fonte --------------
print("Fase 2: Codificador de fonte\n")
binario = bm.ascii_to_binary(mensagem)

# ------------ Codificação de Canal --------------

# ------------ Modulação -------------

# ------------- Meio de Transmissão ------------

# ----------- Demodulação -------------

# ------------- Decodificador de Canal --------------

# ------------ Decodificador de Fonte -------------

# ------------- Receptor de Informação --------------
ascii = bm.binary_to_ascii(binario)
