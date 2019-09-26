from bs4 import BeautifulSoup
import urllib.request

url = ('https://finance.naver.com/marketindex/')
response = urllib.request.urlopen(url)

soup=BeautifulSoup(response,'html.parser')

print(type(soup))
results = soup.select('span.value')
for result in results:
    print(result.string)

print('원달러환율:',results[0].string)




