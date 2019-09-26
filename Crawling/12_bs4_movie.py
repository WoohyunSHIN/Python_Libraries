from bs4 import BeautifulSoup
import urllib.request, urllib.parse
import json
from collections import OrderedDict

params =urllib.parse.urlencode({'page':1})
url='https://movie.naver.com/movie/point/af/list.nhn?&%s' %params
print(url)

response = urllib.request.urlopen(url)
navigator=BeautifulSoup(response,'html.parser')
table=navigator.find('table', class_='list_netizen')
#print(table)

# 만들어진 내용을 전처리 할 것이다.
list_record=[]
for i,r in enumerate(table.find_all('tr')): # enumerate : 찾아서 index값이랑 값을 리턴해준다. i는 tr의 인덱스 값이다. r은 <tr> 안의 내용이다.
    for j,c in enumerate(r.find_all('td')): # 따라서 여기서 r.find_all 로 다시 접근한다.
        if j==0:
            record={'번호':int(c.text.strip())}
        elif j==2:
            record.update({'평점':int(c.text.strip())})
        elif j==3:
            record.update({'영화':str(c.find('a',class_='movie').text.strip())})
            record.update({'140자 평':str(c.text).split('\n')[2]}) # 140자 평의 시작 위치가 <br> 후에 3번째 부터 있기 때문에
        elif j==4:
            record.update({'글쓴이':c.find('a',class_='author').text.strip()})
            record.update({'날짜':str(c.text).split('****')[1]})
    try:
        list_record.append(record)
    except:
        pass



# list_record를 json 으로 저장하기 open 이지만 write 이기때문에 저장
with open('crawling/film_list.json','wt',encoding="utf-8") as make_file:
    json.dump(list_record,make_file, ensure_ascii=False, indent="\t")








#api = 'https://movie.naver.com/movie/point/af/list.nhn'
#values={
#    'target':'after',
#    'page':'1'    
#}
#params = urllib.parse.urlencode(values)
#url = api+'?'+params
#
#req = urllib.request.urlopen(url)
#soup = BeautifulSoup(req,'html.parser')
#
#infos = soup.select('tbody > tr')
#
#for movie_data in 10:
#
#for info in infos:
#    print(info)
#print(type(infos))
#print(len(infos))