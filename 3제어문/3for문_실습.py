# for문
# 반복해서 문장을 수행해야 할 경우  for문을 사용한다.

# for문의 기본구조
    # for 변수 in 튜플또는 문자열 또는 리스트:
    #   반복 수행 할 문장1
    #   반복 수행 할 문장2

# 설명 : 리스트나 튜플, 문자열의 첫번째 요소부터 마지막 요소까지 차례대로 변수에 대입되어
# 반복 수행 할 문장 1, 반복 수행 할 문장2 등이 수행 된다.



# 예제 1. for문 이해하기
test_list = ['one', 'two', 'three'] # 리스트 선언

# test_list변수에 저장된 리스트 요소의 갯수만큼 반복 하는데
# 리스트의 첫 번째 요소인 'one'이 먼저 먼저  i변수에 대입된 후
for i in [10,20,30]:
    print(i)

# 예제 2. 다양한 for문 사용
a = [ (1,2), (3,4), (5,6) ] # a리스트의 요소값을 튜플로 저장

# a리스트의 요소들의 개수 만큼 반복, 인덱스 위치 0의 (1,2)부터 for(first, last)변수 자리에 각각 대입된다.


for (first, last) in a:
    print(first,last)

# 예제 3. for문의 응용
# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다.
# 합격인지 불합격인지 결과를 보여주시오

# 문제 : 점수를 차례로 검사해서 합격했는지 불합격했는지 통보해주는 프로그램을 만들어 보자
# 학생 5명의 시험 점수를 리스트에 저장
marks = [90, 25, 67,45,80]

# 각각의 학생에게 번호를 붙여 주기 위해 number변수를 사용함
number = 0
for mark in marks: # 90, 25
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다" %number)
    else:
        print("%d번 학생은 불합격 입니다" %number)

# 예제 4. for문과 continue문을 사용
for mark in marks:
    number = number + 1
    #60점 미만인 학생은 continue문을 만나서 for문의 처음으로 돌아가게 하기

    if mark < 60: continue
    print("%d번 학생축하합니다. 합격입니다" %number)


# 예제 5. for문과 함께 자주 사용하는 range함수
# range함수는 숫자 리스트를 자동으로 만들어 주는 역할한다.
# range(시작숫자, 끝숫자)  형태로 사용하는데, 이때 끝 숫자는 포함되지 않는다.

a = range(10) # range(10) 은 0부터 10미만의 숫자를 포함하는 range객체를 만들어 준다.
print(a)


# 예제 6. for와 range함수를 사용하면 1부터 10까지 더하는 코드를 구현할 수 있다.

add = 0
for i in range(1,11): # 1부터 11까지
    add = add + i
print(add)

# 예제 7. for문과 range함수를 사용하면 소스 코드 단 ~~~ 4줄만으로 구구단을 출력할 수 있습니다

for i in range(2,10):
    for j in range(1,10):
        print(i," X " , j," = ", i*j)
    #print(i*j, end = " ")

# 설명 : 1번 for문에서 2부터 9까지의 숫자 (range(2,10))가 차례대로 i변수에 대입 된다.
# i변수 값이 처음 2일때 2번 for문을 만나게 된다. 2번 for문에서 1부터 9까지의 숫자 (range(1,10))가 j변수에 대입되고
# 그 다음 문장 print(i*j, end=" ")을 수행하게 된다.
# 그리고 end=""를 넣어 준이유는 해당 결과 값을 출력 할때 다음줄로 넘기지 않고 그 줄에 빈 공백을 주어
# 계속해서 출력함


dictonary = {"name":"건조망고",
             "type" : "당절임",
             "ingredient":["망고", "설탕", "등등"],
             "origin" : "필리핀"
             }
for key in dictonary:
    print(key, ":", dictonary[key])
    print("key : ", key)
