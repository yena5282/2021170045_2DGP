import pico2d
import play_state
import logo_state
start_state = logo_state # 모듈을 변수로 저장

pico2d.open_canvas()
start_state.enter() # 초기화
#게임 로프
while start_state.running:
    start_state.handle_events()
    start_state.update()
    start_state.draw()
    pico2d.delay(0.05)
start_state.exit() # 종료
pico2d.close_canvas()

