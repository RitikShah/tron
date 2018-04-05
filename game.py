import pygame
import time
import random
import tron
from text import *
from color import *
from helptext import *

def init(ws):
	global crashed, windowsize, blocksize, fps, keynone, clock, gamedisplay, keydict, sound
	global s_main, s_dead, s_help, t_play, t_quit, t_help, t_back, musicloop, t_empty, soundf
	pygame.init()

	pygame.mixer.init()

	try:
		musicloop = pygame.mixer.Sound('data/sounds/musicloop.wav')
		soundf = True
	except pygame.error:
		print('Sound file not found, disabling sound')
		soundf = False

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
	t_quit    = (gamedisplay, 'Q to quit', red, 20, 0, 140, True, True)
	t_help    = (gamedisplay, 'H for more help', white, 20, 0, 120, True, True)
	t_back    = (gamedisplay, 'B to go back to the main menu', white, 20, 0, 100, True, True)
	t_sound   = (gamedisplay, 'S to toggle sound', white, 20, 0, 100, True, True)

	h = Help(gamedisplay)
	s_main    = Screen(gamedisplay, t_title, c=t_play, p=t_players, q=t_quit, h=t_help, s=t_sound)
	s_dead    = Screen(gamedisplay, t_over, c=t_play, q=t_quit, b=t_back)
	s_help    = Screen(gamedisplay, h.t_title,  h.t_line1, h.t_line2, h.t_line3, h.t_line4, h.t_line5, h.t_line6, h.t_line7, h.t_line8, h.t_line9, h.t_line10, b=h.t_line11, s=h.t_line12, q=h.t_line13)

'''
def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)
'''
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
	if bike == None:
		s_win  = Screen(gamedisplay, (gamedisplay, "It's a Tie", randcolor(), 80, 0, 0, True, True), c=t_play, q=t_quit, b=t_back)
		key(s_win.loop())
	else:
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
		if not sound and soundf:
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
			gamewin(None)

		tron.update()

		pygame.display.update()
		clock.tick(fps)