class Player:
	def __init__(self, x, y):
		self.seglist = [Segment(x, y)]
		self.dir     = 'r'
	class Segment:
		def __init__(self, x, y):
			self.x = x
			self.y = y