# ajax[비동기 방식] 를 이해하고 있으면 된다.  틀은 놓아두고 데이터 값만 왔다 갔다 하는거
# 우리가 bs4 방식으로 했던 것은 데이터 안가져와짐 왜냐하면 우리가 받은 정보는
# 데이터 값이 내려오기 전이기 때문이다.

# 셀레니움 말고도 팬티움이라던지 다른 것이 있다.
# 방식은, 틀 + 데이터로 가상 웹페이지를 만들고 가상 웹페이지에서 데이터를 끍어오는 형태이다.
 
from bs4 import BeautifulSoup
import requests
# import requests = urllib 이랑 비슷한 역활을 한다.

starbugs = requests.get('https://www.istarbucks.co.kr/store/store_map.do')
# 가져온거 '.' text 해서 가져오면 되고 html.paser --> lxml 
st_bs=BeautifulSoup(starbugs.text,'lxml')
print(st_bs.select('li.quickResultLstCom'))



