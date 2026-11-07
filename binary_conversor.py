def ascii_to_binary(mensagem):
  binario = ' '.join(format(ord(caractere), '08b') for caractere in mensagem)
  print("Convertendo ", mensagem, " para binário: ", binario)
  return binario

def binary_to_ascii(binario):
  characters = binario.split()
  ascii = ''.join(chr(int(caractere, 2)) for caractere in characters)
  print("Realizando conversão...\nCódigo binário: ", binario, "\nMensagem convertida: ", ascii)
  return ascii
