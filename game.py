import pygame
import time
import random
import tron
from color import *

class Game:
	def __init__(self, title):
		pygame.init()

		self.crashed = False
		self.windowsize = (800,600)
		self.tron = tron.Tron(self.windowsize[0]/2, self.windowsize[1]/2)
		self.blocksize = self.tron.blocksize
		self.fps = 60

		self.clock = pygame.time.Clock()
		self.gamedisplay = pygame.display.set_mode(self.windowsize)
		pygame.display.set_caption(title)

	def xbutton(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quitgame()

	def quitgame(self):
		pygame.quit()
		quit()

	def textobjects(self, text, color=red, size=20, font_type='fonts/Courier New.ttf'):
		text = str(text)
		font = pygame.font.Font(font_type, size)
		textsurf = font.render(text, True, color)
		return textsurf, textsurf.get_rect()

	def displaytext(self, text, x_displace=0, y_displace=0, color=red, size=20):
		textsurf, textrect = self.textobjects(text, color, size)
		textrect.center = (self.windowsize[0]/2) + x_displace, (self.windowsize[1]/2) + y_displace
		self.gamedisplay.blit(textsurf, textrect)

	def startscreen(self):
		intro = True

		while intro:
			self.gamedisplay.fill(black)
			self.displaytext("TR0N", color=green, size = 100)
			
			self.displaytext("C to play", 0, 60, white)
			self.displaytext("Q to quit", 0, 80, white)
			pygame.display.update()

			self.xbutton()

			key = pygame.key.get_pressed()
			if key[pygame.K_q]:
				self.quitgame()
			if key[pygame.K_c]:
				intro = False
				self.gameloop(self.tron)

			self.clock.tick(self.fps/4)

	def newgame(self):
		self.startscreen()

	def gameloop(self, tron):
		while not self.crashed:
			self.xbutton()
			key = pygame.key.get_pressed()

			if key[pygame.K_q]:
				self.quitgame()
			if key[pygame.K_RIGHT]:
				tron.keylistener('r')
			elif key[pygame.K_LEFT]:
				tron.keylistener('l')
			elif key[pygame.K_UP]:
				tron.keylistener('u')
			elif key[pygame.K_DOWN]:
				tron.keylistener('d')

			# Display
			self.gamedisplay.fill(black)
			for index in range(len(tron.p1.seglist)):
				pygame.draw.rect(self.gamedisplay, tron.p1.getcolor(), tron.p1.displist(index))

			tron.update()

			if tron.p1.seglist[0].x > self.windowsize[0] or tron.p1.seglist[0].x < 0 or tron.p1.seglist[0].y > self.windowsize[1] or tron.p1.seglist[0].y < 0:
				self.gameover()

			pygame.display.update()
			self.clock.tick(self.fps)

