# 다차원 배열
import numpy as np
A = np.array([1,2,3,4])
print(A) # [1 2 3 4]
print(np.ndim(A)) # 1
print(A.shape) # (4,)
print(A.shape[0])  # 4
print('__________________')

B = np.array([[1,2],[3,4],[5,6]])
print(np.ndim(B)) # 2
print(B.shape) # (3,2)
print('__________________')

C = np.array([[1,2],[3,4]])
D = np.array([[5,6],[7,8]])
# C*D를 하고 싶으면
F=np.dot(C,D)
print(F)
print('__________________')

# 3.3.3. 신경망에서 행렬의 곱
X = np.array([1,2])
print(X.shape) # (2,)

W = np.array([[1,3,5],[2,4,6]])
print(W.shape) #(2,3)

Y = np.dot(X,W)
print(Y) # [5 11 17]
print('__________________')
