# 상속이란?
#   -새로운 클래스를 만들 때 기존에 만들 었던 클래스의 기능을 그대로 상속하면서
#   새로운 기능을 추가하는 것을 말함
# 이때 기존에 만들 었떤 클래스를 부모 클래스 또는 기초 클래스라고 부르며,
# 상속을 통해서 새롭게 생성되는 클래스를 자식 클래스 또는 파생클래스라고 한다

#-----------------------------------------------------------------------------------------
# 클래스 상속 하기 문법
    # class 자식 클래스 명 extends부모 클래스 명 :

    # 설명 : 파이썬에서 클래스를 선언할 때 다른 클래스를 상속받고 싶다면?
    # 소괄호()를 사용하여 그 안에 상속받고 싶은 클래스명을 넣어 전달함으로써
    # 해당 클래스의 모든 멤버를 상속받을 수 있다.


# 예제
class Bird: # 부모클래스
    def __init__(self):
        self.flying = True

    def birdsong(self):
        print("새소리")

class Sparrow(Bird): #Sparrow클래스가 Bird 클래스를 상속받아 선언됨
    def birdsong(self):
        print("개소리")


my_pet = Sparrow() # 자식 클래스
# 이때 Sparrow클래스는 Bird클래스를 상속받았기 때문에, Sparrow클래스에서 선언하지 않았지만
# 부모클래스만 Bird클래스에 존재하는 flying 속성값이 True를 자유롭게 사용할 수 있는 것이다.

my_biard = Bird() # 부모 호출


print(my_pet.flying) # true
my_pet.birdsong() # 개소리 호출
my_biard.birdsong() # 새소리


my_pet.flying # Bird로 부터 상속받은 자식객체가 부모의 속성값을 사용할 수 있음

#--------------------------------------------------------
# 메소드 오버라이딩
# 상속관계에 있는 부모클래스에서 이미 정의된 메소드를 자식 클래스에서 같은 이름으로 사용하되
# 메소드의 구현부만 재정의 해서 사용하는 것을 메소드오버라이딩이라고 한다.

class Bird: # 부모클래스
    def __init__(self):
        self.flying = True

    def birdsong(self):
        print("새소리")

class Sparrow(Bird): # Sparrow클래스가 Bird 클래스를 상속받아 선언됨
    def birdsong(self): # Bird클래스의 메소드를 재정의 했음 (오버라이딩 했음)
        print("개소리")


class Chicken(Bird): # ㅠㅠ
    # 생성자
    def __int__(self):
        self.flying = False # 생성자 오버라이딩

# --------------------------------------------------------

my_sparrow = Sparrow() # 인스턴스 생성

my_chicken = Chicken() # 자식 인스턴스 생성

my_sparrow.birdsong() # 짹짹

my_chicken.birdsong() # 새소리

