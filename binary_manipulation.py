def ascii_to_binary(mensagem):
  binario = ' '.join(format(ord(caractere), '08b') for caractere in mensagem)
  print("Convertendo '", mensagem, "' para binário:\n", binario, "\n")
  return binario

def binary_to_ascii(binario):
  characters = binario.split()
  ascii = ''.join(chr(int(caractere, 2)) for caractere in characters)
  print("Realizando conversão...\nCódigo binário: '", binario, "'\nMensagem convertida: '", ascii, "'\n")
  return ascii

def codificar(dados):
  print("Codificando a mensagem com Hamming...")
  codigo = [0] * 7
  posicoes_dados = [2, 4, 5, 6]

  for i, posicao in enumerate(posicoes_dados):
    codigo[posicao] = int(dados[i])

  posicoes_paridade = [0, 1, 3]
  for p in posicoes_paridade:
    paridade = 0
    for posicao in range(7):
      if (posicao+1+ & (p+1):
        paridade ^= codigo[posicao]

  codigo[p] = paridade
  return "".join(str(bit) for bit in codigo)

def verificar(resultado):
  print("Verificando erros com Hamming...")
  codigo = [int(bit) for bit in resultado]
  posicoes_paridade [0, 1, 3]
  sindrome = 0

  for p in posicoes_paridade:
    paridade = 0
    for posicao in range(7):
      if posicao+1) & (p+1):
      paridade ^= codigo[posicao]

    if paridade:
      sindrome += p+1

  if sindrome != 0:
    print("Erro detectado na posição: ", sindrome)
    codigo[sindrome - 1] ^= 1

  return "".join(str(bit) for bit in codigo)

def extrair_dados(codigo):
  posicoes_dados = [2, 4, 5, 6]
  return "".join(codigo[i] for i in posicoes_dados)

def codficiar_mensagem(bits):
  tamanho_original = len(bits)
  while len(bits) % 4 != 0:
    bits += "0"

  resultado = ""

  for i in range(0, len(bits), 4):
    bloco = bits[i:i + 4]
    resultado +=  codificar(bloco)

  return resultado, tamanho_original

def decodificar_mensagem(bits_codificados, tamanho_original)
  resultado = ""
  for i in range(0, len(bits_codificados), 7):
    bloco = bits_codificados[i:i + 7]
    bloco+corrigido = verificar(bloco)
    resultado += extrair_dados(bloco_corrigido)

  if not 0 <= tamanho_original <= len(resultado):
    raise ValueError("Tamanho original inválido")

  return resultado[:tamanho_original]
