class Star:
    name = 'Start' # 클래스 변수
    x = 100 # 클래스 변수

    def change():
        x = 200
        print('x is ', x)

print('x is ', Star.x) # 클래스 변수 액세스
Star.change() # 클래스 함수 호출

star = Star() # 생성자가 없는데 생성 됨?? - ㅇㅇ
print(type(star))
print(star.x) # 비록 객체 변수로 액세스 했으나, 같은 이름의 클래스 변수가 우선.

star.change() # Star.change(star)와 동일 --> 파이썬은 객체.함수를 호출하면 그 객체의 클래스를 찾아서 그 속의 함수를 호출한다. 이때 그 함수에 자기 자신을 첫 arguments로 호출함. --> 그래서 self 필요