conditions = [[" X", " X", " X"], [" O", " O", " O"]]

def diagonal(matriz):
  diagonalEsquerda = []
  diagonalDireita = []

  for i in range(len(matriz)):
    diagonalEsquerda.append(matriz[i][i])

  for i, j in zip(range(len(matriz)), range(len(matriz) - 1, -1,-1)):
    diagonalDireita.append(matriz[i][j])
  return (diagonalEsquerda, diagonalDireita)

def linhas(matriz):
  linhas = []

  for i in range(len(matriz)):
    temp = []
    for j in range(len(matriz)):
      temp.append(matriz[i][j])
    linhas.append(temp)

  return linhas

def colunas(matriz):
  colunas = []

  for i in range(len(matriz)):
    temp = []
    for j in range(len(matriz)):
      temp.append(matriz[j][i])
    colunas.append(temp)

  return colunas

def win(matriz):
  dig = diagonal(matriz)
  for i in colunas(matriz):
    if i in conditions:
      return True

  for j in linhas(matriz):
    if j in conditions:
      return True

  for m in dig:
    if m in conditions:
      return True

def empate(matriz):
  all = True

  for i in matriz:
    if "  " in i:
      all = False

  return all