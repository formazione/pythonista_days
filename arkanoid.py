import scene
import sound
import random

class Brick(scene.SpriteNode):
    def __init__(self, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.size = (40, 20)
        self.color = random.choice(['#ff0000', '#00ff00', '#0000ff', '#ffff00'])

class Arkanoid(scene.Scene):
    def setup(self):
        self.background_color = '#000000'
        
        # Create paddle
        self.paddle = scene.SpriteNode(color='white')
        self.paddle.size = (80, 20)
        self.paddle.position = (self.size.w / 2, 50)
        self.add_child(self.paddle)
        
        # Create ball
        self.ball = scene.SpriteNode(color='white')
        self.ball.size = (20, 20)
        self.ball.position = (self.size.w / 2, 100)
        self.add_child(self.ball)
        
        # Set initial ball velocity
        self.ball_velocity = scene.Point(4, 4)
        
        # Create bricks
        self.bricks = []
        for row in range(5):
            for col in range(7):
                brick = Brick(position=(col * 60 + 40, row * 30 + 400))
                self.add_child(brick)
                self.bricks.append(brick)
        
        # Set up score
        self.score = 0
        self.score_label = scene.LabelNode('Score: 0', position=(50, self.size.h - 30))
        self.add_child(self.score_label)
    
    def update(self):
        # Move paddle
        self.paddle.position = (self.touch.location.x, 50)
        
        # Move ball
        self.ball.position += self.ball_velocity
        
        # Check for collisions with walls
        if self.ball.position.x <= 10 or self.ball.position.x >= self.size.w - 10:
            self.ball_velocity.x *= -1
        if self.ball.position.y >= self.size.h - 10:
            self.ball_velocity.y *= -1
        
        # Check for collision with paddle
        if self.ball.frame.intersects(self.paddle.frame):
            self.ball_velocity.y *= -1
            sound.play_effect('arcade:Bleep_1')
        
        # Check for collisions with bricks
        for brick in self.bricks[:]:
            if self.ball.frame.intersects(brick.frame):
                brick.remove_from_parent()
                self.bricks.remove(brick)
                self.ball_velocity.y *= -1
                self.score += 10
                self.score_label.text = f'Score: {self.score}'
                sound.play_effect('arcade:Explosion_1')
        
        # Check for game over
        if self.ball.position.y <= 0:
            self.game_over()
    
    def game_over(self):
        self.paused = True
        game_over_label = scene.LabelNode('Game Over', position=(self.size.w/2, self.size.h/2))
        self.add_child(game_over_label)

if __name__ == '__main__':
    scene.run(Arkanoid(), show_fps=False)
