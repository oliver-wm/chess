
from player import Pawn, Castle, Horse, Bishop, Queen, King
from player import Pieces as p
from termcolor import colored

BLACK = 1
WHITE = -1

class Square(object):
	"""docstring for Square"""
	def __init__(self, x, y):
		super(Square, self).__init__()
		self.piece = None
		self.row = x
		self.col = y

class Board(object):
	"""docstring for Board"""
	def __init__(self):
		self.board = [ [Square(x,y) for x in range(8)] for y in range(8) ]
		
		for i in range(8):
			self.board[1][i].piece = Pawn(BLACK)
		self.board[0][0].piece = Castle(BLACK) 
		self.board[0][7].piece = Castle(BLACK) 
		self.board[0][1].piece = Horse(BLACK) 
		self.board[0][6].piece = Horse(BLACK) 
		self.board[0][2].piece = Bishop(BLACK) 
		self.board[0][5].piece = Bishop(BLACK) 
		self.board[0][3].piece = Queen(BLACK) 
		self.board[0][4].piece = King(BLACK) 

		for i in range(8):
			self.board[6][i].piece = Pawn(WHITE) 
		self.board[7][0].piece = Castle(WHITE)
		self.board[7][7].piece = Castle(WHITE)
		self.board[7][1].piece = Horse(WHITE)
		self.board[7][6].piece = Horse(WHITE) 
		self.board[7][2].piece = Bishop(WHITE)
		self.board[7][5].piece = Bishop(WHITE) 
		self.board[7][4].piece = Queen(WHITE)
		self.board[7][3].piece = King(WHITE) 

	# @staticmethod
	def print_board(self):
		for row in self.board:
			print("|", end='')
			for square in row:
				# print(square.piece.__dict__)
				if square.piece != None:
					colour = True if square.piece.colour == BLACK else False
				if square.piece == None:
					print(" * ",end='') 
				elif square.piece.type == p.PAWN:
					print(colored(" P ", 'red') if colour else colored(" P ", 'white'),end='')
				elif square.piece.type == p.KING:
					print(colored(" K ", 'red') if colour else colored(" K ", 'white'),end='')
				elif square.piece.type == p.QUEEN:
					print(colored(" Q ", 'red') if colour else colored(" Q ", 'white'),end='')
				elif square.piece.type == p.CASTLE:
					print(colored(" C ", 'red') if colour else colored(" C ", 'white'),end='')
				elif square.piece.type == p.BISHOP:
					print(colored(" B ", 'red') if colour else colored(" B ", 'white'),end='')
				elif square.piece.type == p.HORSE:
					print(colored(" H ", 'red') if colour else colored(" H ", 'white'),end='')
				print("|",end='')
			print()