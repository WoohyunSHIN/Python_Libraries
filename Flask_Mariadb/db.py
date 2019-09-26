import pymysql

# 연결 함수
def conn_db():
    conn = pymysql.connect(host='localhost',
                    port=44449,
                    user='root',
                    password='1234',
                    db='test1',
                    charset='utf8mb4')
                    #cursorclass=pymysql.cursor.DictCursor)
    return conn

# Create table method
def create_table():
    conn=conn_db()
    cursor=conn.cursor()
    
    cursor.execute('''CREATE TABLE if not exists users(
        userid varchar(11) NOT NULL,
        email varchar(255) NOT NULL,
        address varchar(255),
        password varchar(255) NOT NULL,
        PRIMARY KEY (userid)
    )''')
    conn.commit()
    conn.close()

# Insert data method
def insert_users(user):
    conn=conn_db()
    cursor=conn.cursor()

    # 데이터 입력방법1
    # cursor.execute("INSERT INTO books VALUES('Java','2019-05-20','길벗',500,10)")

    # 데이터 입력방법2
    sql='INSERT INTO users VALUES(%s,%s,%s,%s)'
    # cursor.execute(sql,('Python','201001','한빛',584,20))

    # 데이터 입력방법3
    cursor.execute(sql,user)
    conn.commit()
    conn.close()
    
# print all data
def all_users():
    conn=conn_db()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM users')

    print('[1]전체 데이터 출력하기')
    users = cursor.fetchall()
    for user in users:
        for i in range(len(user)):
            print(user[i],end=" ")
        print()
    conn.close()
    return users
    


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
def update_users(user):
    conn = conn_db()
    cursor = conn.cursor()
    sql='''UPDATE users 
            SET email=%s,
                address=%s,
                password=%s
            WHERE userid=%s
        '''
    cursor.execute(sql,(user['email'],user['userAddress'],user['password'],user['userid']))
    conn.commit()
    conn.close()

# delete data
def delete_users(userid):
    conn = conn_db()
    cursor = conn.cursor()
    sql='''DELETE FROM users WHERE userid=%s '''
    cursor.execute(sql,userid)
    conn.commit()
    conn.close()

def one_user(userid):
    conn=conn_db()
    cursor=conn.cursor()
    sql='SELECT * FROM users WHERE userid=%s'
    cursor.execute(sql,userid)
    user=cursor.fetchone()
    conn.commit()
    conn.close()
    return user

