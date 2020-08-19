# 주제 : 객체(인스턴스) 어떤 클래스로 부터 만들어 졌는지 확인할 수 있도록 할하는 isinstance()함수

# 문법
# is instance(인스턴스, 클래스)

# 설명 : 함수의 첫번째 매개변수에 객체(인스턴스), 두번째 매개변수에는 클래스를 입력한다.

# 이때 인스턴스가 해당 클래스를 기반으로 만들어 졌다면 True
# 전혀 상관이 없는 인스턴스와 클래스 관계라면 false를 리턴함

# 학생 클래스 선언
class Student:
    def study(self):
        print("공부를 한다.") # 웃기는 소리 하네
# 선생님 클래스 선언
class Teacher:
    def teach(self):
        print("학생을 가리킨다.")

# 교실 내부의 객체 리스트를 생성 한다.
classroom = [Student(), Student(), Teacher(), Student(), Student() ]
# 반복을 적용해서 적절한 함수를 호출하게 한다.
for person in classroom:
    if isinstance(person, Student):
        # print("person 인스턴스 내부" , person)
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

# 설명 : Sutdent와 Teacher클래스를 생성하고
# classroom이라는 리스트 내부에 객체ㄷ를을 넣습니다.
# 그리고 for 반복을 적용 했을때, 요소가 Student 클래스의 인스턴스인지...
# Teacher클래스의 인스턴스인지 확인하고 각각의 대상이 가지고 있는 적절한 함수를 호출한다.
