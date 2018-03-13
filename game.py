import pygame
import time
import random
import tron
from text import *
from color import *

def init(ws):
	global crashed, windowsize, blocksize, fps, keynone, clock, gamedisplay, keydict, sound
	global s_main, s_dead, s_help, t_play, t_quit, t_help, t_back, musicloop, t_empty
	pygame.init()

	pygame.mixer.init()
	musicloop = pygame.mixer.Sound('sounds/musicloop.wav')

	crashed = False
	windowsize = ws
	sound = False
	
	fps = 60
	keynone = tuple([0] * 323)

	clock = pygame.time.Clock()
	gamedisplay = pygame.display.set_mode(windowsize)
	pygame.display.set_caption('TR0N')
	
	tron.init()
	blocksize = tron.blocksize

	t_empty   = Text(gamedisplay, '')

	t_title   = Text(gamedisplay, 'TR0N', green, 100)
	t_over    = Text(gamedisplay, 'Game Over', red, 80)

	t_play    = Text(gamedisplay, 'C to play', yoffset=60)
	t_players = Text(gamedisplay, 'P to change amount of players', yoffset=80)
	t_quit    = Text(gamedisplay, 'Q to quit', yoffset=140)
	t_help    = Text(gamedisplay, 'H for more help', yoffset=120)
	t_back    = Text(gamedisplay, 'B to go back to the main menu', yoffset=100)
	t_sound   = Text(gamedisplay, 'S to toggle sound', yoffset=100)

	# help
	t_htitle  = Text(gamedisplay, 'Help Screen', blue, 70, ycenter=False, yoffset=60)
	t_hline1  = Text(gamedisplay, 'Rules: Do not touch the line the border', yoffset=-40)
	t_hline2  = Text(gamedisplay, 'There are two players: ', yoffset=0)
	t_hline3  = Text(gamedisplay, 'Top right is player 1', yoffset=20)
	t_hline4  = Text(gamedisplay, 'Bottom left is player 2', yoffset=40)
	t_hline5  = Text(gamedisplay, 'Try to survive as long as possible!', ycenter=False, yoffset=500)
	t_hline6  = Text(gamedisplay, 'Good Luck! (Press B to go back)', ycenter=False, yoffset=520)
	t_hline7  = Text(gamedisplay, 'Press Q to quit', ycenter=False, yoffset=540)
	t_hline8  = Text(gamedisplay, 'Press S to toggle sound', ycenter=False, yoffset=560)

	s_main    = Screen(gamedisplay, t_title, c=t_play, p=t_players, q=t_quit, h=t_help, s=t_sound)
	s_dead    = Screen(gamedisplay, t_over, c=t_play, q=t_quit, b=t_back)
	s_help    = Screen(gamedisplay, t_htitle, t_hline1, t_hline2, t_hline3, t_hline4, t_hline5, b=t_hline6, q=t_hline7, s=t_hline8)

def xbutton():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quitgame()

def quitgame():
	pygame.quit()
	quit()

def newgame():
	key(s_main.loop())

def gamewin(bike):
	s_win  = Screen(gamedisplay, Text(gamedisplay, bike.name + ' won!', bike.color, 80), c=t_play, q=t_quit, b=t_back)
	key(s_win.loop())

def gameover():
	key(s_dead.loop())

def players():
	if not len(tron.bikes) == tron.num:
		tron.updatebikes()
	s_players  = Screen(gamedisplay, Text(gamedisplay, "<   " + str(tron.num) + "   >", randcolor(), 80), b=t_back, LEFT=t_empty, RIGHT=t_empty)
	key(s_players.loop())

def key(output):
	global sound, musicloop
	if output == pygame.K_q:
		quitgame()
	elif output == pygame.K_c:
		tron.reset()
		gameloop()
	elif output == pygame.K_h:
		help()
	elif output == pygame.K_b:
		newgame()
	elif output == pygame.K_p:
		players()
	elif output == pygame.K_LEFT:
		if tron.num > 2:
			tron.num -= 1
		waitforrelease()
		players()
	elif output == pygame.K_RIGHT:
		if tron.num < 4:
			tron.num += 1
		waitforrelease()
		players()
	elif output == pygame.K_s:
		if not sound:
			musicloop.play(-1)
			musicloop.set_volume(0.5)
			sound = True
			newgame()
		else:
			musicloop.fadeout(2)
			sound = False
			newgame()

def help():
	key(s_help.loop())

def waitforrelease():
	pygame.event.pump()
	key = pygame.key.get_pressed()
	while not key == keynone:
		pygame.event.pump()
		key = pygame.key.get_pressed()
		clock.tick(fps)

def gameloop():
	while not crashed:
		xbutton()
		key = pygame.key.get_pressed()
		if key[pygame.K_q]:
			waitforrelease()
			gameover()
		else:
			tron.controls(key)

		# Display
		gamedisplay.fill(black)

		deadbikes = 0	
		for bike in tron.bikes:
			if not bike.dead:
				for index in range(len(bike.seglist)):
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

