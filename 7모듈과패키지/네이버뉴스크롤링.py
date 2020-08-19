# 주제 : 파이썬으로 네이버 실시간 뉴스정보 크롤링 하기

#1. 웹 크롤링
# 웹을 돌아다니며 유용한 정보를 찾아 특정 데이터베이스로 수집해오는 작업, 또는 그러한 기술

#2. 웹크롤링에 필요한 모듈 설치 방법
# bs4 모듈 -> HTML요소들을 우리가 쉽게 사용할 수 있도록 파싱해 줄 수 있는 BeautifulSoup클래스가 존재하는 모듈
# 설치 하는 방법
#
# 명령프롬프트 창을 열어 pip install bs4 입력후 엔터키
# request모듈 -> 파이썬에서 웹 사이트에서 http 요청을 하기 위한 모듈
# 설치 방법
# 프롬프트 창을 열어 pip install request입력후 엔터키


# 3. 네이버 실시간 뉴스정보 크롤릴을 이용한 목적지 찾는 방법
# 목적지 페이지 : https://www.naver.com로 접속해서 f12를 누른다.

# 네이버 사이트에 접속하면 중간쯤에 연합뉴스 -> 실시간 최신정보 크롤링

# requests  모듈과 , bs4 모듈의 BeautifulSoup클래스 사용을 위해 모듈들을 불러옴

import requests
from bs4 import BeautifulSoup

# 네이버 사이트에 요청하기 위해 requests 모듈의 get()메소드를  호출하여 네이버 사이트의 전체 html소스를 불러옴

source = requests.get("https://www.naver.com/").text

# 일련의 문자열만 가지고는 원하는 데이터를 예쁘게 가져올 수 없기 때문에 BeaufifulSoup을 이용한다.
# 요청해서 받은 source변수의 데이터를 가지고 BeaufifulSoup객체에 html소스로 파싱 해야 한다고 옵션을 정하고
soup = BeautifulSoup(source, "html.parser")
index = 0
print(source)
hotkeys =

for key in hotkeys:
    index += 1
    print(str(index) +"," + key.text)



