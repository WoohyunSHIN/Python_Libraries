import sqlite_def as db 
# 이름이 기니까 db 라는 이름으로 쓰겠다.
# 여기서는 함수를 따로 처리 해놓고 import 해서

db.create_table()

items=[
        ('빅데이터','2014-07-02','삼성',296,11),
        ('안드로이드','2010-02-02','삼성',526,20),
        ('Spring','2013-12-02','삼성',248,15),
    ]
db.insert_books(items)
db.all_books()
