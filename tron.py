import pygame
import random
from color import *

def init(ws):
	global blocksize, bikes, windowsize
	windowsize = ws

	blocksize = 2
	bikes = [Bike(25, ws[1]-25, blocksize), Bike(ws[0]-25, 25, blocksize)]

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

	if not bikes[0].dead:
		keylistener(bikes[0], uldr)

	if not bikes[1].dead:
		keylistener(bikes[1], wasd)

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
	for bike in bikes:
		if (bike.change_x != 0 or bike.change_y != 0) and not bike.dead:
			bike.seglist.append(bike.Segment(bike.getx(0), bike.gety(0)))
			bike.setx(0, bike.getx(0) + bike.change_x)
			bike.sety(0, bike.gety(0) + bike.change_y)
	collide()

def collide():
	for head in bikes:
		if head.dead:
			continue
		for bike in bikes:
			if bike.dead:
				continue
			for seg in bike.seglist:
				if head.seglist[0] is not seg:
					if head.seglist[0].x == seg.x and head.seglist[0].y == seg.y:
						kill(head)

def kill(bike):
	bike.dead = True

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
		self.dir       = ''

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