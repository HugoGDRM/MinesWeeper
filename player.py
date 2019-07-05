class Player:

	def __init__(self):

		self.win = False
		self.dead = False
		self.cursorX = 0
		self.cursorY = 0
		
    # Check the number of flagged mines
	def checkScore(self, table):
		c = 0
		for i in range(len(table)):
			for y in range(len(table[0])):
				if table[i][y].mine and table[i][y].flag:
					c += 1
		return c

