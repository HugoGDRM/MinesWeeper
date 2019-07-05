import os 
import getch
from minefield import *
from cell import *
from player import *

"""
    Get an input from the player.
 
""" 
def getInput(msg):
    try:
        return getch.getch()

    except SyntaxError:
    	pass

"""
    Check if the player win. 
    If the n mines are flagged.
 
""" 
def checkWin(table, n):
    c = 0
    for i in range(len(table)):
        for y in range(len(table[0])):
            if table[i][y].mine and table[i][y].flag:
                c += 1
    return c == n




player = Player()
board = MineField(9,9,player)
board.Fill(10)
board.CountNeighbor()

while(not player.dead and not player.win):

    os.system('clear')

    board.Print()

    i = str(getch.getch())

    # Dig
    if(i == "c"):
        board.table[player.cursorX][player.cursorY].show = True
        # Check if there is a bomb here
        if(board.table[player.cursorX][player.cursorY].mine):
            player.dead = True
    # Flaf
    elif(i == "f"):
        board.table[player.cursorX][player.cursorY].flag = True
    # Left
    elif(i == "q"):
        if(board.CheckCoord(player.cursorX, player.cursorY-1)):
            player.cursorY -= 1
    # Right
    elif(i == "d"):
        if(board.CheckCoord(player.cursorX, player.cursorY+1)):
            player.cursorY += 1
    # Up
    elif(i == "z"):
        if(board.CheckCoord(player.cursorX-1, player.cursorY)):
            player.cursorX -= 1  
    # Down
    elif(i == "s"):
        if(board.CheckCoord(player.cursorX+1, player.cursorY)):
            player.cursorX += 1  
    
    # Check the win
    if checkWin(board.table,10):
        player.win = True

if(player.dead):
    os.system('clear')
    print("YOU LOOSE")
if(player.win):
    os.system('clear')
    print("YOU WIN")


