from bs4 import BeautifulSoup
from selenium import webdriver
import time

# chromedriver 위치를 잡아서 driver 객체에 담아주자
driver = webdriver.Chrome('selenium/data/chromedriver')
driver.get("https://www.istarbucks.co.kr/store/store_map.do")
time.sleep(10) #주소안에 데이터를 들고오는데 시간이 걸리기 때문에 타임을 걸지 않으면 아래의 처리가 빠르기 때문에 슬립을 걸어놓아야한다.

loca = driver.find_element_by_class_name('loca_search') # 찾은 위치만 loca 안에 넣어놓는다.
loca.click() # loca 안에 <a> 태그가 존재하기 때문에 해당 영역이 클릭이 된다.
time.sleep(10)

# li 에는 지역별로 나누어 져있는데 6번째[5]가 부산이니까  
sido = driver.find_element_by_class_name('sido_arae_box') #ul값 받아오기
li = sido.find_elements_by_tag_name('li') # 여러개(=elements)의 li값 받아오기
li[5].click()
time.sleep(10)

# 해운대구는 부산에서 ul 안에 
gugun = driver.find_element_by_class_name('gugun_area_box')
li = sido.find_elements_by_tag_name('li')
li[15].click() # 부산에 해운대구가 16번째 있다. 
time.sleep(10)

# 해운대구 까지 온 후 소스를 가져온다.
source=driver.page_source
bs=BeautifulSoup(source,'lxml')
entire=bs.find('ul',class_='quickSearchResultBoxSidoGugun')