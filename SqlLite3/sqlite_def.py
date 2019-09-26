import sqlite3

# 테이블 생성 함수
def create_table():
    conn = sqlite3.connect('sqlite3/my_books.db')
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE if not exists books(
        title text,
        published_date text,
        publisher text,
        page integer,
        recommend integer
    )''')
    conn.commit()
    conn.close()

# 테이블 생성 함수 호출
# create_table()

# 데이터 입력 함수
def insert_books(items):
    conn = sqlite3.connect('sqlite3/my_books.db')
    cursor = conn.cursor()
    
    # case 1
    #cursor.execute("INSERT INTO books VALUES('Java','2019-05-20','길벗',500,10)")

    # case 2
    sql = 'INSERT INTO books VALUES(?,?,?,?,?)'
    #cursor.execute(sql,('Python','201001','한빛',584,20))

    # case 3
    cursor.executemany(sql,items)
    conn.commit()
    conn.close()

# 데이터 입력 함수 호출
# insert_books()
 
# 전체 데이터 출력 함수
def all_books():
    conn=sqlite3.connect('sqlite3/my_books.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM books")
    print('[1] 전체 데이터 출력하기')
    books=cursor.fetchall()
    print(type(books)) # 타입 출력
    print(len(books)) # 레코드 개수 출력

    for book in books:
        for i in book:
            print(i,end=" ")
        print()
    conn.close()

# 전체 데이터 출력 함수 호출
# all_books()
