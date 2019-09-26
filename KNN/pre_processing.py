import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load Data
df_data_2000 = pd.read_csv('/Users/Shinwoohyun/Desktop/Web_Server/film_Data/film_2000.csv',index_col=None)

# 이름이 같은 영화들 데이터 합쳐 버리기
df_data_2000_suc=df_data_2000.groupby('title').sum()

# title을 인덱스에서 꺼내기 
# [a,b,c] --> [a,b,c,title]
df_data_2000_suc['title']=df_data_2000_suc.index

#columns = ['a','b','c','title']
columns=list(df_data_2000_suc.columns)

# [분류범주]
# title들을 리스트로 만들기
# title_list = ['영화이름','영화이름','영화이름','영화이름','영화이름',...]
title_list =[]
title_list=list(df_data_2000_suc['title'])

# [분류집단]
df_data_2000_suc= df_data_2000_suc.iloc[:,0:25]  # usage = 0 : 25 = 왜냐하면 0부터 25번째 컬럼까지 0||1 의 데이터가 들어있기 때문에
# From DataFrame to NumpyArray
np_df_data_2000_suc=df_data_2000_suc.to_numpy()
print(np_df_data_2000_suc)

# [분류대상] for cinemas

# <테스트용>
target = [0,1,0,0,1,
        0,0,0,0,0,
        1,0,0,0,0,
        0,0,0,0,0,
        0,0,0,0,0]

genres = {'drama':0,'fantasy':0,'western':0,'horror':0,'romance':0,'adventure':0,'thriller':0,'noir':0,'cult':0,'documentary':0,'comedic':0,
'family':0,'mystery':0,'war':0,'animation':0,'crime':0,'musical':0,'SF':0,'action':0,'heroism':0,'sexual':0,'suspense':0,
'epic':0,'blackcomedic':0,'experiment':0}

# '''
# genres=[
#     [0]드라마=drama,
#     [1]판타지=fantasy,
#     [2]서부=western,
#     [3]공포=horror,
#     [4]멜로/로맨스=romance,
#     [5]모험=adventure,
#     [6]스릴러=thriller,
#     [7]느와르=noir,
#     [8]컬트=cult,
#     [9]다큐멘터리=documentary,
#     [10]코미디=comedic,
#     [11]가족=family,
#     [12]미스터리=mystery,
#     [13]전쟁=war,
#     [14]애니메이션=animation,
#     [15]범죄=crime,
#     [16]뮤지컬=musical,
#     [17]SF=SF,
#     [18]액션=action,
#     [19]무협=heroism,
#     [20]에로=sexual,
#     [21]서스펜스=suspense,
#     [22]서사=epic,
#     [23]블랙코미디=blackcomedic,
#     [24]실험=experiment,
#  
# ]
# '''

#target = [1,1,1]

# KNN 시작
def data_set():
    # 분류집단
    dataset = np.array(np_df_data_2000_suc) 
    size = len(dataset)

    # 분류대상
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.tile.html
    class_target = np.tile(target,(size,1))
    
    # 분류범주
    class_category = np.array(title_list)

    return dataset, class_target, class_category

# dataset 생성
dataset, class_target, class_category = data_set()

def classify(dataset, class_target, class_category, k):
    # 유클리드 거리 계산
    diffMat = class_target - dataset    # 두 점의 차
    sqDiffMat = diffMat**2              # 차에 대한 제곱
    row_sum = sqDiffMat.sum(axis=1)     # 차에 대한 제급에 대한 합
    distance = np.sqrt(row_sum)         # 차에 대한 제곱에 대한 합의 제곱근(최종거리)

    # 가까운 거리 오름차순 정렬
    sortDist = distance.argsort()

    # 이웃한 k개 선정
    class_result={}
    for i in range(k):
        c = class_category[sortDist[i]]
        class_result[c] = class_result.get(c,0) + 1
    
    return class_result

# 함수 호출 = 시작포인트
# 이웃한 3개를 찾으면 C,A,B 가 나와야한다 <--성공
k = 5
class_result = classify(dataset, class_target, class_category, k)
# print(class_result) # 확인 코드

# 분류결과 출력 함수 정의
def classify_result(class_result):
    for title in title_list:
        for recommand in class_result.keys():
            if recommand == title:
                print(title+'을 추천합니다')
            else:
                pass
print('-----------')
classify_result(class_result)  # 얘가 출력한다.
print('-----------')

z,x,c = data_set()
classify_result(classify(z,x,c,5))
print('-----------')

def trans_data(set_data):
    ####### test part#############
    # set_data = ['horor','comedic']
    for i in set_data:
        for j in genres.keys():
            if i==j:
                genres[j] += 1
            else:
                pass
        # 전역변수인 target에 데이터 넣기
        global target
        target = list(genres.values()) 