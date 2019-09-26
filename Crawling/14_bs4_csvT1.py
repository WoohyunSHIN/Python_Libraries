# investing.com은 http 로 막아놔서 Error 403 이 뜬다.
import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.investing.com/equities/tesla-motors-historical-data'
req = urlopen(url)
soup = BeautifulSoup(req,'html.parser')

table = soup.find_all('table',{'class':'genTbl closedTbl historicalTbl'})
rows = table.find_all('tr')

csvFile=open('crawling/Tesla.csv','wt', newline='', encoding='utf-8')

write = csv.writer(csvFile)
try:
    for row in rows:
        csvRow=[]
        for data in row.find_all('td'):
            csvRow.append(data.get_text())
        write.writerow(csvRow)
finally:
    print('데이터 저장 성공')
    csv.close()