import pygame
import time
import random
import tron
from color import *

def init(title):
	global crashed, windowsize, tron, blocksize, fps, keynone, clock, gamedisplay, keydict
	pygame.init()

	crashed = False
	windowsize = (800,600)
	tron.init(windowsize)
	blocksize = tron.blocksize
	fps = 60
	keynone = tuple([0] * 323)

	clock = pygame.time.Clock()
	gamedisplay = pygame.display.set_mode(windowsize)
	pygame.display.set_caption(title)

def xbutton():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quitgame()

def quitgame():
	pygame.quit()
	quit()

def textobjects(text, color=red, size=20, font_type='fonts/Courier New.ttf'):
	text = str(text)
	font = pygame.font.Font(font_type, size)
	textsurf = font.render(text, True, color)
	return textsurf, textsurf.get_rect()

def displaytext(text, x_displace=0, y_displace=0, color=red, size=20):
	textsurf, textrect = textobjects(text, color, size)
	textrect.center = (windowsize[0]/2) + x_displace, (windowsize[1]/2) + y_displace
	gamedisplay.blit(textsurf, textrect)

def startscreen():
	intro = True

	while intro:
		gamedisplay.fill(black)
		displaytext("TR0N", color=green, size = 100)
		
		displaytext("C to play", 0, 60, white)
		displaytext("Q to quit", 0, 80, white)
		pygame.display.update()

		xbutton()

		key = pygame.key.get_pressed()
		if key[pygame.K_q]:
			quitgame()
		if key[pygame.K_c]:
			intro = False
			gameloop()

		clock.tick(fps/4)

def newgame():
	startscreen()

def gameover():
	gamedisplay.fill(black)
	over = True

	displaytext("Game Over", color = red, size = 80)
	displaytext("C to play", 0, 60, white)
	displaytext("Q to quit", 0, 80, white)
	pygame.display.update()

	while over:
		xbutton()
		key = pygame.key.get_pressed()
		if key[pygame.K_q]:
			quitgame()
		elif key[pygame.K_c]:
			key = keynone
			over = False
			init('Comets - By Ritik Shah')
			newgame()

def gameloop():
	while not crashed:
		xbutton()
		key = pygame.key.get_pressed()

		if key[pygame.K_q]:
			key = keynone
			gameover()
		else:
			tron.controls(key)

		# Display
		gamedisplay.fill(black)

		deadbikes = 0	
		for bike in tron.bikes:
			for index in range(len(bike.seglist)):
				if not bike.dead:
					pygame.draw.rect(gamedisplay, bike.getcolor(), bike.displist(index))
			if bike.dead:
				deadbikes += 1
		
		if deadbikes >= len(tron.bikes)-1:
			gameover()

		tron.update()

		pygame.display.update()
		clock.tick(fps)

