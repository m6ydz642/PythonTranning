# 주제 : getter메소드 setter메소드

# 2 클래스 좀더 파헤치기.py 파일의 소스코드를 이용해
# 원둘레를 변경하고 싶다면 어떻게 해야 할까요?
# 클래스 외부에서 직접 __redius속성에 접근 할 수 없기 때문에
# 간접적으로 접근 할 수 있는 방법을 찾아야 한다
# getter setter메소드는 프라이빗으로 선언된 변수의 값은 추출하거나
# 변경할 목적으로 간접적으로 속성에 접근 하도록 해주는 메소드이다.



# math라는 이름의 모듈을 불러온다.
import math
# 클래스 선언
class Circle:
    def __del__(self, redius): # 생성자
        self.__redius = redius # 인스턴스 변수 -> 변수명으로 선언후 값을 저장함

    def get_circumference(self): # 메소드
        return 2 * math.pi * self.__redius # 인스턴스 변수에 저장된 값을 사용함

    def get_area(self): # 메소드
        return math.pi * (self.__redius ** 2) # 2번 곱함

    # 게터 세터 메소드 선언


#-----------------------------------------------------------------------------------------

# 원의 둘레와 넓이를 구한다.
circle = Circle(10)
print("#원의 둘레와 넓이를 구한다.")
print("원의 둘레 : ", circle.get_circumference() )
print("원의 넓이", circle.get_area())

print()

print("# __redius 프라이빗 인스턴스 변수의 값")
print(circle.__redius)

# 결론 : 클래스 내부에서 __redius를 사용하는 것은 문제 없지만 클래스 외부에서 __redius를 사용하려 할때 그런 속성은 없다는 오류를 출력한다.



