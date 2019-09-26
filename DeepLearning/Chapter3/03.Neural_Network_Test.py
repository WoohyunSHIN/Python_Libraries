# 3.4. 3층 신경망 구현해보기 연습 
import numpy as np

X = np.array([1.0,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

print(X.shape)
print(W1.shape)
print(B1.shape)

A1 = np.dot(X,W1) + B1
print(A1)
print("_____________________")

# 시그모이드 활성화함수를 통해 output 값 받기
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
Z1 = sigmoid(A1)
print(Z1)
print("_____________________ END layer 1")

W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])

print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = np.dot(Z1,W2)+B2
print(A2)
Z2=sigmoid(A2)
print(Z2)
print("_____________________ END layer 2")

# 마지막 활성함수는 항등함수로 예시를 든다.
def identity_function(x):
    return x

W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])

print(Z2.shape)
print(W3.shape)
print(B3.shape)

A3 = np.dot(Z2,W3) + B3
Z3 = identity_function(A3)
print(Z3)
print("_____________________ END layer 3")
