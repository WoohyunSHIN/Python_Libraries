#웹페이지를 분석하여 CSV로 저장하기
# <table> 내부의 텍스트 저장
# 더 자세히 알고 싶으면 csv API 찾아보기
# https://docs.python.org/3/library/csv.html

from bs4 import BeautifulSoup
import urllib.request
import csv

url = 'https://en.wikipedia.org/wiki/Comparison_of_text_editors'
urlopen = urllib.request.urlopen(url)
soup = BeautifulSoup(urlopen,'html.parser')

# class가 wikitable인 태그들 중에서 첫번째 태그 서냍ㄱ
table=soup.find_all('table',{'class':'wikitable'})[0]
rows = table.find_all('tr')

# wt : 텍스트 쓰기 모드
csvFile=open('crawling/editors.csv','wt',newline='',encoding='utf-8')

# csv 파일 저장 객체
write=csv.writer(csvFile)
try: 
    for row in rows:
        csvRow=[]
        # td, th 태그의 내용을 리스트에 추가
        for cell in row.find_all(['td','th']):
            csvRow.append(cell.get_text())
        write.writerow(csvRow)
finally:
    print('csv로 저장되었습니다.')
    csvFile.close()
