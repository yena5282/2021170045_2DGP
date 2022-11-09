from pico2d import *
import game_framework
import play_state
import title_state

running = True              
image = None

def enter():
    global image
    image = load_image('add_delete_boy.png')
    pass

def exit():
    global image
    del image

def update():
    play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()
    # fill here
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_LEFTBRACKET:
                    print('delete one boy')
                    play_state.delete_one_boy()
                case pico2d.SDLK_RIGHTBRACKET:
                    print('add one boy')
                    play_state.add_one_boy()





