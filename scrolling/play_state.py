import random
import json
import os

from pico2d import *
import game_framework
import game_world
import ball

from boy import Boy
from ball import Ball
# fill here
from background import FixedBackground as Background

import server

balls = []

def enter():
    server.boy = Boy()




    game_world.add_object(server.boy, 1)

    server.background = Background()
    game_world.add_object(server.background, 0)

    balls = ball.Ball.make_ball_list(Ball)
    game_world.add_objects(balls, 0)
    game_world.add_collision_pairs(server.boy, balls, 'boy:ball')





def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            server.boy.handle_event(event)



def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            # if group == 'boy:ball'
            if group == 'boy:ball':
                Boy.ball_cnt += 1
                a.handle_collision(b, group)
                b.handle_collision(a, group)




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






