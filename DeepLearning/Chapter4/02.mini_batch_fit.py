import sys,os
sys.path.append(os.pardir)
import numpy as np
from mnist import load_mnist

(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape) # (60000,784) : 60000개의 데이터 28*28 픽셀 
print(t_train.shape) # (60000,10) : 60000개의 데이터, 10줄 짜리 데이터 == [0,0,1,0,0,0,0,0,0,0]

"""
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
"""

# 4.2.4. 배치용 교차 엔트로피 오차
# 아래의 해당 코드는 원-핫 인코딩으로 1과 다수의 0 으로 이루어 져있을 경우사용한다.
# version. one_hot_encoding
def cross_entropy_error(y,t):
    if y.ndim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)
    
    batch_size = y.shape[0]
    return -np.sum(t*np.log(y+1e-7))/batch_size

# version. not one_hot_encoding
def cross_entropy_error_NOHE(y,t):
    if y.ndim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)
    
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size),t] + 1e-7))/batch_size
