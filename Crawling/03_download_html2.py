import urllib.request
import urllib.parse

# 네이버 통합검색에서 검색어 '초콜릿'을 넣고 주소를 보면 search.naver 쪽으로 간다. query= 이후에 이상하게 %로 있는것은 초콜릿을 뜻한다.
# https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%B4%88%EC%BD%9C%EB%A6%BF

# ? 물음표를 기준으로 api 를 만든다
api = 'https://search.naver.com/search.naver'
values={
    'sm':'top__hty',
    'fbm':'1',
    'ie':'utf8',
    'query':'초콜릿'
}

# 한국어로 적으면 query 부분이 이상하게 %로 보인다 따라서 urllib.parse를 사용하면 딕셔너리 values 를 쿼리로 바꿔주는 역활을 한다.
params = urllib.parse.urlencode(values)
url=api+'?'+params
data=urllib.request.urlopen(url).read()
text=data.decode('utf-8')
print(text)

# 네이버 뉴스에서 검색을 '장마' 라고 하면 위에와 다른 방식으로 query가 생긴다.
# https://search.naver.com/search.naver?query=%EC%9E%A5%EB%A7%88&where=news&ie=utf8&sm=nws_hty

values_news={
    'query' : '장마',
    'where' : 'news',
    'ie' : 'utf8',
    'sm' : 'nws_hty'
}

params_news = urllib.parse.urlencode(values_news)
url_news=api+'?'+params_news
data_news=urllib.request.urlopen(url_news).read()
text_news=data_news.decode('utf-8')
print(text_news)