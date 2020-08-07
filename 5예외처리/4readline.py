# 특정 파일의 첫번째 줄을 읽어오는 예제
f = open("C:\doit\새파일.txt","r")

while True: # 무한 반복 하면서
    line = f.readline() # 한줄을 읽어
    if not line: # 더 읽을 줄이 없으면 빠져나감
        break
    print(line)

f.close() # file 객체 자원 해제


# 예제. 파이썬으로 작성한 프로그램에서 외부 파일의 내용을 읽어 들이는 방법으로
# readline함수 사용하기
# 4readline.py만들어서 실습

# 예제. 파이썬으로 작성한 프로그램에서 외부 파일의 모든 내용을 읽어 들이는 방법으로
# readlines 함수 사용하기

# 5readlines.py 파일 만들어서 실습

