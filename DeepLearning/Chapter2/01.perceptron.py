# 인간이 인공적으로 정해주는 부분은 w1, w2와 theta 와 같은 임계값을 정의해준다.
import numpy as np

# AND Logic without numpy
def AND(x1,x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


# AND Logic with numpy
x = np.array([0,1]) # 입력값
w = np.array([0.5, 0.5]) # 임의의 가중치
b = -0.7 # b=bias 편향
print(np.sum(w*x)+b)

def AND_1(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5, 0.5]) #임의의 가중치
    b = -0.7
    tmp = np.sum(x*w)+b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1 

# NAND 경우, 가중치와 편향의 부호만 반대이고 나머지는 동일하다.
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])  
    b = 0.7
    tmp = np.sum(x*w)+b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

#
def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(x*w)+b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1    

# NAND, OR --> AND 조합으로 만들어지는 XOR 조합
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND_1(s1,s2)
    return y