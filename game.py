import pygame
import time
import random
import tron
from text import *
from color import *

def init(ws):
	global crashed, windowsize, blocksize, fps, keynone, clock, gamedisplay, keydict
	global s_main, s_dead, t_play, t_quit, t_help
	pygame.init()

	crashed = False
	windowsize = ws
	
	fps = 60
	keynone = tuple([0] * 323)

	clock = pygame.time.Clock()
	gamedisplay = pygame.display.set_mode(windowsize)
	pygame.display.set_caption('TR0N')
	
	tron.init()
	blocksize = tron.blocksize

	t_title = Text(gamedisplay, 'TR0N', green, 100)
	t_gameover = Text(gamedisplay, 'Game Over', red, 80)

	t_play  = Text(gamedisplay, 'C to play', yoffset=60)
	t_quit  = Text(gamedisplay, 'Q to quit', yoffset=80)
	t_help  = Text(gamedisplay, 'H for more help', yoffset=100)

	s_main  = Screen(gamedisplay, t_title, c=t_play, q=t_quit)
	s_dead  = Screen(gamedisplay, t_gameover, c=t_play, q=t_quit)

def xbutton():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quitgame()

def quitgame():
	pygame.quit()
	quit()

'''
def textobjects(text, color=red, size=20, font_type='fonts/Courier New.ttf'):
	text = str(text)
	font = pygame.font.Font(font_type, size)
	textsurf = font.render(text, True, color)
	return textsurf, textsurf.get_rect()

def displaytext(text, x_displace=0, y_displace=0, color=red, size=20):
	textsurf, textrect = textobjects(text, color, size)
	textrect.center = (windowsize[0]/2) + x_displace, (windowsize[1]/2) + y_displace
	gamedisplay.blit(textsurf, textrect)
'''
'''
def screen(title, sub1, sub2):
	gamedisplay.fill(black)
	title.displaytext()
	sub1.displaytext()
	sub2.displaytext()
	pygame.display.update()

def screenupdate()

def startscreen():
	intro = True
	gamedisplay.fill(black)
	displaytext("TR0N", color=green, size = 100)
	
	displaytext("C to play", 0, 60, white)
	displaytext("Q to quit", 0, 80, white)
	pygame.display.update()

	while intro:
		xbutton()
		key = pygame.key.get_pressed()
		if key[pygame.K_q]:
			quitgame()
		if key[pygame.K_c]:
			intro = False
			gameloop()

		clock.tick(fps/4)
'''

def newgame():
	output = s_main.loop()
	if output == pygame.K_q:
		quitgame()
	elif output == pygame.K_c:
		gameloop()

'''
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
'''

def gamewin(bike):
	s_win  = Screen(gamedisplay, Text(gamedisplay, bike.name + ' won!', bike.color, 80), c=t_play, q=t_quit)
	output = s_win.loop()
	if output == pygame.K_q:
		quitgame()
	elif output == pygame.K_c:
		init((800, 600))

def gameover():
	output = s_dead.loop()
	if output == pygame.K_q:
		quitgame()
	elif output == pygame.K_c:
		init((800, 600))

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
			for bike in tron.bikes:
				if not bike.dead:
					gamewin(bike)

		tron.update()

		pygame.display.update()
		clock.tick(fps)

