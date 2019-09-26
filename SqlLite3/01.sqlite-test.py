import sqlite3

# [sql 순서]
# 1. 커낵션
# 2. 커서를 받아내고
# 3. Query 문을 execute 로 보내고
# 4. 데이터를 뽑아낼려면 fetch()를 사용하고 아니면 commit()으로 저장하고

# SQLite3 모듈 자체 버전 --> 2.6.0 버전
print(sqlite3.version)

# Mongo DB 는 관계형이 아닌 Database 이고, 요즘 모든 DB 들은 거의다 관계형 DB이다. 
# 파일 한개로 끝나기 때문에 {포트번호, 유저아이디, 비밀번호} 신경안 써도 된다.
conn = sqlite3.connect('sqlite3/example.db')
c = conn.cursor()

# 관계형 데이터 베이스의 기본 저장단위는 Table이다.
# Create table
# CREATE TABLE [조건] [table명](...)
c.execute('''
            CREATE TABLE if not exists stocks(
                data text, 
                trans text, 
                symbol text, 
                qty real, 
                price real
            ) 
            ''')

# Insert a row of data 
# INSERT INTO [table명] VALUES(...)
# SQL문은 문자열을 나타낼때 ' 작은 따옴표를 쓰기 때문에 밖에는 " 큰 따옴표를 사용해야한다.
c.execute('''
            INSERT INTO stocks(data, trans, symbol, qty, price)
                VALUES('2006-01-05','BUY','RHAT',100,35.14)''')

c.execute('''
            INSERT INTO stocks(data, trans, symbol, qty, price)
                VALUES('2006-01-05','BUY','aaaa',100,35.14)''')                

c.execute('''
            INSERT INTO stocks(data, trans, symbol, qty, price)
                VALUES('2006-01-05','BUY','shin',100,35.14)''')
# Save(commit) the changes
conn.commit()
conn.close()

