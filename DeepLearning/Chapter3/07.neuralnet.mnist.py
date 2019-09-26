import numpy as np
from mnist import load_mnist
import pickle

def sigmoid(x):
    return 1 / (1+ np.exp(-x)) 

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c) # 오버플로 대책
    sum_exp_a = np.exp(exp_a)
    y = exp_a/sum_exp_a
    return y

def get_data():
    (x_train, t_train),(x_test, t_test)=\
    load_mnist(flatten=True, normalize=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("/Users/Shinwoohyun/Desktop/DeepLearning/Chapter3/sample_weight.pkl","rb") as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1,W2,W3 = network['W1'],network['W2'],network['W3']
    b1,b2,b3 = network['b1'],network['b2'],network['b3']

    a1 = np.dot(x,W1)+b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2)+b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3)+b3
    y = softmax(a3)
    return y

x,t = get_data()
network = init_network()

# 단일 이미지 카운트
accuracy_cnt = 0
for i in range(len(x)):
    y=predict(network,x[i])
    p = np.argmax(y)    # 확률이 가장 높은 원소의 인덱스를 얻는다.
    if p == t[i]:
        accuracy_cnt +=1
print("Accuracy:"+str(float(accuracy_cnt)/len(x)))
print('______________________ Solo')

# 배치 처리를 하여 100개의 이미지 한번에 처리
batch_size = 100    # 배치 크기
accuracy_cnt_batch = 0
for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt_batch += np.sum(p == t[i:i+batch_size])
print("Accuracy:"+str(float(accuracy_cnt_batch)/len(x)))
