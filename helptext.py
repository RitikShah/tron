from color import *
class Help():
	def __init__(self, gamedisplay):
		self.t_title  = (gamedisplay, 'Help Screen', blue, 60, 0, -160, True, True)
		self.t_line1  = (gamedisplay, 'Use the cooresponding keys to control your bike', white, 20, 0, -100, True, True)
		self.t_line2  = (gamedisplay, 'Do not run into:', white, 20, 0, -80, True, True)
		self.t_line3  = (gamedisplay, 'Any bike trails', white, 20, 0, -60, True, True)
		self.t_line4  = (gamedisplay, 'The window border', white, 20, 0, -40, True, True)
		self.t_line5  = (gamedisplay, 'The game can be played with 2 to 4 players: ', white, 20, 0, 0, True, True)
		self.t_line6  = (gamedisplay, 'Top right is player 1. Use wasd to move', white, 20, 0, 20, True, True)
		self.t_line7  = (gamedisplay, 'Bottom left is player 2. Use the arrow keys to move', white, 20, 0, 40, True, True)
		self.t_line8  = (gamedisplay, 'Top left is player 3. Use tfgh to move', white, 20, 0, 60, True, True)
		self.t_line9  = (gamedisplay, 'Bottom right is player 4. Use ijkl to move', white, 20, 0, 80, True, True)
		self.t_line10 = (gamedisplay, 'Try to survive as long as possible!', white, 20, 0, 100, True, True)
		self.t_line11 = (gamedisplay, 'Good Luck! (Press B to go back)', white, 20, 0, 500, True, False)
		self.t_line12 = (gamedisplay, 'Press S to toggle sound', white, 20, 0, 520, True, False)
		self.t_line13 = (gamedisplay, 'Press Q to quit', red, 20, 0, 540, True, False)