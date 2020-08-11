

class Dog:
    def __init__(self, name): # 기본 생성자
        self.name = name
        print("생성자 내용 ", name)


def bark(self):
    print(self.name + "가 멍멍하고 짖는다")

my_dog = Dog("삼식이") # 인스턴스 생성 (객체 생성)시 매개변수가 하나인 생성자를 호출하여
                    # name 변수값을 초기화함



# my_dog.bark() # 인스턴스의 메소드 호출, 난왜 안되지 ㅋㅋㅋㅋㅋㅋ
bark(my_dog)


# 예제2. 클래스 내부에 생성자, 메소드 선언하기
class Student:
    # 생성자
    def __init__(self, name, korean, math, english, science):
        self.name  = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    #메소드 : 점수 합구하기
    def get_sum (self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    #메소드 만들기
    def to_string(self):
        return "{} \t{} \t{}".format(self.name, self.get_sum(), self.get_average())

#Student("윤인성",89, 100, 20, 95).get_sum()

#--------------------------------------------------------------------------------------------------
#Student 인스턴스를 생성하여 리스트에 저장
print("-------------------------------------------")
students  = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 88, 78)
]

#학생 한명의 정보씩 반복하여 출력
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())


# 예제3
#클래스에서도 변수가 선언된 위치에 따라 변수의 유효범위가 달라지며,
# 이에 따라 다음과 같이 구분 할 수 있다.

    #1. 클래스 변수
    # - 해당 클래스에서 생성된 모든 인스턴스가 값을 공유하는 변수
    #2 인스턴스 변수
    # - __init__생성자 내에서 선언된 변수로
    # 인스턴스가 생성될 때 마다 새로운 값이 할당 되는 변수

class Dog:
    # 클래스 변수
    sound = "멍멍"
    # 생성자 선언

    def __init__(self, name):
        #인스턴스 변수 선언
        self.name = name

    #일반 메소드 선언

    def bark(self):
        print(self.name + "가 멍멍하고 짖는다.")

# 인스턴스 생성
my_dog =  Dog ("멍멍이")
your_dog = Dog("콩이")

# 클래스 변수에 접근
print("-----------------------------------------")
print(your_dog.sound)
print(my_dog.name)
print("-----------------------------------------")


#print
















