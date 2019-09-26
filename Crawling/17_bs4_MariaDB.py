# Maria DB 사용하는 방법
# 아몰랑 개념은 맞는데 안된다~!!!!!!!!~!~!~!~!
from bs4 import BeautifulSoup
import urllib.request, urllib.parse
import pymysql
import db

params =urllib.parse.urlencode({'page':1})
url='https://movie.naver.com/movie/point/af/list.nhn?&%s' %params
print(url)

response = urllib.request.urlopen(url)
navigator=BeautifulSoup(response,'html.parser')
table=navigator.find('table', class_='list_netizen')

list_records=[]


for i,r in enumerate(table.find_all('tr')): 
    for j,c in enumerate(r.find_all('td')): 
        if j==0:
            record=int(c.text.strip())
        elif j==2:
            record1=int(c.text.strip())
        elif j==3:
            record2=str(c.find('a',class_='movie').text.strip())
            record3=str(c.text).split('\n')[2] # 만약 글자가 '140자 평' 과 같이 띄어쓰기가 있으면 위의 fieldnames 와 다르기 때문에 안된다. 
        elif j==4:
            record4=str(c.find('a',class_='author').text.strip())
            record5=str(c.text).split('****')[1]
    try:
        record_t=tuple([record,record1,record2,record3,record4,record5])
        list_records.append(record_t)
    except:
        pass
print(list_records)

conn = db.conn_db()
db.create_table()
db.insert_cines(list_records)
db.all_cines()

