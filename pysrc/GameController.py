import pygame
class GameController :

	"""
	This class should control the whole game events and interactions between the settlers and
	everything. Simply the whole game logic.
	"""

	def __init__ (self, game):
	
		self.game = game
		self.gfxengine = game.get_gfxengine()
		self.inputmanager = game.get_inputmanager()
		self.last_keyevent = None
		self.mysettler = Settler(self.gfxengine, 100, 100)
		self.mouse_is_down = False


	def tick (self):
	
		"""
		One cycle in the game loop
		"""
		self.move_settlers()
	
	def move_settlers(self):
		self.set_settler_direction_by_keyevents()
		self.set_settler_direction_by_mouseevents()
		self.mysettler.move()

	def set_settler_direction_by_keyevents(self):
		event = self.inputmanager.get_last_keyevent()
		if event == None:
			return
		dir = self.mysettler.get_direction()
		if event.type == pygame.KEYDOWN:	
			speed = 1
		elif event.type == pygame.KEYUP:
			speed = 0	
		if event.key == 274:
			dir.set_down(speed)
		elif event.key == 273:
			dir.set_up(speed)
		if event.key == 276:
			dir.set_left(speed)
		elif event.key == 275:
			dir.set_right(speed)

	def set_settler_direction_by_mouseevents(self):
		event = self.inputmanager.get_last_mouseevent()
		dir = self.mysettler.get_direction()
		if self.mouse_is_down or event != None and event.type == pygame.MOUSEBUTTONDOWN:	
			self.mouse_is_down = True
			mouse_x,mouse_y = pygame.mouse.get_pos()
			pos_x, pos_y = self.mysettler.get_pos()
			dir = self.mysettler.get_direction()
			if mouse_x > pos_x:
				dir.set_right(1) 
				print "right"
			elif mouse_x < pos_x:
				dir.set_left(1) 
				print "left"
			else:
				print "no left right"
				dir.set_left(0) 
				dir.set_right(0) 
			if mouse_y > pos_y:
				print "down!"
				dir.set_down(1)
			elif mouse_y < pos_y:
				print "up"
				dir.set_up(1)
			else:
				print "no up down"
				dir.set_down(0) 
				dir.set_up(0) 
		if event != None and event.type == pygame.MOUSEBUTTONUP:
			self.mouse_is_down = False
			self.mysettler.stop()
		

class Settler(object):

	def __init__(self, gfxengine, x, y):
		self.sprite = gfxengine.create_settler(x, y)
		self.direction = Direction()

	def move(self):
		self.sprite.y += self.direction.down
		self.sprite.y -= self.direction.up
		self.sprite.x -= self.direction.left
		self.sprite.x += self.direction.right

	def get_direction(self):
		return self.direction
	
	def get_pos(self):
		return (self.sprite.x, self.sprite.y)

	def stop(self):
		self.direction.right = 0
		self.direction.left = 0
		self.direction.up = 0
		self.direction.down = 0
		

class Direction(object):
	def __init__(self):
		self.right = 0
		self.left = 0
		self.up = 0
		self.down = 0
	def set_left(self, left):
		self.left = left
		self.right = 0
	def set_right(self, right):
		self.right = right
		self.left = 0
	def set_up(self, up):
		self.up = up
		self.down = 0
	def set_down(self, down):
		self.down = down
		self.up = 0
