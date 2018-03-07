import pygame
from color import *

def xbutton():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True

class Text:
	def __init__(self, screen, text, color=white, size=20, xoffset=0, yoffset=0, center=True):
		windowsize = pygame.display.get_surface().get_size()
		self.text = str(text)
		self.font = pygame.font.Font('fonts/Courier New.ttf', size)
		self.screen = screen
		self.textsurf = self.font.render(self.text, True, color)
		self.textrect = self.textsurf.get_rect()
		self.textrect.center = (windowsize[0]/2) + xoffset, (windowsize[1]/2) + yoffset
	
	def displaytext(self):
		self.screen.blit(self.textsurf, self.textrect)

class Screen:
	class _Text:
		def __init__(self, key, text):
			self.key  = key
			self.text = text

	def __init__(self, screen, title, **kwargs):
		self.textlist = [self._Text(None, title)]
		self.screen = screen
		for k,v in kwargs.items():
			key = 'pygame.K_'+k
			self.textlist.append(self._Text(key,v))

	def loop(self):
		self.screen.fill(black)
		for _t in self.textlist:
			_t.text.displaytext()
		pygame.display.update()

		while True:
			if xbutton():
				return pygame.K_q
			key = pygame.key.get_pressed()
			for _t in self.textlist:
				if _t.key == None:
					continue
				elif key[eval(_t.key)]:
					return eval(_t.key)