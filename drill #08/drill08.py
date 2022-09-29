from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    #global idle
    global dir
    global upDown
    global rightLeft

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                rightLeft = True
                dir += 1
            elif event.key == SDLK_LEFT:
                rightLeft = False
                dir -= 1
            elif event.key == SDLK_UP:
                upDown += 1
            elif event.key == SDLK_DOWN:
                upDown -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key ==SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                upDown -= 1
            elif event.key == SDLK_DOWN:
                upDown += 1

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
rightLeft = True
#if running == False:
    # idle = True
# elif running == True:
#     idle = False

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir = 0
upDown = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if rightLeft == True:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

    elif rightLeft == False:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8
    x += dir * 5
    y += upDown * 5
    handle_events()

# while idle:
#     clear_canvas()
#     tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
#     character.clip_draw(frame * 100, )

close_canvas()