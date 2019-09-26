from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'html.parser') # BeatifulSoup([문서],[어떤문서로만들어졌는지])
# html.parser 는 html이 어떻게 생겼는지에 대한 정의가 내려져 있다. 
# 보통 default 값으로 html이 파서로 잡혀 있는데 xml 같은 경우 xml.parser 로 해줘야한다.

# 1. prettify() 라는 함수를 쓰면 읽기 편하게 나온다. 
print(soup.prettify()) 

# 2. title 태그만 리턴해준다. 
print(soup.title)
# <title>The Dormouse's story</title>

print(soup.title.name)
# title

print(soup.title.string)
# The Dormouse's story

# title태그의 부모태그의 이름 
print(soup.title.parent.name)
# head

# 처음오는 p 태그 1개
print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>


print(soup.p['class'])

print(soup.a)

print(soup.find_all('a'))

print(soup.find(id="link3"))

#*********************************************************************
for link in soup.find_all('a'):
    print(type(link))
    print(link.get('href'))

a =soup.get_text()
print(a)
print(type(a))

# 이렇게 하면 첫번째 a태그가 blockquote태그로 바뀌꼈다.
tag = soup.a
print(type(tag))
print(tag.name)
tag.name="blockquote"
print(tag.name)

# 현재 tag 에 soup.a 가 들어 있었고 soup.blockquote 로 바뀌었다.
#사용방법 : 네이버 뉴스 홈에 가면 여러가지 글이 있는데 모든 글이 링크가 걸려잇다면, 
#그것을 타고 들아가서 안에 있는 값을 들고오는 것을 해볼 수 있다.
print(tag['id'])
print(tag.attrs)  # 딕셔너리 형태로 값이 나온다.

tag['id'] = 'verybold' # attribute 수정
tag['another-attribute'] = 1 # attribute 추가
print(tag)
# <blockquote .... id = 'verybold', another-attribute = '1'>

# attribute 삭제
del tag['id']
del tag['another-attribute']

print(tag['id']) # 없기때문에 KeyError 뜸
print(tag.get('id')) # id의 key에 맞는 value 가 None으로 뜸