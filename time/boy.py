# 속도 = 속성변화 / 시간

from pico2d import *

import game_framework
import play_state
import game_world
from ball import Ball

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

running = True
image = None

def enter():
    global image
    bird_image = load_image('bird_animation.png')
    pass

def exit():
    global bird_image
    del bird_image

def update():
    play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    bird_image.draw(800,300)
    update_canvas()
    # fill here
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()