# 신경망이 훈련데이터를 얼마나 잘 처리 했느냐를 표현하는 지표로 '손실 함수' 라는 것을 사용한다
# 대표적인 손실함수로써 MSE(= 평균 제곱 오차) 와 CEE(= 교차 엔트로피 오차)를 많이사용한다.
import numpy as np

def MSE(y,t):
    return 0.5*np.sum((y-t)**2)

y = [0.1,0.05,0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]  # softmax 출력으로 얻은 확률
t = [0,0,1,0,0,0,0,0,0,0] # one_hot_encoding 레이블 값이 일치하는 것만 1이고 나머지는 다 0 으로 처리하는 방식

print("정답:2, 2일 확률이 가장 높다고 추정할때 (0.6) : ",MSE(np.array(y),np.array(t)))
print('_______________')

y_7 = [0.1,0.05,0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print("정답:2, 7일 확률이 가장 높다고 추정할때 (0.6) : ",MSE(np.array(y_7),np.array(t)))
print('_______________')

def CEE(y,t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))

print("정답:2, 2일 확률이 가장 높다고 추정할때 (0.6) : ",CEE(np.array(y),np.array(t)))
print('_______________')
print("정답:2, 7일 확률이 가장 높다고 추정할때 (0.6) : ",CEE(np.array(y_7),np.array(t)))