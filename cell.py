class Cell(object):
    """
    Class how represent a cell of the minefield.
 
    """
    def __init__(self):
        self.mine = False  # There is a mine here ?
        self.flag = False  # There is a flag here ?
        self.show = False  # This cell is visible ?
        self.value = 0     # The number of neighbor(s) around it 

    def __str__(self):
        """
        Return a letter that represent the state of this cell.
 
        """
        if self.show:
            return str(self.value)
        elif self.flag:
            return 'F'
        else:
            return '.'


            


        