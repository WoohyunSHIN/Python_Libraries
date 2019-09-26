#https://movie.naver.com/movie/sdb/browsing/bmovie_open.nhn <-- 크롤링
#http://blog.naver.com/PostView.nhn?blogId=nonamed0000&logNo=220976767692&parentCategoryNo=&categoryNo=24&viewDate=&isShowPopularPosts=true&from=search <-- knn


# https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?genre=21&year=2000&page=1
# <genre는 1번 부터 25번까지>
# <year는 2000년 부터 2019년 까지 데이터>
# <page는 1번 부터 마지막 페이지 까지>
# 일단 1번 장르에 2000년 page 1번 데이터를 끌어오는 것 부터 시작해 보자.

from bs4 import BeautifulSoup
import pymysql
import urllib.request
import csv

films=[['title','drama','fantasy','western','horror','romance','adventure','thriller','noir','cult','documentary','comedic',
        'family','mystery','war','animation','crime','musical','SF','action','heroism','sexual','suspense',
        'epic','blackcomedic','experiment']]

# 2000년 데이터
for genre in range(1,26): # 1부터 25번 장르까지 
    for page in range(1,81): # 1부터 100페이지 까지
        
        url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?genre='+str(genre)+'&year=2019&page='+str(page)+''
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response,'html.parser')

        list_items = soup.select('ul.directory_list > li')

        # select film's genre
        genres = {'drama':0,'fantasy':0,'western':0,'horror':0,'romance':0,'adventure':0,'thriller':0,'noir':0,'cult':0,'documentary':0,'comedic':0,
        'family':0,'mystery':0,'war':0,'animation':0,'crime':0,'musical':0,'SF':0,'action':0,'heroism':0,'sexual':0,'suspense':0,
        'epic':0,'blackcomedic':0,'experiment':0}

        if genre==1:
            genres['drama']=1
        elif genre==2:
            genres['fantasy']=1
        elif genre==3:
            genres['western']=1
        elif genre==4:
            genres['horror']=1
        elif genre==5:
            genres['romance']=1
        elif genre==6:
            genres['adventure']=1
        elif genre==7:
            genres['thriller']=1
        elif genre==8:
            genres['noir']=1
        elif genre==9:
            genres['cult']=1
        elif genre==10:
            genres['documentary']=1
        elif genre==11:
            genres['comedic']=1
        elif genre==12:
            genres['family']=1
        elif genre==13:
            genres['mystery']=1
        elif genre==14:
            genres['war']=1
        elif genre==15:
            genres['animation']=1
        elif genre==16:
            genres['crime']=1
        elif genre==17:
            genres['musical']=1
        elif genre==18:
            genres['SF']=1
        elif genre==19:
            genres['action']=1
        elif genre==20:
            genres['heroism']=1
        elif genre==21:
            genres['sexual']=1
        elif genre==22:
            genres['suspense']=1
        elif genre==23:
            genres['epic']=1
        elif genre==24:
            genres['blackcomedic']=1
        elif genre==25:
            genres['experiment']=1
        else:
            pass

        # values 값만 dic_list 형식으로 뽑아내기
        genres = genres.values()

        # title Crawling --> List 또는 Dict 에 넣어야함
        for li in list_items:
            sub_title = li.select('a')
            title=sub_title[0]
            # table = [(영화타이틀),({드라마:0},{판타지:0},{서부:0},{공포:0},{멜로/로멘스:0},{모험:0},{스릴러:0},...),(영화년도)]
            dataset = [title.string]

            # for문을 돌면서 dic_list --> list 만들기
            for i in genres:
                dataset.append(i)
            films.append(dataset)

# csv 파일로 저장하기 
csvfile = open("/Users/Shinwoohyun/Desktop/Web_Server/film_Data/film_2019.csv","w",newline="\n")
csvwriter = csv.writer(csvfile)
for row in films:
    csvwriter.writerow(row)
csvfile.close()




