# 매직 메소드

# __add__()메소드는 + 연산자 역할을 한다.

class coordinate:
    # 생성자
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 더하기 + 연산자 역할을 하는 메소드
    # self는 corrd1, other변수에는 coord2가 들어가서
    # self와 other로 지정한 두개의 숫자 묶음을 x는 x끼리 y는 y끼리 더하기를 해서
    # coordinate 클래스의 객체 형태로 변환하도록 한다는 뜻입니다

    def __add__(self, other):return coordinate(self.x + other.x, self.y + other.y)
coord1 = coordinate(5, 7)
coord2 = coordinate(3, 9)


class Student:
    def __init__(self, name, korean,math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

# 메소드
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

# 메소드 평균
    def get_average(self):
        return self.get_sum() / 4

    # 매개변수로 전달 받는 객체를 문자열 저봉로 만들어서 변환 해조는 메소드
    def __str__(self, student):
        return

    def __eq__(self,value): # 매개변수로 전달 받는 객체들의 점수의 총합이 같냐 묻는 메소드
        return self.get_sum() == value.get_sum()

    def __ne__(self, value): # 매개변수로 전달받는 객체들의 점수의 총합이 다르냐 묻는 메소드
        return self.get_sum() != value.get_sum()


# 학생 인스턴스들을 생성하여 리스트에 저장
student = [
    Student("윤인성보소", 87,98,88,95),
    Student("연하진", 92,98,88,95)
]






