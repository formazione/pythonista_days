from scene import *


class Game(Scene):
	
	def setup(self):
		self.background_color = "#3b21b5"
		ground = Node(parent=self)
		x = 0
		while x <= self.size.w +64:
			tile = SpriteNode('plf:Ground_Dirt', position=(x,10))
			ground.add_child(tile)
			x += 64
		# create player sprite
		self.player = SpriteNode('plf:AlienGreen_front')
		
		# position
		self.player.position = (self.size.w / 2, 41)
		
		# anchor
		self.player.anchor_point = (0.5, 0)
		
		# attach the player the ground (make it visible)
		ground.add_child(self.player)

run(Game(), LANDSCAPE)
