def ascii_to_binary(mensagem):
  binario = ' '.join(format(ord(caractere), '08b') for caractere in mensagem)
  print("Convertendo ", mensagem, " para binário: ", binario)
  return binario
