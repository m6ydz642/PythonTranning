# 함수 호출시 매개변수 이름을 직접적으로 지정해서 값을 입력하여 전달 받는 매개 변수를 키워드 매개변수라 부른다.

def print_n_times(*values, n = 2):
    for i in range (n):
        for value in values:
            print(value)

print_n_times("벨류 횟수, 벨류 횟수", 3)

# 매개변수 이름 n에 직접적으로 값을 저장하여 전달함
# n=3자체를 키워드 매개변수라고 부른다.

