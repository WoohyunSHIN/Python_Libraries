from bs4 import BeautifulSoup
import urllib.request

url = 'https://music.bugs.co.kr/chart'
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response,'html.parser')
results = soup.select('th>p.title > a')

print(results)
print('______')

for result in results:
    print(result.string)