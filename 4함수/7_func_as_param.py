# 함수 매개변수로 함수 전달 해보기

# 매개변수로 받은 print_hello()함수를 10번 호출하는 함수

def call_10_times(func):
    for i in range(10):
        func()


def print_hello():
    print("안녕하세요")

call_10_times(print_hello )
# 매개변수로 들어가는 거라서 print_hello()안씀



