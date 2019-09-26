import sqlite3

conn =sqlite3.connect('sqlite3/example.db')
c = conn.cursor()

# Never do this -- insecure!
# target = 'RHAT'
# c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % target)

# 관계형 데이터베이스에서, 1 row == 1 case(data) == 1 record 라고 말한다.
# WHERE 포함 이후의 부분은 조건절이다. 1 record 기준으로 뽑아낸다.  
# 데이터를 가져올땐 fecth()를 사용한다 한 행식 접근해서 쓰는 방법을 말한다.
items = c.fetchall()
for item in items:
    print(item)


# Do this instead
t = ('RHAT',)
# t1 = (100)
sql='SELECT * FROM stocks WHERE symbol=?'
c.execute(sql,t)   #c.execute(sql,(t,t1)) <- 여러개가 한 세트면 () 로 묶어서 넣어줘야한다.
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28','BUY','IBM',1000,45.00),
            ('2006-04-05','BUY','MSFT',1000,72.00),
            ('2006-04-06','SELL','IBM',500,53.00),]
c.executemany('INSERT INTO stocks VALUES(?,?,?,?,?)', purchases)
conn.commit()

# price 의 오름차순 순서로 데이터 들고오기
c.execute('SELECT * FROM stocks ORDER BY price')
rows = c.fetchall()
for row in rows:
    print(row)

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

c.close()