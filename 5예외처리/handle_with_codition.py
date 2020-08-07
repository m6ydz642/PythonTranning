# 조건문으로 예외 처리 하기

user_input_a = input("정수를 입력하세요 : ")

# 입력받은 문자열을 숫자로 변환

# 이 코드는 정수를 입력하지 않았을 때 문제가 발생함

try:
    number_input_a = int(user_input_a)
    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2 * 3.14 * number_input_a)
    print("원의 넓이 ", 3.14 * number_input_a * number_input_a)
except:
    print("예외가 발생했다네 정수만 입력하시게")

# 또는 if 문

user_input_a = input("(if문 들어감) 정수를 입력하세요 : ")

if user_input_a.isdigit(): # true반환, true이면
    number_input_a = int(user_input_a)

    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2 * 3.14 * number_input_a)
    print("원의 넓이 ", 3.14 * number_input_a * number_input_a)

else:
    print("정수만 입력하시죠 ^^; ")

