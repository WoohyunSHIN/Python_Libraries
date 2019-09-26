from bs4 import BeautifulSoup

html='''
<html>
    <body>
    <div id="main-goods" role="page">
        <h1>과일과 야채</h1>
        <ul id="fr-list" class="items art it book">
            <li class="red green" data-lo="ko">사과</li>
            <li class="purple" data-lo="ko">포도</li>
            <li class="yello" data-lo="ko">레몬</li>
            <li class="yello" data-lo="ko">오렌지</li>
        </ul>
        <ul id="fr-list">
            <li class="red green" data-lo="ko">사과2</li>
            <li class="purple" data-lo="ko">포도2</li>
            <li class="yello" data-lo="ko">레몬2</li>
            <li class="yello" data-lo="ko">오렌지2</li>
        </ul>
        </div>
    </body>
</html>
'''

# CSS SELECTORS, 접근자 방식으로 선택하기 . 는 class, # 는 id
soup = BeautifulSoup(html, 'html.parser')
header = soup.select_one('body div h1')
list_items=soup.select('ul.items li')

print(header.string)
print(soup.select_one('ul').attrs)
for li in list_items:
    print(li.string)
print("*********")

# Ex) soup.select("p:nth-of-type(3)") --> 3번째 p태그 
list_items2=soup.select('li:nth-of-type(3)')
print(list_items2)

print("************************/n")

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
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# soup.select("body a") # body안에 있는 자손 a, 자녀 X
# soup.select("body > a") # body안에 있는 직손 자녀 a 만 찾는다 

soup.select("body a")
soup.select("html head title")

soup.select("head > title")
soup.select("p > a")
soup.select("p > a:nth-of-type(2)")
soup.select("p > #link1")  #id 가 link1 인것
soup.select("body > a") # 아무것도 없음 body안에 직접적인 자손 a 가 존재하지 않기 때문에