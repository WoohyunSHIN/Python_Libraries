from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.naver.com/'
response = urllib.request.urlopen(url)


soup = BeautifulSoup(response,'html.parser')
keywords = soup.find_all('span',class_='ah_k')
print("****")
print(type(keywords))
print("****")
#get_text() == 데이터에서 문자열만 추출
#strip() == 데이터의 양옆 공백제거
#[:20]의 이유? 인기검색어의 중복을 막고 20위까지만 출력하기 위함

keywords = [each_line.get_text().strip() for each_line in keywords[:20]]
print(keywords)