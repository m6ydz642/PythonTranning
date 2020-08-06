#1. 변수의 유효 범위란?
# - 파이썬에서는 변수가 선언된 위치에 따라 해당 변수가 영향을 미치는 볌위까지 달라지며


# 이것을 변수의 유효 범위라고 부른다.

# 예를 들어, 함수 내부에서 선언된 변수는 해당 함수 내부에서만 사용할 수 있다.

# 함수 밖에서는 사용할 수 없다.

# - 유효 범위에 따른 변수의 종류

# 1. 지역변수
# 2. 전역 변수
#-----------------------------------------------------------------------------------------------------------------------

# 2. 지역변수
#   - 함수내에서 선언된 변수를 의미 한다.

# 예제 1
def func():
    local_var = "지역변수"
    print(local_var)


func()


# 예제 2
def func2():
    # 글로벌 키워드를 사용하여 해당 전역변수를 재선언 함
    global global_var
    print("func2()")
    local_var = "지역변수"
    print(local_var)

# 함수 밖에 전역 변수 선언
global_var = "글로벌변수"
print(global_var)
func2()

print("--------------------------------------------------------------------------------")
# 예제 3 함수 외부에서 선언된 전역 변수와 함수 내부에서 선언된 지역 변수의 이름이 같은 경우에는
#   global 키워드를 사용하지 않으면 전혀 별개의 변수로 취급되므로 주의해야 한다.

def func3():
    bar = "지역 bar"
    print(bar)

bar = "전역 bar"
print(bar)  # 전역
func3() # 지역
print("--------------------------------------------------------------------------------")



