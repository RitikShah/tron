import pygame
from color import *

def xbutton():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True

class Text:
	def __init__(self, screen, text, color=white, size=20, xoffset=0, yoffset=0, xcenter=True, ycenter=True):
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
	class _Text:
		def __init__(self, key, text):
			if key == 'nan' or key == None:
				self.key = None
			else:
				self.key = eval('pygame.K_'+key)
			self.text = text

	def __init__(self, screen, *args, **kwargs):
		self.textlist = []
		for a in args:
			self.textlist.append(self._Text(None, a))
		self.screen = screen
		for k,v in kwargs.items():
			self.textlist.append(self._Text(k,v))

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
				elif key[_t.key]:
					return _t.key