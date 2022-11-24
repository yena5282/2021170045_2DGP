import random
from pico2d import*
import game_world

class Ball:
    image = None
    balls = []

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = 50 + random.randint(-100,2000), random.randint(-100, 1150)

    def make_ball_list(self):
        global balls
        balls = [Ball() for i in range(100)]
        return balls

    def draw(self):
        self.image.draw(self.x, self.y,)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 21, self.y - 21, self.x + 21, self.y + 21

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)