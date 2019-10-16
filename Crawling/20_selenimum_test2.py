from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('selenium/data/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')
time.sleep(5)

id='sjwert'
pw='####'

# send_key 로 값을 밀어넣는다. 
# 보안상 send_key 해서 넣어서 들어가는 방법은 못하게 막아 놓았다.
#driver.find_element_by_name('id').send_keys(id)
#driver.find_element_by_name('pw').send_keys(pw)
#bt = driver.find.element_by_class_name('btn_global')
#bt.click()

driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
time.sleep(3)

# 로그인 해서 안에 데이터 값은 xpath를 이용한다
# xpath값을 알아내어서, 로그인 3단계를 넘어갈수있다.
# 1. 단계
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(1)
# 2. 단계 : 새로운 기기에서 로그인 되었습니다. 이부분을 또 xpath를 통해서 넘어가야한다.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[1]/a').click()
time.sleep(1)
# 3. 단계
driver.find_element_by_xpath('//*[@id="login_maintain"]/span[1]').click()
time.sleep(1)

