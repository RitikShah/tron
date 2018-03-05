from color import *
class Tron:
	def __init__(self, x, y):
		self.blocksize = 2
		self.p1 = self.Bike(x, y, self.blocksize)

	def keylistener(self, key):
		if key =='r' and self.p1.dir != 'l':
			self.p1.change_x = self.blocksize
			self.p1.change_y = 0
			self.p1.dir = 'r'
		elif key == 'l' and self.p1.dir != 'r':
			self.p1.change_x = -self.blocksize
			self.p1.change_y = 0
			self.p1.dir = 'l'
		elif key == 'u' and self.p1.dir != 'd':
			self.p1.change_y = -self.blocksize
			self.p1.change_x = 0
			self.p1.dir = 'u'
		elif key == 'd' and self.p1.dir != 'u':
			self.p1.change_y = self.blocksize
			self.p1.change_x = 0
			self.p1.dir = 'd'

	def update(self):
		self.p1.seglist.append(self.p1.Segment(self.p1.getx(0), self.p1.gety(0)))
		self.p1.setx(0, self.p1.getx(0) + self.p1.change_x)
		self.p1.sety(0, self.p1.gety(0) + self.p1.change_y)

	class Bike:
		class Segment:
			def __init__(self, x, y):
				self.x = x
				self.y = y

		def __init__(self, x, y, blocksize):
			self.blocksize = blocksize
			self.lead_x    = x
			self.lead_y	   = y

			self.change_x  = 0
			self.change_y  = 0

			self.seglist   = [self.Segment(x, y)]
			self.dir       = 'r'

			self.color 	   = whiteuu

		def trail(self):
			self.seglist.append(self.Segment(self.lead_x, self.lead_y))

		def getcolor(self):
			return self.color

		def getx(self, index):
			return self.seglist[index].x

		def gety(self, index):
			return self.seglist[index].y

		def setx(self, index, value):
			self.seglist[index].x = value

		def sety(self, index, value):
			self.seglist[index].y = value

		def displist(self, index):
			return [self.getx(index), self.gety(index), self.blocksize, self.blocksize]