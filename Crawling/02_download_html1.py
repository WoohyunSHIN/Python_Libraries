import urllib.request

url='https://www.google.com/'

men=urllib.request.urlopen(url).read() # 주소값으로 페이지를 열어가지고 읽는다. 
print(men)
print(men.decode('utf-8'))

