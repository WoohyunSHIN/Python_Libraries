#print('=============================여기까지 1세트===================')

# Word
'''
genres=[
    [0]드라마=drama,
    [1]판타지=fantasy,
    [2]서부=western,
    [3]공포=horror,
    [4]멜로/로맨스=romance,
    [5]모험=adventure,
    [6]스릴러=thriller,
    [7]느와르=noir,
    [8]컬트=cult,
    [9]다큐멘터리=documentary,
    [10]코미디=comedic,
    [11]가족=family,
    [12]미스터리=mystery,
    [13]전쟁=war,
    [14]애니메이션=animation,
    [15]범죄=crime,
    [16]뮤지컬=musical,
    [17]SF=SF,
    [18]액션=action,
    [19]무협=heroism,
    [20]에로=sexual,
    [21]서스펜스=suspense,
    [22]서사=epic,
    [23]블랙코미디=blackcomedic,
    [24]실험=experiment,
    [25]공연실황=reality
]
'''

# DB에 연결
conn=pymysql.connect(host='127.0.0.1',
    port=44449,
    user='root',
    password='1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

c = conn.cursor()

query_for_title_year = '''
CREATE TABLE if not exists title_year(
  `title` varchar(50) NOT NULL AUTO_INCREMENT,
  `sort_year` int(4) DEFAULT '0' COMMENT 'sort_year',
  PRIMARY KEY (`title`)
)ENGINE=InnoDB AUTO_INCREMENT=2760 DEFAULT CHARSET=utf8;
'''

# 여기 수정해야함.
query_for_title_genre='''
CREATE TABLE if not exists title_year(
  `title` varchar(50) NOT NULL AUTO_INCREMENT,
  `sort_year` int(4) DEFAULT '0' COMMENT 'sort_year',
  PRIMARY KEY (`title`)
)ENGINE=InnoDB AUTO_INCREMENT=2760 DEFAULT CHARSET=utf8;
'''

c.execute(query_for_title_year)