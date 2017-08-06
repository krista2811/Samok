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

	def __str__(self):
		return "AI"

	def update(self, gameBoard):
		self.gameBoard = gameBoard

	def constructSearchTree(self, x, y, num): #return tree
		_x = 0
		_y = 0

		if num > 0:
			root = Tree()
			for i in range(7):
				for j in range(7):
					_x = i + x - 2
					_y = j + y - 2
					#_x, _y should be inside the gameBoard
					if(_x < 19 and _x >= 0 and _y < 19 and _y >= 0):
						if self.gameBoard[_y][_x] == self.BLANK:
							node = Tree()
							node = self.constructSearchTree(_x, _y, num - 1)
							node.parent = root
							root.children.append(node)

			return root

		else:
			node = Tree()
			#print("appendingposition "+str(x)+", "+str(y))
			node.position.append(x)
			node.position.append(y)
			#print(node.position)
			if self.checkOneLine_num(x, y, 4):
				node.data = 4
			elif self.checkOneLine_num(x, y, 3):
				node.data = 3
			elif self.checkOneLine_num(x, y, 2):
				node.data = 2
			elif self.checkOneLine_num(x, y, 1):
				node.data = 1
			else:
				node.data = 0
			#print(node.data)
			return node

	def calculateTree(self, x, y):
		tree = self.constructSearchTree(x, y, 1)
		(alphabetaValue, alphabetaPosition) = self.alphabeta(tree, 1, -9999, 9999, True, [0,0])
		print(alphabetaPosition)
		return alphabetaPosition


	def alphabeta(self, node, depth, alpha, beta, maximizingPlayer, position):
		if depth == 0 or node.children == None:
			return (node.data, node.position)
		if maximizingPlayer:
			v = -9999
			for child in node.children:
				(alphabetaValue, alphabetaPosition) = self.alphabeta(child, depth - 1, alpha, beta, False, position)
				v = max(v, alphabetaValue)
				if v == alphabetaValue:
					#print("wow")
					position = alphabetaPosition
					#print(position)
				alpha = max(alpha, v)
				if beta <= alpha:
					break
			return (v, position)

		else:
			v = 9999
			for child in node.children:
				(alphabetaValue, alphabetaPosition) = self.alphabeta(child, depth - 1, alpha, beta, False, position)
				v = min(v, alphabetaValue)
				if v == alphabetaValue:
					position = alphabetaPosition
				beta = min(beta, v)
				if beta <= alpha:
					break
			return (v, position)
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
