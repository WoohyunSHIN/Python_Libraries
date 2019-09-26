import pymysql

# db= test 일수도 있고
# cursorclass=pymysql.cursors.DictCursor 을 통해서 list 형식이 아니라 Dictionary 값으로 접근 할 수있다.
# port번호는 따로 지정해 주어야 한다.
conn = pymysql.connect(host = 'localhost',
                                port=44449,
                                user='root',
                                password='1234',
                                db='test1', 
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

c = conn.cursor()

#c.execute("CREATE DATABASE test")
#c.commit()
#c.execute("use test")

# Create table 
# 자료형 이상한거 같은데 이거 바꿔야할 나중에 꼭 찾아봐라 귀찮으니까 지금 링크 걸어둔다
# https://blog.naver.com/PostView.nhn?blogId=jevida&logNo=220340062504
c.execute('''CREATE TABLE if not exists stocks(
        date text,
        trans text,
        symbol text,
        qty real,
        price real)''')

c.execute("INSERT INTO stocks VALUES('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
conn.close()
