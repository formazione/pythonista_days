from scene import *
import numpy
import sound



class Game(Scene):
	
	def setup(self):
		self.tiles = [
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[1,0,0,0,2,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0],
			[1,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1],
			]
		self.add_ground()
		self.add_player()
		self.add_background()
		self.add_map()
	
	def update(self):
		''' this is constantly updated '''	
		#self.add_map()
		self.player_pos()
		self.check_collision()
		
		
	def add_ground(self):
		''' the root node. the window object, the main surface '''
		self.ground=Node(parent=self)
				
	def add_background(self):
		''' the color of the background ''' 
		self.background_color = '#20106e'
	
	def add_map(self):
		''' draw the tiles for under the player '''
		x = 32
		y = 800
		self.nodes = []
		for row in self.tiles:
				for i in row:
						if i == 1: 
							tile = SpriteNode('plf:Ground_Grass', position=(x, y))
							
							self.ground.add_child(tile)
						if i == 2:
							tile = SpriteNode('plf:Item_CoinGold', position=(x, y))
							self.ground.add_child(tile)

						
							
						x += 64
				x = 32
				y -= 64
				
						
		
			
	def add_player(self):
		self.player = SpriteNode('plf:AlienBeige_front')
		self.player.anchor_point=(0.5, 0)
		self.player.position = (self.size.w//2, 64)
		self.add_child(self.player)
		
	def touch_began(self, touch):
		x, y = touch.location
		px, py = self.player.position
		self.move_action = Action.move_to(x, 64, 0.7, TIMING_SINODIAL)
		self.player.run_action(self.move_action, 'move_action_key')
		
		
	def touch_ended(self, touch):
		self.player.remove_action("move_action_key")

	def player_pos(self):
		pcol, prow = self.player.position
		
		self.pcol = int(pcol // 64)
		self.prow = int(prow // 64+10)
		# self.pcol, self.prow = pcol, prow
		# return 0, 1 or 2 where the player is
		self.tile_content = self.tiles[self.prow][self.pcol]
		
	
	def check_collision(self):

		if self.tile_content == 2:
			self.tiles[self.prow][self.pcol] = 0
			sound.play_effect('arcade:Coin_1')
			self.ground.remove_from_parent()
			self.ground=Node(parent=self)
				
			# self.add_player()
			self.add_map()
		# print("tile 2 = ", self.tiles[self.prow][self.pcol])
		
		
		
	

run(Game(), LANDSCAPE, show_fps=True)