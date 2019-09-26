import pymysql

# 연결 함수
def conn_db():
    conn = pymysql.connect(host='localhost',
                    port=44449,
                    user='root',
                    password='1234',
                    db='test1',
                    charset='utf8mb4')
    return conn

# Create table method
def create_table():
    conn=conn_db()
    cursor=conn.cursor()
    
    cursor.execute('''CREATE TABLE if not exists cines(
        num int,
        score int,
        title varchar(255),
        opinion varchar(300),
        author varchar(30),
        date varchar(20)
    )''')
    conn.commit()
    conn.close()

# Insert data method
def insert_cines(items):
    items= items.replace("'","''")
    items=items.replace('"','\"')

    conn=conn_db()
    cursor=conn.cursor()

    sql='INSERT INTO cines VALUES(%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql,items)
    conn.commit()
    conn.close()
    
# print all data
def all_cines():
    conn=conn_db()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM cines')

    print('[1]전체 데이터 출력하기')
    cines = cursor.fetchall()
    print(type(cines))
    print(len(cines)) # 레코드 갯수 출력
    print(cines)

    for cine in cines:
        for i in cine:
            print(cine[i],end=" ")
        print()
    conn.close()

# print selected record
# 갯수를 받아서 뽑아낸다
def some_books(number):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books=cursor.fetchall(number)

    for book in books:
        for i in book:
            print(book[i], end=" ")
        print()
    conn.close()

# modify data method
def update_books():
    conn = conn_db()
    cursor = conn.cursor()
    # title 이 java인 recommend를 200으로 수정하겠다!
    sql='''UPDATE books SET RECOMMEND=%s WHERE title=%s'''
    cursor.execute(sql,(200,'Java'))
    conn.commit()
    conn.close()

# delete data
def delete_books():
    conn = conn_db()
    cursor = conn.cursor()
    #publisher가 한빛인 데이터를 삭제
    sql='''DELETE FROM books WHERE publisher='한빛' '''
    cursor.execute(sql)
    conn.commit()
    conn.close()
