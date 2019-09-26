import pymysql

# 연결 함수
def conn_db():
    conn = pymysql.connect(host='localhost',
                    port=44449,
                    user='root',
                    password='1234',
                    db='test1',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursor.DictCursor)
    return conn


# 자료형 이상한거 같은데 이거 바꿔야할 나중에 꼭 찾아봐라 귀찮으니까 지금 링크 걸어둔다
# https://blog.naver.com/PostView.nhn?blogId=jevida&logNo=220340062504
# Create table method
def create_table():
    conn=conn_db()
    cursor=conn.cursor()
    
    cursor.execute('''CREATE TABLE if not exists books(
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer,
    )''')
    conn.commit()
    conn.close()

# Insert data method
def insert_books():
    conn=conn_db()
    cursor=conn.cursor()

    # 데이터 입력방법1
    cursor.execute("INSERT INTO books VALUES('Java','2019-05-20','길벗',500,10)")

    # 데이터 입력방법2
    sql='INSERT INTO books VALUES(%s,%s,%s,%s,%s)'
    cursor.execute(sql,('Python','201001','한빛',584,20))

    # 데이터 입력방법3
    items=[
        ('빅데이터','2014-07-02','삼성',296,11),
        ('안드로이드','2010-02-02','삼성',526,20),
        ('Spring','2013-12-02','삼성',248,15)
    ]
    cursor.executemany(sql,items)
    conn.commit()
    conn.close()
    
# print all data
def all_books():
    conn=conn_db()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM books')

    print('[1]전체 데이터 출력하기')
    books = cursor.fetchall()
    print(type(books))
    print(len(books)) # 레코드 갯수 출력
    print(books)

    for book in books:
        for i in book:
            print(book[i],end=" ")
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


