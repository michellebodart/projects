import random
import re

def printboard(list):
  print()
  print("  1 2 3")
  print("1 "+list[0][0]+"|"+list[0][1]+"|"+list[0][2])
  print("  -----")
  print("2 "+list[1][0]+"|"+list[1][1]+"|"+list[1][2])
  print("  -----")
  print("3 "+list[2][0]+"|"+list[2][1]+"|"+list[2][2])
  print()

def rowlinediag(list):
  return [list[0],list[1],list[2],[list[0][0],list[1][0],list[2][0]],[list[0][1],list[1][1],list[2][1]],[list[0][2],list[1][2],list[2][2]],[list[0][0],list[1][1],list[2][2]],[list[2][0],list[1][1],list[0][2]]]

def tictacto():
  print("Welcome to Tic Tac To\nPlease enter your names")
  player1name = input("Player 1: ")
  player2name = input("Player 2: ")
  
  gameboard = [[" "," "," "],[" "," "," "],[" "," "," "]]

  printboard(gameboard)

  if random.randint(0,1) == 0:
    firstplayer = player1name
    secondplayer = player2name
  else:
    firstplayer = player2name
    secondplayer = player1name
  
  playerlist = [[firstplayer,"X"], [secondplayer,"O"]]

  print(firstplayer+" goes first!")

  winner = ""
  i = 0

  while winner == "" and i<9:

    playerinput = input(playerlist[i%2][0]+", choose an open position (x,y): ")
    correct_syntax = '^ *[123] *, *[123] *$'
    is_correct_syntax = re.match(correct_syntax,playerinput)
    while is_correct_syntax == None:
      playerinput = input(playerlist[i%2][0]+", please use proper syntax and choose a position within the range (x,y): ")
      is_correct_syntax = re.match(correct_syntax,playerinput)
    
    x, y = playerinput.split(",")
    if gameboard[int(y)-1][int(x)-1] == " ":
      gameboard[int(y)-1][int(x)-1] = playerlist[i%2][1]
      printboard(gameboard)
      i+=1
    else:
      emptyspot = False
      while emptyspot == False:
        playerinput = input(playerlist[i%2][0]+", that spot is taken, please choose another: ")
        is_correct_syntax = re.match(correct_syntax,playerinput)
        while is_correct_syntax == None:
          playerinput = input(playerlist[i%2][0]+", please use proper syntax and choose an open position within the range (x,y): ")
          is_correct_syntax = re.match(correct_syntax,playerinput)

        x, y = playerinput.split(",")
        if gameboard[int(y)-1][int(x)-1] == " ":
          emptyspot = True
          gameboard[int(y)-1][int(x)-1] = playerlist[i%2][1]
          printboard(gameboard)
      i+=1
    
    optionslist = rowlinediag(gameboard)
    for n in range(len(optionslist)):
      if optionslist[n] == ["X","X","X"]:
        winner = firstplayer
      elif optionslist[n] == ["O","O","O"]:
        winner = secondplayer

  if winner =="":
    print("Tie game, no one wins :/")
  else:
    print(winner+" wins!!!")
