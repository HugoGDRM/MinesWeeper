# Clean the console
import os 
# Get keyboard input
import getch
# Get the timer
import time
# Get randoms
import random as rnd

"""
Class how represent a cell of the minefield.

"""
class Cell(object):

    def __init__(self):
        self.mine = False  # There is a mine here ?
        self.flag = False  # There is a flag here ?
        self.show = False  # This cell is visible ?
        self.value = 0     # The number of neighbor(s) around it 


    """
    Return a symbol that represent the state of this cell.

    """
    def __str__(self):
        
        # Is she show
        if self.show:
            # An empty cell with no neighbors is a 'space'
            if self.value == 0:
                return " "
            # Else if the cell has cell around it, this is the number of neighbors : (1 <= 'int' <= 8)
            else:
                return str(self.value)
        # She is hide
        elif self.flag:
            return '!'
        else:
            # A simple hide cell
            return '.'

"""
Class how represent the player.

"""
class Player(object):

    def __init__(self):

        self.win = False  # The player win the game ?
        self.dead = False  # Is he dead ?
        self.cursorX = 0  # Vertical Cursor Coord
        self.cursorY = 0  # Horizontal Cursor Coord
        
    """
    Check the number of flagged mines.

    """
    def checkScore(self, table):
        c = 0
        for i in range(len(table)):
            for y in range(len(table[0])):
                if table[i][y].mine and table[i][y].flag:
                    c += 1
        return c

"""
Class how represent the dificulty of the board.

"""
class Dificulty(object):

    def __init__(self, input_key):

        if input_key == 'e':
            self.mines = 10
        if input_key == 'm':
            self.mines = 30
        if input_key == 'h':
            self.mines = 70

        self.key = input_key

"""
Class how represent the minefield.

"""
class MineField(object):

    def __init__(self, width, height, player):

        table = []
        
        # HEIGHT
        for i in range(height): 
            table.append([])

        # WIDTH
        for line in table: 
            for y in range(width):
                line.append(Cell())
        
        self.table = table
        self.player = player

    """
    Check if X and Y coordinates are inside the table.

    """
    def CheckCoord(self, x, y):
        return x >= 0 and x < len(self.table) and y >= 0 and y < len(self.table[0])


    """
    Fill the board with n bombs.

    """
    def Fill(self, n):

        while n > 0:

            # Create 2 random numbers
            rndHeight = rnd.randint(0, len(self.table) - 1)
            rndWidth = rnd.randint(0, len(self.table[0]) - 1)

            cell = self.table[rndHeight][rndWidth]

            # Check if this cell is not trap, if it is, do anything
            if not cell.mine:

                cell.mine = True
                n -= 1
   
    """
    Count all the neighbors of this cell.
 
    """     
    def CountNeighbor(self):

        for i in range(len(self.table)):

            for y in range(len(self.table[0])):

                n = 0
                
                # Check the 8 cells around it, but before each Check, look if coordinates are inside the table

                # North West
                if self.CheckCoord(i-1, y-1):
                    if self.table[i-1][y-1].mine:
                         n += 1

                # North 
                if self.CheckCoord(i-1, y):
                    if self.table[i-1][y].mine:
                         n += 1

                # North Est
                if self.CheckCoord(i-1, y+1):
                    if self.table[i-1][y+1].mine:
                         n += 1

                # Est
                if self.CheckCoord(i, y+1):
                    if self.table[i][y+1].mine:
                         n += 1

                # South Est
                if self.CheckCoord(i+1, y+1):
                    if self.table[i+1][y+1].mine:
                         n += 1
                 
                # South
                if self.CheckCoord(i+1, y):
                    if self.table[i+1][y].mine:
                         n += 1

                # South West
                if self.CheckCoord(i+1, y-1):
                    if self.table[i+1][y-1].mine:
                         n += 1
                
                # West
                if self.CheckCoord(i, y-1):
                    if self.table[i][y-1].mine:
                         n += 1

                self.table[i][y].value = n

    """
    Print the board with arg for dev.
 
    """ 
    def PrintDev(self):

        for i in range(self.height):

            for y in range(self.width):

                print("(" + str(self.table[i][y].mine) + "," + str(self.table[i][y].value) + "," + str(self.table[i][y].flag) + ")" , end = " ")
            
            print()

    """
    Print the minefield.
 
    """ 
    def Print(self):

        for i in range(len(self.table)):

            for y in range(len(self.table[0])):

                print(self.table[i][y].__str__() , end = "")

                if i == self.player.cursorX and y == self.player.cursorY:
                    print("* ", end = "")
                else:
                    print("  ", end = "")
            
            print()

    """
    Dig all the empty cell around and cell.
    i = Vertical Coord
    y = Horizontal Coord
    meet = Boolean on True if we meet a cell with a value != than zero (ending condition) (on false at the begining)

    """ 
    def Clear(self, i, y, meet):

        # Check the 4 cells around it, if the cell is empty, make it visible and make a recursive call on it.
        
        if not meet and not self.table[i][y].show:

            # If the cell is empty and has no neighbors, call the function on cells around it and show it
            if self.table[i][y].value == 0:

                # Show it
                self.table[i][y].show = True

                # North 
                if self.CheckCoord(i-1, y):
                        self.Clear(i-1,y, False)

                # Est 
                if self.CheckCoord(i, y+1):
                        self.Clear(i,y+1, False)

                # South 
                if self.CheckCoord(i+1, y):
                        self.Clear(i+1,y, False)

                # West 
                if self.CheckCoord(i, y-1):
                        self.Clear(i,y-1, False)

            # Else if this cell has neighbors, stop the recursion
            else:

                # Show it
                self.table[i][y].show = True       


"""
Generate a board
 
""" 
def generateBoard(dificulty, player):
    
    if dificulty == 'e':
        # Create an EASY board 
        board = MineField(9,9, player)
        board.Fill(10)
        board.CountNeighbor()
        return board
    elif dificulty == 'm':
        # Create a MEDIUM board 
        board = MineField(16,16, player)
        board.Fill(40)
        board.CountNeighbor()
        return board
    elif dificulty == 'h':
        # Create an HARD board 
        board = MineField(30,16, player)
        board.Fill(99)
        board.CountNeighbor()
        return board
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
        # Check if there is no neighbors
        if table[player.cursorX][player.cursorY].value == 0:
            # Clear
            board.Clear(player.cursorX,player.cursorY, False)
        else:
            # Show it normally
            table[player.cursorX][player.cursorY].show = True

        # Check if there is a bomb here
        if table[player.cursorX][player.cursorY].mine:
            player.dead = True
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


