# csv 파일로 저장하는 방법
from bs4 import BeautifulSoup
import urllib.request, urllib.parse
import csv
import re

params =urllib.parse.urlencode({'page':1})
url='https://movie.naver.com/movie/point/af/list.nhn?&%s' %params
print(url)

response = urllib.request.urlopen(url)
navigator=BeautifulSoup(response,'html.parser')
table=navigator.find('table', class_='list_netizen')

list_records=[]

with open('crawling/names.csv','w', newline='',encoding='utf-8') as csvfile: 
    fieldnames =['번호','평점','영화','140자평','글쓴이','날짜']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
    writer.writeheader()
    for i,r in enumerate(table.find_all('tr')): 
        for j,c in enumerate(r.find_all('td')): 
            if j==0:
                record={'번호':int(c.text.strip())}
            elif j==2:
                record.update({'평점':int(c.text.strip())})
            elif j==3:
                record.update({'영화':str(c.find('a',class_='movie').text.strip())})
                record.update({'140자평':str(c.text).split('\n')[2]}) # 만약 글자가 '140자 평' 과 같이 띄어쓰기가 있으면 위의 fieldnames 와 다르기 때문에 안된다. 
            elif j==4:
                record.update({'글쓴이':c.find('a',class_='author').text.strip()})
                record.update({'날짜':str(c.text).split('****')[1]})
        try:
            list_records.append(record)
            writer.writerow(record)
        except:
            pass