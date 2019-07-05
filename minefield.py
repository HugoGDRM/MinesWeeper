import random as rnd
from cell import *
from player import *

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
    Check if X and Y coordinates are inside the table
    """
    def CheckCoord(self, x, y):
        return (x >= 0 and x < len(self.table) and y >= 0 and y < len(self.table[0]))


    """
    Fill the board with n bombs.
 
    """
    def Fill(self, n):

        while(n > 0):

            rndHeight = rnd.randint(0, self.height - 1)
            rndWidth = rnd.randint(0, self.width - 1)

            cell = self.table[rndHeight][rndWidth]

            # Check if this cell is not trap, if it is, do anything
            if(not cell.mine):

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
                if(self.CheckCoord(i-1, y-1)):
                    if(self.table[i-1][y-1].mine):
                         n += 1

                # North 
                if(self.CheckCoord(i-1, y)):
                    if(self.table[i-1][y].mine):
                         n += 1

                # North Est
                if(self.CheckCoord(i-1, y+1)):
                    if(self.table[i-1][y+1].mine):
                         n += 1

                # Est
                if(self.CheckCoord(i, y+1)):
                    if(self.table[i][y+1].mine):
                         n += 1

                # South Est
                if(self.CheckCoord(i+1, y+1)):
                    if(self.table[i+1][y+1].mine):
                         n += 1
                 
                # South
                if(self.CheckCoord(i+1, y)):
                    if(self.table[i+1][y].mine):
                         n += 1

                # South West
                if(self.CheckCoord(i+1, y-1)):
                    if(self.table[i+1][y-1].mine):
                         n += 1
                
                # West
                if(self.CheckCoord(i, y-1)):
                    if(self.table[i][y-1].mine):
                         n += 1

                self.table[i][y].value = n

    
    """
    Print the board with arg for dev
 
    """ 
    def PrintDev(self):

        for i in range(self.height):

            for y in range(self.width):

                print("(" + str(self.table[i][y].mine) + "," + str(self.table[i][y].value) + "," + str(self.table[i][y].flag) + ")" , end = " ")
            
            print()

    """
    Print the minefield
 
    """ 
    def Print(self):

        for i in range(self.height):

            for y in range(self.width):

                print( self.table[i][y].__str__() , end = "")
                if(i == self.player.cursorX and y == self.player.cursorY):
                    print("*", end = "")
                else:
                    print(" ", end = "")
            
            print()




