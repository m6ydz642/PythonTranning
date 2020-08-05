# if문이란
# 프로그래밍에서 조건을 판단하여 해당 조건에 맞는 상황을 수행하는데 사용하는 제어문
# if문의 기본 구조
    #if 조건문 :
    # 수행할 문장 1
    # 수행할 문장 2
    # ........
    # else :
    #   수행할 문장A
    #   수행할 문장B

# 예제 1
money = True

if (money):
    print("머니가 트루, 택시를 탑시다")
else:
    print("걸어가 이자식아")

# 조건문에 비교 연산자를 사용하는 방법
# 예제 2
x = 3
y = 2
print("x와 y의 비교값 = ", x > y)
print("x와 y의 비교값 = ", x < y)
print("x와 y의 비교값 = ", x == y)
print("x와 y의 비교값 = ", x != y)

# 예제 3. 조건식 : 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가기
# if문 작성
money = 2000    # 2000원을 가지고 있다
if money >= 3000:
    print("택시 ㄱ")
else:
    print("돈이없네 ㅡ.ㅡ 걸어가자")

# 연산자       설명
# x or  y       x와 y둘중에 하나만 참이면 참이다.
# x and y       x와 y모드 참이어야 참이다.
# not  x        x가 거짓이면 참이다.

# 조건문 and, or not 연산자

# 예제 4. 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라. if문으로 작성
money = 2000
card = True
if (money >= 3000 or card): # money는 2000이지만 card True이기 때문에 조건문의 결과가 참이다.
    print("트루, 택시 타자") # 출력됨
else:
    print("걸어가야 됨 ^^;;; ") # 출력 되지 않음


# in    ->     ~안에 있는가?
# not in    ->   ~안에 없는가?

# 예제 5. 1이 [1,2,3] 리스트 안에 있는가? 라는 물음에 참이므로 True를 반환함
print(1 in [1,2,3])


# 예제 6. 1이 [1,2,3]리스트 안에 없는가? 라는 물음에 거짓이므로 False를 반환함
print(1 not in [1,2,3])


# 예제 7. 튜플에 in 적용한 예제
# 'a'가 ('a','b','c')튜플 안에 있는가? 라는 물음에 참이므로 True를 반환함
print('a' in ('a','b','c'))

# 예제 8. 문자열에 not in 적용한 예제
# 'j'가 python문자열 안에 없는가? 라는 물음에 참이므로 True를 반환함
print( 'j' not in 'python')


# 예제 9. 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라 in을 적용
pocket = ['paper','cellphone','money']
card = True

if 'money' in pocket:
    print("돈이 있넹 택시를 타자")
else:
    print("돈이 없넹 걸어가자")

# 다양한 조건을 판단하는 elif 문
# 예제 10. 아래의 조건들을 이용하여 if elif else 로 작성하시오

# 주머니에 돈이 있으면 "택시를 타고 가라"
# 주머니에 돈이 없고 카드가 있으면 "택시를 타고 가라"
# 주머니에 돈도 없고 카드도 없으면 "걸어가라"

print('-----------------------------------------')
print('예제 10 -------------------------------------')

if 'money' in pocket:
    print("돈이 있네 택시를 타자")
elif card:
    print("돈은 없는데 카드가 있네")
else:
    print("걸어가 임마")

print('-----------------------------------------')
print('예제 11 -------------------------------------')

# 예제 11
score = 70

if score >= 60:
    message = "success"
else:
    message = "fail"

print(message)


# 파이썬의 조건부 표현식을 사용하면 위의 코드를 간단히 표현 할 수 있다.
# 조건부 표현식 사용
print('if문 한줄로 사용-------------------------------------')
message = "success" if score >= 60 else "fail"
print(message)






















