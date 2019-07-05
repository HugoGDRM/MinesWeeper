import random as rnd
from cell import *
from player import *

class Dificulty:
    """
    Class how represent the dificulty of the board.
 
    """
    def __init__(self, input_key):

        if input_key == 'e':
            self.mines = 10
        if input_key == 'm':
            self.mines = 40
        if input_key == 'h':
            self.mines = 99

        self.key = input_key

class MineField(object):
    """
    Class how represent the minefield.
 
    """
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
        self.width = width
        self.height = height
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

            rndHeight = rnd.randint(0, self.height - 1)
            rndWidth = rnd.randint(0, self.width - 1)

            cell = self.table[rndHeight][rndWidth]

            # Check if this cell is not trap, if it is, do anything
            if not cell.mine:

                cell.mine = True
                n -= 1
   
    """
    Count all the neighbors of this cell.
 
    """     
    def CountNeighbor(self):

        for i in range(self.height):

            for y in range(self.width):

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

        for i in range(self.height):

            for y in range(self.width):

                print(self.table[i][y].__str__() , end = "")

                if i == self.player.cursorX and y == self.player.cursorY:
                    print("* ", end = "")
                else:
                    print("  ", end = "")
            
            print()

    """
    Dig all the empty cell around and cell.
 
    """ 
    def Clear(self, i, y):

        # Check the 8 cells around it, if the cell is empty, make it visible and make a recursive call on it.
        
        # North West
        if self.CheckCoord(i-1, y-1):
            if self.table[i-1][y-1].value == 0:
                self.table[i-1][y-1].show = True
                #self.Clear(i-1,y-1)

        # North 
        if self.CheckCoord(i-1, y):
            if self.table[i-1][y].value == 0:
                self.table[i-1][y].show = True
                #self.Clear(i-1,y)

        # North Est
        if self.CheckCoord(i-1, y+1):
            if self.table[i-1][y+1].value == 0:
                self.table[i-1][y+1].show = True
                #self.Clear(i-1,y+1)

        # Est 
        if self.CheckCoord(i, y+1):
            if self.table[i][y+1].value == 0:
                self.table[i][y+1].show = True
                #self.Clear(i,y+1)

        # South Est 
        if self.CheckCoord(i+1, y+1):
            if self.table[i+1][y+1].value == 0:
                self.table[i+1][y+1].show = True
                #self.Clear(i+1,y+1)

        # South 
        if self.CheckCoord(i+1, y):
            if self.table[i+1][y].value == 0:
                self.table[i+1][y].show = True
                #self.Clear(i+1,y)

        # South West 
        if self.CheckCoord(i+1, y-1):
            if self.table[i+1][y-1].value == 0:
                self.table[i+1][y-1].show = True
                #self.Clear(i+1,y-1)

        # West 
        if self.CheckCoord(i, y-1):
            if self.table[i][y-1].value == 0:
                self.table[i][y-1].show = True
                #self.Clear(i,y-1)

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

