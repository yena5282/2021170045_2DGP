from pico2d import *
import game_framework
import play_state
import title_state

running = True
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('tuk_credit.png')
    pass

def exit():
    global image
    del image

def update():
    global logo_time
    # global running
    if logo_time > 0.5:
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()





