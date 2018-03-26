import pygame
import copy
from color import *

def xbutton():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True

class Text:
	def __init__(self, screen, text, color, size, xoffset, yoffset, xcenter, ycenter):
		windowsize = pygame.display.get_surface().get_size()
		self.text = str(text)
		self.font = pygame.font.Font('fonts/Courier New.ttf', size)
		self.screen = screen
		self.textsurf = self.font.render(self.text, True, color)
		self.textrect = self.textsurf.get_rect()
		self.textrect.center = (windowsize[0]/2)*xcenter + xoffset, (windowsize[1]/2)*ycenter + yoffset
	
	def displaytext(self):
		self.screen.blit(self.textsurf, self.textrect)

class Screen:
	class _Text(Text):
		def __init__(self, text, key=None):
			super().__init__(*text)
			if key == 'nan' or key == None:
				self.key = None
			else:
				self.key = eval('pygame.K_'+key)

	def __init__(self, screen, *args, **kwargs):
		self.textlist = []
		for a in args:
			self.textlist.append(self._Text(a))
		self.screen = screen
		for k,v in kwargs.items():
			self.textlist.append(self._Text(v, k))

	def loop(self):
		self.screen.fill(black)
		for _t in self.textlist:
			_t.displaytext()
		pygame.display.update()

		while True:
			if xbutton():
				return pygame.K_q
			key = pygame.key.get_pressed()
			for _t in self.textlist:
				if _t.key == None:
					continue
				elif key[_t.key]:
					return _t.key