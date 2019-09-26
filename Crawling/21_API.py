# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
client_id = "YaQRzr82eP4_dg9AYU2a"
client_secret = "MBEunHKyeU"
encText = urllib.parse.quote("다나스") # 내가 검색하기 원하는 단어를 집어넣으면 된다.
url = "https://openapi.naver.com/v1/search/news?query=" + encText # json 결과 : 블로그쪽에다 질의를 하는 것이다.
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

# 요청하는 데이터의 헤더에 id&pw 를 붙여서 날린다.
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

# reponse로 값을 받아온다.
response = urllib.request.urlopen(request)
rescode = response.getcode()
# 에러코드 200은 성공이라는 뜻이다.
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)