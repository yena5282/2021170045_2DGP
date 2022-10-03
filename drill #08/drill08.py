from pico2d import *
TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global acting
    global running
    global dir
    global upDown
    global rightLeft

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            acting = False

        elif event.type == SDL_KEYDOWN:
            running = True
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
                acting = False

        elif event.type == SDL_KEYUP:
            running = False
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

acting = True
running = False
rightLeft = True

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir = 0
upDown = 0

while acting:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if running == True:
        if rightLeft == True:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        elif rightLeft == False:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

    elif running == False:
        if rightLeft == True:
            character.clip_draw(frame * 100, 300, 100, 100, x, y)
        elif rightLeft == False:
            character.clip_draw(frame * 100, 200, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8
    x += dir * 5
    y += upDown * 5

    if x <= 20 :
        x = 20
    elif x >= 1260 :
        x = 1260
    if y >= 984 :
        y = 984
    elif y <= 40 :
        y = 40

    handle_events()

close_canvas()