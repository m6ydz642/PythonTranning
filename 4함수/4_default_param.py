# 매개 변수의 기본값을 이용하여 함수 만들기
    # 함수를 선언할 때 미리 매개변수의 기본값을 설정 해 놓으면
    # 함수 호출 시 전달받지 못한 인수에 대해서는 설정해 놓은 기본값으로 자동 초기화 할 수 있다.


def print_n_times(value, n = 2):
    for i in range(n):
        print(value)


print_n_times("벨류", 5)