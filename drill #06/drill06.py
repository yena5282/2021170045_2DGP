from pico2d import *
import math

open_canvas()


grass = load_image('grass.png')
character = load_image('character.png')

def move_square(x, y):
    while(x <= 750):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 15
        delay(0.01)
    while(y <= 550):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 15
        delay(0.01)
    while(x >= 50):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 15
        delay(0.01)
    while(y >= 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 15
        delay(0.01)

def move_circle(x, y, angle):
    for angle in range(0, 360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        angle = angle + 20
        x = 400 + (math.cos(angle / 360 * 2 * math.pi) * 200)
        y = 300 + (math.sin(angle / 360 * 2 * math.pi) * 200)
        delay(0.01)
        
while(True):
    x = 50
    y = 90
    move_square(x, y)
    angle = 0
    x = 600
    y = 300
    move_circle(x, y, angle)
    
close_canvas()
