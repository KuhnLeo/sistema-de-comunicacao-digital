def ascii_to_binary(mensagem):
  binario = ' '.join(format(ord(caractere), '08b') for caractere in mensagem)
  return binario
