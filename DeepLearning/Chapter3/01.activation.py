# 입력 신호의 총합을 출력 신호로 변환하는 함수를 일반적으로 activation function 활성화 함수 라고 표현한다.
# 다양한 활성화 함수중 먼저 계단함수와, 시그모이드 함수를 공부해 보겠다.

# 3.2.2. 계단 함수 구현
import numpy as np

# np 를 사용한 이유는 이렇게 해야 step_function(x) 에 들어오는 arguments 값을 여러개를 받을 수 있다. 
def step_function(x):
    y  = x > 0 
    return y.astype(np.int) 
# x = np.array([-1.0, 1.0, 2.0]) 일때,
# y = array([False, True, True], dtype=bool) 이며
# np.int가 False는 0으로 True는 1로 변환시켜서 return 해 주는 역활을 한다. 
x = np.array([-1.0,1.0,2.0])
print(step_function(x))
print('_____________')

# 3.2.3. 계단 함수의 그래프 
import matplotlib.pylab as plt
def step_function_1(x):
    return np.array(x>0, dtype=np.int)

x_1 = np.arange(-5.0, 5.0, 0.1)
y = step_function_1(x_1)
plt.plot(x_1,y)
plt.ylim(-0.1,1.1)
plt.show()

# 3.2.4. 시그모이드 함수 그래프
def sigmoid(x):
    return 1 / (1+ np.exp(-x))

x_2 = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x_2))
print('_____________')
y_2 = sigmoid(x_1)
plt.plot(x_1,y_2)
plt.ylim(-0.1,1.1)
plt.show()

# 3.2.7. ReLU 함수
def relu(x):
    return np.maxium(0,x)

# 3.5.1. 항등함수
def identity_function(x):
    return x

# 3.5.1. 소프트 맥스 함수 but, exp 를 사용하기 때문에 값이 너무 커지는 결함이 있다. 따라서 수정된 소프트맥스함수를 쓴다
def softmax_original(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a
    return y

# 3.5.2. 수정된 소프트맥스 함수
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c) # 오버플로 대책
    sum_exp_a = np.exp(exp_a)
    y = exp_a/sum_exp_a
    return y