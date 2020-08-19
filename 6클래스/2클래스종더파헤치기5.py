# 주제 : 클래스 함수
# 클래스 함수도 클래스 변수처럼 그냥 클래스가 가진 함수 이다.,
# 일반적인 함수로 만드나 클래스 함수로 만드나 사용에는 큰 차이가 없다.
# 다만 클래스가 가진 기능이라고 명시적으로 나타내는 것 뿐 이다.

# 1. 클래스 함수 만들기
# 방법 : @classmethod 데이코레이터 라고 부르는데 이 기호를 붙여서 함수를 만든다.

# class 클래스 이름 :
#   @classmethod
#   def클래스 함수명 (cls, 매개변수) :
#       함수 기능

#  설명 : 클래스 함수의 첫번째 매개변수에는 클래스 자체가 들어온다.
# 일반적으로 cls 라는 이름의 변수로 선언한다.


# 2. 클래스 함수 호출하기
    # 클래스 이름.함수명 (매개변수들로 전달한 인수들)

#   예제
class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수 (메소드)
    @classmethod
    def print(cls): #class student클래스 자체가 넘어옴
        print("----------------학생 목록----------------")
        print("이름 \t 총점 \t 평균")

        for student in cls.students: # Student클래스 이름.students클래스 변수이름이라고 적어도 상관없다.
            print(str(student)) # 문자열로 변환
        print("-----------------------------------------")

        # 인스턴스를 전달 받아 사용하는 함수
        # 생성자

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        print("{}번째 학생이 생성되었습니다".format(Student.count))
        Student.students.append(self) # 아래에서 Student()인스턴스를 생성하여
                                      # 위의 클래스 변수 students=[]리스트에 추가 ~


        # 인스턴스들의 점수의 총합을 계산하여 리턴
        def get_sum(self):
            return self.korean + self.math + self.english + self.science


        # 인스턴스가 가지는 점수들의 평균을 계산하여 리턴 하는 메소드
        def get_average(self):
            return self.get_sum() / 4

        def __str__(self):
            return "{} \t {}\t {} \t".format(self.name, self.get_sum(), self.get_average())

#--------------------------------------------------------------------------------------------

 # Student학생 인스턴스 생성
Student("윤인성보소", 87, 98, 88, 95)
Student("연하진", 92, 98, 88, 95)


# 현재 생성된 Student 학생 인스턴스의 정보들을 모두 출력한다.
Student.print()








