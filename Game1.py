# coding: utf-8

from scene import *
import sound


ypos = 41

# standing and walking texture
standing = Texture('plf:AlienGreen_front')
walking = [Texture('plf:AlienGreen_walk1'), Texture('plf:AlienGreen_walk2')]


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
		self.player.position = (self.size.w/2, 41)
		
		# anchor
		self.player.anchor_point = (0.5, 0)
		
		# attach the player the ground (make it visible)
		ground.add_child(self.player)
		
		# walk_state
		self.walk_state = -1
		
	def update(self):
		global xpos
		global ypos
		g = gravity()
		if abs(g.y) > 0.05:
			speed = g.x * 50
			xpos = max(0, min(self.size.w, self.player.position.x + speed))
			self.player.position = xpos, ypos
		
		# animate the walk
		step = int(self.player.position.x / 40) % 2
		if step != self.walk_state:
			self.player.texture = walking[step]
		else:
			self.player.texture = standing
		
	
	def touch_began(self, touch):
		global xpos, ypos
		# load the sprite
		laser = SpriteNode('plf:LaserPurpleDot',
			position=self.player.position,
			parent=self)
			
		 # moving the laser
		laser.run_action(Action.sequence(Action.move_by(0,1000), Action.remove()))
		
		# sound to the laser
		
		sound.play_effect('arcade:Laser_1')
		
		
		 
		 
		
						
run(Game(), PORTRAIT)
