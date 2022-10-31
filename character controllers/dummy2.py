class Player:
    name = 'Player'

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

player = Player()
player.where()

print(Player.name)
print(player.name)

Player.where(player) # 클래스가 아닌 클래스의 '함수'를 호출해준 것이기 때문에 내 이름 넣어줘야됨
