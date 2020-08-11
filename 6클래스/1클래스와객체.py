#예제 1. 클래스 선언하기

class Dog:
    #속성선언
    name="삼식이"
    age=3
    breed ="골든 리트리버"

    def bark(self):
        print(self.name + "가 짓는다")


# 예제 dog 인스턴스 생성하기
my_dog = Dog()
a = Dog().bark()

