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

	t_empty   = (gamedisplay, '', white, 20, 0, 0, True, True)

	t_title   = (gamedisplay, 'TR0N', green, 100, 0, 0, True, True)
	t_over    = (gamedisplay, 'Game Over', red, 80, 0, 0, True, True)

	t_play    = (gamedisplay, 'C to play', white, 20, 0, 60, True, True)
	t_players = (gamedisplay, 'P to change amount of players', white, 20, 0, 80, True, True)
	t_quit    = (gamedisplay, 'Q to quit', white, 20, 0, 140, True, True)
	t_help    = (gamedisplay, 'H for more help', white, 20, 0, 120, True, True)
	t_back    = (gamedisplay, 'B to go back to the main menu', white, 20, 0, 100, True, True)
	t_sound   = (gamedisplay, 'S to toggle sound', white, 20, 0, 100, True, True)

	# help
	t_htitle  = (gamedisplay, 'Help Screen', blue, 20, 0, 60, True, False)
	t_hline1  = (gamedisplay, 'Rules: Do not touch the line the border', white, 20, 0, -40, True, True)
	t_hline2  = (gamedisplay, 'There are two players: ', white, 20, 0, -20, True, True)
	t_hline3  = (gamedisplay, 'Top right is player 1', white, 20, 0, 20, True, True)
	t_hline4  = (gamedisplay, 'Bottom left is player 2', white, 20, 0, 40, True, True)
	t_hline5  = (gamedisplay, 'Try to survive as long as possible!', white, 20, 0, 500, True, False)
	t_hline6  = (gamedisplay, 'Good Luck! (Press B to go back)', white, 20, 0, 520, True, False)
	t_hline7  = (gamedisplay, 'Press Q to quit', white, 20, 0, 540, True, False)
	t_hline8  = (gamedisplay, 'Press S to toggle sound', white, 20, 0, 560, True, False)

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
	s_win  = Screen(gamedisplay, (gamedisplay, bike.name + ' won!', bike.color, 80, 0, 0, True, True), c=t_play, q=t_quit, b=t_back)
	key(s_win.loop())

def gameover():
	key(s_dead.loop())

def players():
	if not len(tron.bikes) == tron.num:
		tron.updatebikes()
	s_players  = Screen(gamedisplay, (gamedisplay, "<   " + str(tron.num) + "   >", randcolor(), 80, 0, 0, True, True), b=t_back, LEFT=t_empty, RIGHT=t_empty)
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
			waitforrelease()
			newgame()
		else:
			musicloop.fadeout(2)
			sound = False
			waitforrelease()
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