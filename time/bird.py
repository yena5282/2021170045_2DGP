import random

from pico2d import *

import game_framework
import play_state

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            self.image = load_image('bird_animation.png')
        self.x, self.y = random.randint(0, 1400), random.randint(100, 500)
        self.dir = 1
        self.frame = 1

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.dir * 1
        if self.x > 1600:
            self.x = 1600
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        self.image.clip_draw(int(self.frame)*180, 170, 170, 180, self.x, self.y, 150, 160)

