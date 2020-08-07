# try except 구문을 사용하여 예외 처리 하기

# 문법

#   try:
#       예외가 발생할 가능성이 있는 코드
#   except:
#       예외가 발생했을때 실행할 코드

# 설명 : 예외가 발생할 가능성이 있는 코드를 모두 try구문안에 넣고
# 예외가 발생했을때 실행할 코드를 모두 except구문 안에 넣으면 된다.

# 이렇게 예외처리를 하면 어떤 상황에 예외가 발생하는지 완벽하게 이해하고 있지 않아도
# 프로그램이 강제로 죽어버리는 상황을 막을 수 있다.

user_input_a = int(input("정수를 입력하세요 : ")) # 예외가 발생

try:
    number_input_a = int(user_input_a)
    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2 * 3.14 * number_input_a)
    print("원의 넓이 ", 3.14 * number_input_a * number_input_a)
except:
    print("예외가 발생했다네 정수만 입력하시게")
