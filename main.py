import binary_manipulation as bm
import channel as c
import line_encoding as le
import metrics
import modulator as mod

mensagem = "Inter maior do mundo"

binario = bm.ascii_to_binary(mensagem)

ascii = bm.binary_to_ascii(binario)
