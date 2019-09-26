from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister sts" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,"html.parser")
# 첫번째 a 태그 안에 attribute class안에 2개의 값이들어가 있다. 리스트로 반환된다.
attr = soup.a['class']
print(attr)

# 새로운 <p>Back to the <a rel="index">homepage</a></p> 에서 
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
print(rel_soup.a['rel']) 
# ['index']

rel_soup.a['rel'] = ['index','contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents", >homepage</a></p>

# 객채가 navigableString ---> unicode 로 바꾸고 싶을때는 unicode()를 사용하면 된다.
test_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
print(test_soup.prettify())

# ancer tag 안에 string 은 homepage가 있다.
# 태그안에 string을 만들기,삭제, 수정 가능하다
tag = test_soup.a
print(tag.string)
print(type(tag.string))
tag.string.replace_with('홈페이지')
print(tag)

#***************************
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
</body>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# 리스트 형식이라 인덱스를 사용하여서 접근가능하고, contents를 이용하여 태그 안의 내용만 뺄수도 있다.
tag=soup.body
print(tag.contents)
print(len(tag.contents))

for child in tag.children:
    print(child)

print(len(list(tag.children)))
# 7
print(len(list(tag.descendants)))
# 20