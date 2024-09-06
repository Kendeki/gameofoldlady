conditions = [[" X", " X", " X"], [" O", " O", " O"]]
almost = [["  ", " X", " X"], [" X", "  ", " X"], [" X", " X", "  "]]

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

  return any(k in conditions for k in dig)
  
def empate(matriz):
  all = True

  for i in matriz:
    if "  " in i:
      all = False

  return all

def close(matriz):
  dig = diagonal(matriz)
  col = colunas(matriz)
  lin = linhas(matriz)
  
  for i in colunas(matriz):
    if i in almost:
      return (almost.index(i), col.index(i), int(0))

  for j in linhas(matriz):
    if j in almost:
      return (almost.index(j), lin.index(j), int(1))

  for k in dig:
    if k in almost:
      return (almost.index(k), dig.index(k), int(2))
      
  return None