
# 함수의 가변 매개변수에 대해
# 함수를 실제로 호출할 때 몇개의 인수가 전달될지 미리 알 수 없다면
# 만들어져 있는 함수 호출시 매개변수의 값을 전달 할때 사용자가 직접 매개 변수의 개수를 정할 수 있도록
# 함수에.. 가변 매개변수를 생성해 놓을 수 있습니다

# 가변 매개변수 함수를 정의 하는 문법
# def 함수명 (매개변수, 매개변수, *가변 매개변수명):
#       실행할 코드 1
#       실행할 코드 2

# 가변 매개변수를 사용할 때의 제약 조건
#   - 가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
#   - 가변 매개변수는 하나만 사용 할 수 있다.

# 가변 매개변수 함수 만들기 예제
def print_n_times(n,*test):
    # n번 반복
    for i in range(n):
        #test는 리스트처럼 활용함
        print(n, test)

print_n_times(2, "음", "음")

# 설명 :  가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.

