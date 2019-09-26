from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.cgv.co.kr/movies/'
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response,'html.parser')
results = soup.select('a strong.title')

print(results)

for result in results:
    print(result.string) # 또는 print(result.text)
