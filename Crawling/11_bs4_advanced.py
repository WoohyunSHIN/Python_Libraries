from bs4 import BeautifulSoup
import urllib.request

url = 'https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y'
req = urllib.request.urlopen(url)

soup = BeautifulSoup(req,'html.parser')

url_list1 = []
for raw_url1 in soup.find_all('a', class_='nclicks(fls.list)'):
    url_list1.append(raw_url1.get('href')) 
    
for raw_url2 in soup.find_all('a', class_='nclicks(cnt_flashart)'):
    url_list1.append(raw_url2.get('href'))

print(url_list1)
print(len(url_list1))
print(type(url_list1))

# results = soup.select('.section_list_ranking li a')  --> 강사님
# section_list_ranking 클래스 안에있는 li 태그 안에 a 태그를 results 에 넣는다.

for url_connect in url_list1:
    print()
    req_connect = urllib.request.urlopen(url_connect)
    soup_content = BeautifulSoup(req_connect,'html.parser')
    result = soup_content.select_one('#articleBodyContents')

    #가공작업
    output =''
    for item in result.contents:
        stripped = str(item).strip() # 공백제거
        if stripped=='':
            continue
        if stripped[0] not in['<','/']: # 태그나 주석제거
            output+=str(item).strip()
    ouput = output.replace('무단 전재 및 재배포 금지','')
    ouput = output.replace('본문 내용TV플레이어','')
    print(output)
    print()

#    time.sleep(3)
