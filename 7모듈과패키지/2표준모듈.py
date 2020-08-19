# 표준 모듈 종류
# random모듈
# -> 랜덤값을 생성할때 사용하는 모듈

# rondom모듈 불러오기
import random

print("#랜덤 모듈")


# random모듈의 random()함수는 0.0 <= 랜덤값  < 1.0 랜덤값을 float를 리턴한다.

# print(range.random()) # 이거 range뭐지?


# random모듈의 uniform(min, max)함수는 지정한 범위 사이의 랜덤값을 float를 리턴합니다
print(random.uniform(10,20) )

# random모듈의 randrange()함수는 지정한 범위 사이의 랜덤값을 int로 리턴합니다
# 문법 ) ranrange(max) : 0부터 max값 사이의 랜덤값을 int로 리턴합니다
print(random.randrange(10) )

# 문법 ) randrange(min,max) : min값부터 max 값사이의 랜덤값을 int리턴합니다

print(random.randrange(10,20))

# random모듈의 choice (리스트) 함수는 리스트 내부에 있는 요소를 랜덤하게 선택한다.
print(random.choice([1,2,3,4,5]))


# random모듈의 shuffle(리스트) 함수는 리스트의 요소들을 랜덤하게 섞어서 제공해줌
list = ["ice cream", "pancakes", "brownies", "cookies","candy"]
random.shuffle(list)
print(list)


# random모듈의 sample(리스트, k=숫자) 함수는
# 리스트의 요소 중에 k개를 랜덤으로 뽑아낸다.
print(random.sample([1,2,3,4,5], k=2))

# 예제 계산 문제를 맞히는 게임  -> random.py 파일 생성
# 예제 타자 게임 -> typing.py파일로 생성



