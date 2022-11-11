from pico2d import *
import game_framework
import game_world

from grass import Grass
from boy import Boy
from ball import Ball

boy = None
grass = None
balls = []


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)

    # 리스트로 공들 객체 생성
    global balls
    balls = [Ball() for i in range(10)]
    game_world.add_objects(balls, 1)

    # 충돌 대상 정보를 등록
    game_world.add_collision_pairs(boy, balls, 'boy:ball')


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # 충돌 체크
    # 볼들과 소년의 충돌을 체크
    # for ball in balls.copy(): # 리스트 원본을 건드리는건 위험하기 때문에 카피본을 사용
    #     if collide(boy, ball):
    #         print('COLLISION boy:ball')
    #         balls.remove(ball)
    #         game_world.remove_object(ball)
    #         # 루프 끝나고 다시 들어갈 땐 볼 하나 사라진 원본을 카피한 카피본을 사용하게 됨
    #         # but 객체지향적 코드가 아니다 = 볼과 사람만의 충돌체크만 가능한 상황
    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True


def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
