from enum import Enum

class Pieces(Enum):
	PAWN   = 0
	CASTLE = 1
	HORSE  = 2
	BISHOP = 3
	QUEEN  = 4
	KING   = 5


class Piece(object):
	def __init__(self, colour):
		self.colour = colour

class Pawn(Piece):

	def __init__(self, arg):
		super(Pawn, self).__init__(arg)
		self.type = Pieces.PAWN

	def get_moves(self, row, col):
		pass

	def convert(self):
		pass

class Castle(Piece):

	def __init__(self, arg):
		super(Castle, self).__init__(arg)
		self.type = Pieces.CASTLE

	def get_moves(Piece):
		pass

	def convert(Piece):
		pass

class Horse(Piece):

	def __init__(self, arg):
		super(Horse, self).__init__(arg)
		self.type = Pieces.HORSE

	def get_moves(Piece):
		pass

	def convert(Piece):
		pass

class Bishop(Piece):

	def __init__(self, arg):
		super(Bishop, self).__init__(arg)
		self.type = Pieces.BISHOP

	def get_moves(Piece):
		pass

	def convert(Piece):
		pass

class Queen(Piece):

	def __init__(self, arg):
		super(Queen, self).__init__(arg)
		self.type = Pieces.QUEEN

	def get_moves(Piece):
		pass

	def convert(Piece):
		pass

class King(Piece):

	def __init__(self, arg):
		super(King, self).__init__(arg)
		self.type = Pieces.KING

	def get_moves(Piece):
		pass

	def convert(Piece):
		pass