from pico2d import *
import os

os.chdir('c:/2021170045_2DGP_DRILL/2021170045_2DGP_DRILL/drill #07')

open_canvas()

grass = load_image('grass.png')
character = load_image('penguin.png')


frame = 0

x = 0
while(x < 800):
    clear_canvas()
    grass.draw(400, 180)
    character.clip_draw(frame * 128, 1792, 128, 128, x, 240, 100, 100)
    update_canvas()
    frame = (frame + 1) % 7
    x += 20
    delay(0.1)
    get_events()

y = 0
while(y < 600):
    clear_canvas()
    character.clip_draw(frame * 128,  896, 128, 128, 400, y, 100, 100)
    update_canvas()
    frame = (frame + 1) % 12
    y += 20
    delay(0.1)
    get_events()

y = 0
while(y < 600):
    clear_canvas()
    character.clip_draw(frame * 128, 1408, 128, 128, 150, y, 100, 100)
    update_canvas()
    frame = (frame + 1) %5 + 6
    y += 20
    delay(0.1)
    get_events()

x = 0
while(x < 800):
    clear_canvas()
    grass.draw(400, 180)
    character.clip_draw(frame * 128, 1664, 128, 128, x, 240, 100, 100)
    update_canvas()
    frame = (frame + 1) % 12
    x += 20
    delay(0.1)
    get_events()

x = 0
while(x < 800):
    clear_canvas()
    grass.draw(400, 60)
    character.clip_draw(frame * 128, 640, 128, 128, x, 150, 100, 100)
    update_canvas()
    frame = (frame + 1) % 16
    x += 20
    delay(0.1)
    get_events()

x = 0
while(x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 128, 256, 128, 128, x, 90)
    update_canvas()
    frame = (frame + 1) % 12
    x += 20
    delay(0.1)
    get_events()

close_canvas()




