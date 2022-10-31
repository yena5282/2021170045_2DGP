from pico2d import *

# 이벤트 정의
# RD, LD, RU, LU = 0, 1, 2, 3
RD, LD, RU, LU, TIMER, AUTO = range(6) # 타이머 이벤트 추가

key_event_table = {
    (SDL_KEYDOWN, SDLK_a): AUTO,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}


# 스테이트를 구현 -클래스를 이용해서-
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0 # 정지 상태
        self.timer = 1000 # 타이머 초기화

    @staticmethod
    def exit(self):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1 # 시간 감소
        if self.timer == 0: # 시간이 다되면,
            self.add_event(TIMER) # 타이머 이벤트를 큐에 삽입

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    @staticmethod
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self):
        print('EXIT RUN')
        # 런 상태를 나갈 때, 현재 방향을 저장해놓음
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        # 달리게 만들어준다.
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

class AUTO_RUN:
    @staticmethod
    def enter(self, event):
        print('ENTER AUTO_RUN')
        # if event == RD:
        #     self.dir += 1
        # elif event == LD:
        #     self.dir -= 1
        # elif event == RU:
        #     self.dir -= 1
        # elif event == LU:
        #     self.dir += 1

    @staticmethod
    def exit(self):
        print('EXIT AUTO_RUN')
        # 런 상태를 나갈 때, 현재 방향을 저장해놓음
        self.face_dir = self.dir
        self.dir = self.face_dir

    @staticmethod
    def do(self):
        # 달리게 만들어준다.
        self.frame = (self.frame + 1) % 8
        # if self.x >= 800:
        #         #     self.dir = -1
        #         #     self.x -= 1
        #         # elif self.x <= 0:
        #         #     self.dir = 1
        #         #     self.x += 1
        if self.dir == 1 or self.face_dir == 1:
            if self.x < 800:
                self.x += 1
            else:
                self.dir, self.face_dir = -1, -1
        elif self.dir == -1 or self.face_dir == -1:
            if self.x > 0:
                self.x -= 1
            else:
                self.dir, self.face_dir = 1, 1

        # self.x += self.dir
        # self.x = clamp(0, self.x, 800)
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y, 200, 200)
        if self.face_dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y, 200, 200)
        elif self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y, 200, 200)
class SLEEP:
    @staticmethod
    def enter(self, event):
        print('ENTER SLEEP')
        self.dir = 0 # 정지 상태

    @staticmethod
    def exit(self):
        print('EXIT SLEEP')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

    @staticmethod
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592/2, '',
                                           self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                            3.141592/2, '',
                                            self.x - 25, self.y - 25, 100, 100)


# 상태 변환
next_state = {
    AUTO_RUN: {RU: AUTO_RUN, LU:AUTO_RUN, RD:RUN, LD:RUN, TIMER: AUTO_RUN, AUTO_RUN: IDLE},
    SLEEP: {RU:RUN, LU:RUN, RD:RUN, LD:RUN, TIMER:SLEEP, AUTO: SLEEP},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER:SLEEP, AUTO:AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, TIMER:RUN, AUTO: AUTO_RUN}
}


class Boy:

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.event_q = []

        # 초기 상태 설정과 엔트리
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)
        if self.event_q:
            event = self.event_q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

    def add_event(self, event):
        self.event_q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

