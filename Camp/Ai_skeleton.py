from Tree import*
import copy

class Ai:

	gameBoard = []
	BLACK = "black"
	WHITE = "white"
	BLANK = "*"

	VERTICAL = 0
	HORIZONTAL = 1
	RIGHTDOWN = 2
	RIGHTUP = 3

	def __init__(self, gameBoard):
		self.gameBoard = gameBoard
		print("AI is now constructed")

	def __str__():
		return "AI"

	def update(self, gameBoard):
		self.gameBoard = gameBoard

	def constructSearchTree(self, x, y, num): #return tree
		#=========================================================
	    #
	    # Construct basic minimax tree
	    # return Tree to do the recursion action
	    #
	    #=========================================================




	#====================================================================
    #
    # Return the position
    # use constructSearchTree to construct the basic minimax tree
    # use alphabeta(...) to do the alpha-beta pruning
    #
    #====================================================================
	def calculateTree(self, x, y):
		tree = self.constructSearchTree(x, y, 1)
		(alphabetaValue, alphabetaPosition) = self.alphabeta(tree, 1, -9999, 9999, True, [0,0])
		print(alphabetaPosition)
		return alphabetaPosition


	def alphabeta(self, node, depth, alpha, beta, maximizingPlayer, position):
		#=========================================================
	    #
	    # Do alpha-beta prunning algorithm
	    # Look at alpha-beta pruning sudo code
	    # Return position
	    # Implement here
	    #
	    #=========================================================
	#return bool
	def checkOneLine_num(self, x, y, num):
		if self.checkOneLine(self.WHITE, x, y, self.RIGHTUP, num) :
			return True
		elif self.checkOneLine(self.WHITE, x, y, self.RIGHTDOWN, num) :
			return True
		elif self.checkOneLine(self.WHITE, x, y, self.HORIZONTAL, num) :
			return True
		elif self.checkOneLine(self.WHITE, x, y, self.VERTICAL, num) :
			return True
		else:
			return False

	def checkOneLine(self, color, x, y, dir, len): #direction = int
	    flag = False
	    length = 0
	    localGameBoard = copy.deepcopy(self.gameBoard)

	    dx = 0;
	    dy = 0;
	    _x = 0
	    _y = 0

	    localGameBoard[y][x] = self.WHITE

	    if dir == self.RIGHTUP:
	        dx = 1
	        dy = -1
	    elif dir == self.RIGHTDOWN:
	        dx = 1
	        dy = 1
	    elif dir == self.HORIZONTAL:
	        dx = 1
	        dy = 0
	    elif dir == self.VERTICAL:
	        dx = 0
	        dy = 1

	    for i in range(len * 2 - 1):
	        _y = y + ((len - 1)*(-1))*dy + i * dy
	        _x = x + ((len - 1)*(-1))*dx + i * dx

	        if(_x < 19 and _x >= 0 and _y < 19 and _y >= 0):
	            if(flag) :   
	                    if(localGameBoard[_y][_x] == color) :
	                        length += 1
	                        if length == len:
	                            return True
	                    else:
	                        flag = False
	                        length = 0
	            else:
	                if(localGameBoard[_y][_x] == color):
	                    flag = True
	                    length += 1
