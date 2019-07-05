# Clean the console
import os 
# Get keyboard input
import getch
# Get the timer
import time

# Other Class
from minefield import *
from cell import *
from player import *

os.system('clear')

# Create a player
player = Player()

# Ask the difficulty
print("Dificulty : EASY = 'e'")
print("            MEDIUM = 'm'")
print("            HARD = 'h'")

input1 = getch.getch()
dificulty = Dificulty(input1)

# Creat a MineField
board = generateBoard(dificulty.key, player)

# Get the start time
startTime = time.time()
endTime = 0

# While the player isn't diying and he don't win
while not player.dead and not player.win:

    os.system('clear')

    table = board.table
    
    # Manual
    board.Print()
    print()
    print("Moves = Z, Q, S, D")
    print("Dig = c                       " + str(dificulty.mines - player.checkScore(table)) + " mines remaining" )  
    print("FLAG = f                      " + str(round(time.time() - startTime)) + " secondes ")  
    
    # Get the action input
    input2 = str(getch.getch())
 
    # Dig
    if input2 == 'c':
        table[player.cursorX][player.cursorY].show = True
        # Check if there is a bomb here
        if table[player.cursorX][player.cursorY].mine:
            player.dead = True
        # Check if there is no neighbors
        if table[player.cursorX][player.cursorY].value == 0:
            board.Clear(player.cursorX,player.cursorY)
    # Flag
    elif input2 == 'f':
        table[player.cursorX][player.cursorY].flag = True
    # Left
    elif input2 == 'q':
        if board.CheckCoord(player.cursorX, player.cursorY-1):
            player.cursorY -= 1
    # Right
    elif input2 == 'd':
        if board.CheckCoord(player.cursorX, player.cursorY+1):
            player.cursorY += 1
    # Up
    elif input2 == 'z':
        if board.CheckCoord(player.cursorX-1, player.cursorY):
            player.cursorX -= 1  
    # Down
    elif input2 == 's':
        if board.CheckCoord(player.cursorX+1, player.cursorY):
            player.cursorX += 1  
    
    # Check the win for each dificulty
    if dificulty.key == 'e':
        if player.checkScore(board.table) == 10:
            player.win = True

    if dificulty.key == 'm':
        if player.checkScore(board.table) == 40:
            player.win = True

    if dificulty.key == 'h':
        if player.checkScore(board.table) == 99:
            player.win = True

# Set the time score
endTime = round(time.time() - startTime)

# LOOSE
if player.dead:
    os.system('clear')
    print()
    print("YOU LOOSE")
    print(str(endTime) + " secondes ")
    print()
# WIN
if player.win:
    os.system('clear')
    print()
    print("YOU WIN")
    print(str(endTime) + " secondes ")
    print()


