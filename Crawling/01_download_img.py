import urllib.request
import os

# css 는 select, 일반문법은 find
# dt.tit>a 는 직접적으로 있는 a태그

# urllib : https://docs.python.org/ko/3/library/urllib.html
# 1. 구글이미지에서 이미지 우클릭 후, 이미지 주소 복사또는 링크주소 복사하고 아래에 집어늫는다.
url = 'http://cdn.eyesmag.com/wp-content/uploads/2016/02/28223154/2019-parasite-film-by-bong-reasons-to-be-waiting-main.jpg'

# 2. 실행하는 파일의 경로를 찾아서 '같은 경로'에 이미지 저장
dirname=os.path.dirname(__file__)   # 디렉토리의 절대경로 찾기 
savename=dirname + '/test.jpg'      # 파일의 절대경로 만들기

# 3-1 || 3-2 중 하나만 하면 된다.
# 3-1. 파일로 저장
#urllib.request.urlretrieve(url,savename)

# 3-2. 파일을 열고.. 활용 할 수 있다.
men = urllib.request.urlopen(url).read()

# 3-2. 위에서 불러온 파일을 저장함 write()로.
with open(savename,mode='wb') as f:  # wr = write binaray = 동영상, 이미지
    f.write(men)
    print('저장되었습니다')
