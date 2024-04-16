# numbers = [1, 3, 5, 9]
# print(list(map(lambda n: n**2, numbers)))

# # class Car:
# #     def __init__(self, color, speed):
# #         self.color = color
# #         self.speed = speed
# #     def speedUp(self, v):
# #         self.speed = self.speed + v
# #         return self.speed
# #         pass
# #     def speedDown(self, v):
# #         self.speed = self.speed - v
# #         return self.speed
# class People :
#     def __init__(self, age=0, name=None):
#         self.__age = age
#         self.__name = name
#     def introMe(self):
#         print("Name :", self.__name, "age :", str(self.__age))

# class Teacher(People) :
#     def __init__(self, age=0, name=None, school=None) :
#         super().__init__(age, name) # 부모 클래스의 속성 할당. self 없음
#         self.school = school # 자신의 인스턴스 변수 추가

#     def showSchool(self):
#         print("My School is ", self.school)
        
        
        
        
#         from hello import *
#         p1 = People(29, "Lee")
#         p1. introMe()
        
#         t1 = Teacher(48, "kim", "High school")
#         t1. introMe()
        
#         t1.showSchool

from random import randint

# 플레이어의 초기 자본
money = 50

# 게임 시작
while money > 0 and money < 100:
    print(f"현재 가진 돈: ${money}")
    guess = input("동전의 앞면(1) 또는 뒷면(2)을 선택하세요: ")
    
    # 입력값 유효성 검사
    if guess not in ['1', '2']:
        print("잘못된 입력입니다. 1 또는 2만 입력하세요.")
        continue
    
    # 동전 던지기
    coin = randint(1, 2)
    
    # 결과 판정
    if str(coin) == guess:
        print("축하합니다! 맞췄습니다.")
        money += 9
    else:
        print("아쉽지만 틀렸습니다.")
        money -= 10

# 게임 종료 조건 판정
if money <= 0:
    print("모든 돈을 잃었습니다. 게임이 종료됩니다.")
elif money >= 100:
    print("축하합니다! $100을 달성하여 게임에서 승리하셨습니다.")
