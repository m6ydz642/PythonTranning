#숫자형 데이터

#1. 정수형 (Integer)

# 양수, 음수, 0

#a 라는 이름의 변수 메모리 공간에 123양의 정수를 저장 할 수 있다.

a = 123

print(a)

#a라는 이름의 변수 메모리 공간에 -178음의 정수를 저장 할 수 있다.

a = -178
print(a)


#2. 실수형 (floating-point)
#소수점
a = 1.2
print(a)

a = -3.45
print (a)


a = 4.24E10 # 4.24 * 10 의 10승 값
# a라는 이름의 변수 메모리 공간에 컴퓨터 지수표현 방식으로
# 4.24e10또는 4.24E10 실수를 저장 할 수 있다.
#
print(a)

a = 4.24e-10 #4.24e-10은 4.24 * 10의 -10승

print("10의 -10승" ,a)


#8진수와 16진수
# 8진수는 숫자 0 + 알파벳 소문자 o또는 대문자 O로 시작하는 숫자
a = 0o177 # 헷깔리네 숫자랑 ㅡ.ㅡ
print(a)

#16진수를 만들기 위해서는 0x로 시작하면 된다.
a = 0x8ff
print(a)

b = 0xABC
#8진수나 16진수는 파이썬에서 잘 사용하지 않는 형태의 숫자 자료형




