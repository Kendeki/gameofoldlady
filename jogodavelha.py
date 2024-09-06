import random as rd

import funcoesjogo as fj

jogo = [['  '] * 3 for _ in range(3)] # Cria uma lista repleta de "  " para servir de tabuleiro
game_on = True # Status do jogo
bot = False # Define se será contra bot ou não
turn = True # True = X, False = O

question = int(input("1 - Modo de 2 jogadores\n2 - Modo contra bot\nR: "))
if question == 2:
  bot = True

while game_on: # Executa o jogo enquanto não houver um vencedor ou empatar 
  
  # vvv Imprime o tabuleiro na tela
  tabuleiro = f"""{jogo[0][0]} | {jogo[0][1]} | {jogo[0][2]}
------------
{jogo[1][0]} | {jogo[1][1]} | {jogo[1][2]}
------------
{jogo[2][0]} | {jogo[2][1]} | {jogo[2][2]}
"""
  
  print(f"\n{tabuleiro}\n")
  conditions = [[" X", " X", " X"], [" O", " O", " O"]] # Condições de vitória

  if not bot: # Loop para o modo de 2 jogadores
  
    if fj.win(jogo):
      if not turn:
        print("X Ganhou!")
        game_on = False
        break
        
      else:
        print("O Ganhou!")
        game_on = False
        break
        
    else:
      if fj.empate(jogo):
        print("Empate.")
        game_on = False
        break
        
    while True:
      x, y = int(input("Insira a linha: ")), int(input("Insira a coluna: "))
  
      if turn:
        if jogo[x - 1][y - 1] == "  ":
          jogo[x - 1][y - 1] = ' X'
          break
          
        else:
          print("Posição inválida, tente novamente.")
  
      else:
        if jogo[x - 1][y - 1] == "  ":
          jogo[x - 1][y - 1] = ' O'
          break
          
        else:
          print("Posição inválida, tente novamente.")
      
    turn = not(turn)
    
  else: # Loop para o modo contra bot
    
    if fj.win(jogo):
      if not turn:
        print("X Ganhou!")
        game_on = False
        break
      else:
        print("O Ganhou!")
        game_on = False
        break
    else:
      if fj.empate(jogo):
        print("Empate.")
        game_on = False
        break

    while True:

      if turn:
        x, y = int(input("Insira a linha: ")), int(input("Insira a coluna:"))
        
        if jogo[x - 1][y - 1] == "  ":
          jogo[x - 1][y - 1] = ' X'
          break
          
        else:
          print("Posição inválida, tente novamente.")
          
      else:
        x, y = rd.randint(0, 2), rd.randint(0, 2)
        
        if jogo[x][y] == "  ":
          jogo[x][y] = ' O'
          break
          
    turn = not(turn)