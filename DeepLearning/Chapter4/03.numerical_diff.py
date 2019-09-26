# 수치 미분 함수화

def numerical_diff(f,x):
    h = 1e-4 # 0에 수렴한다라는 표현을 10^-4를 써서 사용한다.
    return (f(x+h)-f(x-h)) / (2*h)

# y = 0.01x^2 + 0.1x 의 function을 definition 화 
def function_1(x):
    return 0.01*x**2 + 0.1*x

import numpy as np
import matplotlib.pylab as plt
x = np.arange(0.0,20.0,0.1)
y = function_1(x)
plt.xlabel("x")
plt.xlabel("f(x)")
plt.plot(x,y)
plt.show()

print('_______________')
print('x=5일때, 해석적 해 :',numerical_diff(function_1,5)) # 진짜 해는 0.2
print('x=10일때, 해석적 해 :',numerical_diff(function_1,10)) # 진짜 해는 0.3

# [편미분]
# f(x0,x1) = x0^2 + x1^2 의 function을 definition 화
def function_2(x):
    return x[0]**2 + x[1]**2
    # 또는 return np.sum(x**2)
    
# [기울기] = gradient
def numerical_gradient(f,x):
    h = 1e-4
    grad = np.zeros_like(x) # x와 형상이 같은 0이 들어가는 배열을 생성

    for idx in range(x.size):
        tmp_val = x[idx]

        #f(x+h) 계산식
        x[idx] = tmp_val + h
        fxh1 = f(x)

        #f(x-h) 계산식
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 값 복원

    return grad

print("(3,4)에서의 기울기 :", numerical_gradient(function_2,np.array([3.0,4.0])))
print("(0,2)에서의 기울기 :", numerical_gradient(function_2,np.array([0.0,2.0])))
print("(3,0)에서의 기울기 :", numerical_gradient(function_2,np.array([3.0,0.0])))
print('_________________________')

# [경사법(경사하강법)] p.129 ~ p.131
def gradien_descent(f, init_x, lr=0.01, step_num=100):
    # f = 최적화 하려는 함수
    # init_x = 초깃값
    # lr = 학습률, '하이퍼파라미터'라고도 불린다.
    # step_num = 반복횟수

    x = init_x
    
    for i in range(step_num):
        grad = numerical_gradient(f,x)
        x = x- lr*grad
    return x
    
# 문제 : 경사법으로 f(x0,x1) = x0^2 + x1^2 의 최솟값을 구하여라
init_x = np.array([-3.0,4.0])
result=gradien_descent(function_2,init_x=init_x, lr=0.1, step_num=100)
print("정답:",result) # 실제 최소값은 (0,0) 이기에 거의 근소값이 나왔다.