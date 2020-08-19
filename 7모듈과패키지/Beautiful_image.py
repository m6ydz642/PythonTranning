

# https://movie.naver.com/movie/bi/mi/basic.nhn?code=15729


import urllib.request
from bs4 import  BeautifulSoup

print("Beginning file download with urlib2.......")
url ="https://movie.naver.com/movie/bi/mi/basic.nhn?code=15729"
res = urllib.request.urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(res, "html.parser")

soup = soup.find("div", class_="poster")

imgUrl = soup.find("img")["src"]

print(imgUrl)


urllib.request.urlretrieve(imgUrl, soup.find("img")["alt"] + '.jpg')  # img.alt는 이미지 명 ==  마약왕


