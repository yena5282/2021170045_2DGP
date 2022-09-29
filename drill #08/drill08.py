from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def handle_events():
    global running
    global idle
    global dir
    global upDown
    global idleDir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            idle = False
        elif event.type == SDL_KEYDOWN:
            idle = False
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_UP:
                upDown += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_DOWN:
                upDown -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
                idle = False

        elif event.type == SDL_KEYUP:
            running = False
            if event.key == SDLK_RIGHT:
                idleDir = 0
                dir -= 1
            elif event.key == SDLK_LEFT:
                idleDir = 1
                dir += 1
            elif event.key == SDLK_UP:
                upDown -= 1
            elif event.key == SDLK_DOWN:
                upDown += 1

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = False
idle = True
idleDir = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir = 0
upDown = 0
# hide_cursor()

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if idleDir == 0:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif idleDir == 1:
        character.clip_draw(frame * 100, 100 , 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    x += dir * 5
    y += upDown * 5
    handle_events()

while idle:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if idleDir == 0:
        character.clip_draw(frame * 100, 301, 100, 100, x, y)
    elif idleDir == 1:
        character.clip_draw(frame * 100, 201, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    x += dir * 5
    y += upDown * 5
    handle_events()

close_canvas()




