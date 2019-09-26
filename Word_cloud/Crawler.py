from bs4 import BeautifulSoup
import urllib.request, urllib.parse
from selenium import webdriver
import time
import os
import sys

def crawling_words():

    list_record=[]

    for i in range(0,201,20): #(1, xxx, 20) : 1부터 xxx 까지 20 씩 , 21
        
        params = urllib.parse.urlencode({'iStartCount':i})
        url = 'http://www.riss.kr/search/Search.do?detailSearch=false&viewYn=OP&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&queryText=&strQuery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&'+params+'&iGroupView=5&icate=re_a_kor&colName=re_a_kor&exQuery=&pageScale=20&strSort=RANK&order=%2FDESC&onHanja=false&keywordOption=0&searchGubun=true&p_year1=&p_year2=&dorg_storage=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&language_code=&ccl_code=&language=&inside_outside=&fric_yn=&image_yn=&regnm=&gubun=&kdc=&resultSearch=false&listFlag=&h_groupByField=&orderBy='
        req = urllib.request.urlopen(url)
        navigator = BeautifulSoup(req,'html.parser')
        pre = navigator.select('li>div>p>a')

        for j in range(20):
            pre_one = pre[j]
            record = {'title':str(pre_one.text.strip())}
            list_record.append(record)

    return list_record

def API_naver():
    client_id = "YaQRzr82eP4_dg9AYU2a"
    client_secret = "MBEunHKyeU"
    encText = urllib.parse.quote("미세먼지") # 내가 검색하기 원하는 단어를 집어넣으면 된다.
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과 : 블로그쪽에다 질의를 하는 것이다.
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

    # 요청하는 데이터의 헤더에 id&pw 를 붙여서 날린다.
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    # reponse로 값을 받아온다.
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    # 에러코드 200은 성공이라는 뜻이다.
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)


## 하.............못하겠다
def crawling_words1():

    list_record=[]
    list_content=[]

    for i in range(0,21,20): #(1, xxx, 20) : 1부터 xxx 까지 20 씩 , 21
        
        params = urllib.parse.urlencode({'iStartCount':i})
        url = 'http://www.riss.kr/search/Search.do?detailSearch=false&viewYn=OP&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&queryText=&strQuery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&'+params+'&iGroupView=5&icate=re_a_kor&colName=re_a_kor&exQuery=&pageScale=20&strSort=RANK&order=%2FDESC&onHanja=false&keywordOption=0&searchGubun=true&p_year1=&p_year2=&dorg_storage=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&language_code=&ccl_code=&language=&inside_outside=&fric_yn=&image_yn=&regnm=&gubun=&kdc=&resultSearch=false&listFlag=&h_groupByField=&orderBy='
        req = urllib.request.urlopen(url)
        navigator = BeautifulSoup(req,'html.parser')
        pre = navigator.select('li>div>p>a')

        links=[]
        # li>div>p에 anger 태그 값
        for j in range(20):
            link=pre[j].get('href')
            link='http://www.riss.kr'+link
            links.append(link)

        # ul태그 id = abs2 그후 li[1] == 2번째꺼 들고 오면 되겠다.
        for link in links:
        #    driver = webdriver.Chrome('selenium/data/chromedriver')
        #    driver.get(link)
        #    time.sleep(5)
        #    contents = driver.find_element_by_id('abs2')
        #    li = contents.find_elements_by_tag_name('li')
        #    print(li)
        #    li = li[1]
        #    content = {'naeyoung':str(li.text.strip())}     
        #    print(content)
        #    print('******')
            request=urllib.request.urlopen(link)   
            soup = BeautifulSoup(request,'html.parser')
            print(soup)
            print('*************')
            contents = soup.select("ul > #abs2")
            print(contents)
            print(type(contents))
            content = {'naeyoung':str(contents.text.strip())}
            list_content.append(content)

    return list_content

API_naver()