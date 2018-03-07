import pygame
import random
from color import *

def init():
	global blocksize, bikes, windowsize
	windowsize = pygame.display.get_surface().get_size()

	blocksize = 2
	bikes = [Bike("Player 1", 25, windowsize[1]-25, blocksize), Bike("Player 2", windowsize[0]-25, 25, blocksize)]

def reset(x, y):
	global blocksize, bikes
	blocksize = 2
	bikes = [Bike(x, y, blocksize), Bike(x, y, blocksize)]

def randcolor():
	return (
		round((random.randrange(0,255)+255)/2),
		round((random.randrange(0,255)+255)/2),
		round((random.randrange(0,255)+255)/2)
	)

def controls(key):
	uldr = (key[pygame.K_UP], key[pygame.K_LEFT], key[pygame.K_DOWN], key[pygame.K_RIGHT])
	wasd = (key[pygame.K_w], key[pygame.K_a], key[pygame.K_s], key[pygame.K_d])

	if not bikes[1].dead:
		keylistener(bikes[1], uldr)

	if not bikes[0].dead:
		keylistener(bikes[0], wasd)

def keylistener(bike, key):
	if key[0] and bike.dir != 'd':
		bike.change_y = -blocksize
		bike.change_x = 0
		bike.dir = 'u'
	elif key[1] and bike.dir != 'r':
		bike.change_x = -blocksize
		bike.change_y = 0
		bike.dir = 'l'
	elif key[2] and bike.dir != 'u':
		bike.change_y = blocksize
		bike.change_x = 0
		bike.dir = 'd'
	elif key[3] and bike.dir != 'l':
		bike.change_x = blocksize
		bike.change_y = 0
		bike.dir = 'r'

def update():
	movement()
	collide()
	border()
	for bike in bikes:
		if bike.isdying and not bike.dead:
			bike.selfdestruct()

def movement():
	for bike in bikes:
		if (bike.change_x != 0 or bike.change_y != 0) and not (bike.dead or bike.isdying):
			bike.seglist.append(bike.Segment(bike.getx(0), bike.gety(0)))
			bike.setx(0, bike.getx(0) + bike.change_x)
			bike.sety(0, bike.gety(0) + bike.change_y)

def collide():
	for head in bikes:
			if head.dead or head.isdying:
				continue
			for bike in bikes:
				if bike.dead or head.isdying:
					continue
				for seg in bike.seglist:
					if head.seglist[0] is not seg:
						if head.seglist[0].x == seg.x and head.seglist[0].y == seg.y:
							head.isdying = True

def border():
	for bike in bikes:
		if bike.dead or bike.isdying:
			continue
		if bike.seglist[0].x > windowsize[0] or bike.seglist[0].x < 0 or bike.seglist[0].y > windowsize[1] or bike.seglist[0].y < 0:
			bike.isdying = True

class Bike:
	class Segment:
		def __init__(self, x, y):
			self.x = x
			self.y = y

	def __init__(self, name, x, y, blocksize):
		self.name 	   = name

		self.blocksize = blocksize
		self.lead_x    = x
		self.lead_y	   = y

		self.change_x  = 0
		self.change_y  = 0

		self.anim	   = 0

		self.seglist   = [self.Segment(x, y)]
		self.dir       = ''

		self.isdying   = False
		self.dead	   = False

		self.color 	   = randcolor()

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

	def selfdestruct(self):
		try:
			self.seglist.pop()
			self.seglist.pop()
			self.seglist.pop()
		except IndexError:
			self.isdying = False
			self.dead    = True



