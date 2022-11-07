from pico2d import *
from game_world import*

class Grass:
    image = None
    def __init__(self, x, y):
        if Grass.image == None:
            self.image = load_image('grass.png')
        self.x, self.y = x, y

    def draw(self):
            self.image.draw(self.x, self.y)
    def update(self):
        pass

