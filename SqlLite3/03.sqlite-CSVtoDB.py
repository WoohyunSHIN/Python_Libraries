import csv, sqlite3

# 이 파일에서는 input.csv 에 있는 데이터를 suppliers.db에 저장하는 것이다.

# input_file 이란 객체 안에 data.csv 파일의 주소값을 미리 넣어놓는다.
input_file = 'sqlite3/input.csv'

# Table 자체를 날려버리는 구문을 sql_delete 객체에 넣어놓는다.
sql_delete='DELETE FROM suppliers'

conn=sqlite3.connect('sqlite3/suppliers.db')
cursor = conn.cursor()
sql='''
    CREATE TABLE if not exists suppliers(
        supplier_name text(20),
        invoice_number text(20),
        part_number text(20),
        cost real,
        purchase_date date
    )'''
cursor.execute(sql)

# csv 파일에서 데이터를 읽어서 테이블에 insert
# 해당파일을 읽기전용으로 열고 인코딩을 utf-8 이고 구분자는 ; 로 하겠다.
file_reader = csv.reader(open(input_file,'r',encoding='utf-8'),delimiter=';')

# 첫 라인을 읽음(제목행)
# next() 함수는 한 줄을 읽고 삭제해 버리는 함수이다.
header=next(file_reader,None)
print('header',header)
print(len(header))

# header 이후 2번째 행부터 끝까지 읽어 들이며 insert
for row in file_reader:
    data=[]
    # len(header) = 5,5개의 필드갯수, range(5)
    for idx in range(len(header)):
        data.append(row[idx])
    cursor.execute('INSERT INTO suppliers VALUES(?,?,?,?,?)', data)
conn.commit()

