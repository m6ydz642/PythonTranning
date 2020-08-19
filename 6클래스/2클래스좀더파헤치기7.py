# 프라이빗 변수
# 파이썬은 클래스 내부의 변수를 ??? 클래스 외부에서 사용하는 것을 막고 싶을 때
# 인스턴스 변수이름을? __<변수명> 형태로 선언 한다.




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


