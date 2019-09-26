// Reference Book : [점프 투 파이썬](https://wikidocs.net/book/1)

// Written by WoohyunSHIN. I reconstitute the reference book as my style for studying. If you have question or I commit an infrigement of copyright, send me a mail <swh159@gmail.com> please thank you.

# Python

***

###변수 표기법이란 ?

파이썬에서는 2가지 변수 표기법이 존재한다. 카멜표기법과 스네이크표기법 두가지가 존재한다.  

1. 카멜표기법은 대문자와 소문자로 구분을 한다.

   typeName

2. 스네이크표기법은 언더바 (_)로 구분을 한다

   type_name

***

## 2. 제어문

> 파이썬에서 if, while, for 등 제어문을 여기서 부터 다룰 것이다.

### 2.1. if문

> 조건문에서 테스트를하여 그 값이 참(True)이면 if문 바로 다음 문장을 수행하고, 조건문이 거짓(False)이면  else문 다음의 문장을 수행한다. 또한 **들여쓰기** 와 조건문 뒤에 **:** 가 무엇보다 중요하다. 아래의 예를 보자.



> **Tip** : 파이썬에서는 if의 가독성이 좋지 않기 때문에 2단, 3단 중첩하여 if 를 사용하는 것은 좋지 않다.

```python
# 실행가능
>>> if 조건문:
... 	수행할 문장 1
... 	수행할 문장 2
... 	수행할 문장 3
	
# 오류 1
>>> if 조건문:
... 	수행할 문장 1
... 수행할 문장 2
... 	수행할 문장 3

# 오류 2
>>> if 조건문:
... 	수행할 문장 1
... 		수행할 문장 2
... 	수행할 문장 3
```

####2.1.1. 비교연산자

> 조건문에 비교연산자(<, >, ==, !=, >=, <=) 가 존재 하며 C언어에서 사용하는 방법과 동일하다. 아래의 예시에서 알아 둘 것은 리턴하는 값의 자료형은 bool 로써 참인지 거짓인지를 판단해준다.

```python
>>> x = 3
>>> y = 2
>>> x > y
True
```

#### 예시

```python
>>> money = 2000
>>> if money >= 3000:
... 	print("택시를 타고 가라")
... else:
... 	print("걸어가라")
...
걸어가라
```

>**and, or, not**  : 조건을 판단하기 위해 사용하는 다른 연산자

```python
>>> money = 2000
>>> card = True
>>> if money >= 3000 or card:
... 	print("택시를 타고 가라")
... else:
... 	print("걸어가라")
...
택시를 타고 가라
# money가 3000이상 이지는 않지만 card가 True 이기 떄문에 실행문 1을 진행한다. 
```

#### 2.1.2. x in s, x not in s 

> 다른 프로그래밍 언어에서는 볼수 없는 특수한 조건문들을 제공한다. 요소 x 가 s ={리스트, 튜플, 문자열} 안에 존재 하는 가 ? 라는 말이며 리턴하는 값은 bool 자료형 이다.

```python
# 리스트
>>> 1 in [1,2,3]
True
>>> 1 not in [1,2,3]
False

# 튜플
>>> 'a' in ('a','b','c')
True
>>> 'j' not in 'python'
True

# if문
>>> pocket = ['paper','cellphone','money']
>>> if 'money' in pocket:
... 	print("택시를 타고 가라")
... else:
... 	print("걸어가라")
...
택시를 타고 가라
```

> **Tip** : 아래와 같이 True 조건문에서 아무 일도 일어나지 않게 만들고 싶을 경우 **pass** 라는 변수를 사용하면 if문이 종료 되고 그 다음 코드로 넘어간다. 

```
>>> pocket = ['paper', 'money', 'cellphone']
>>> if 'money' in pocket:
... 	pass
... else:
... 	print("카드를 꺼내라")
...
```

#### 2.1.3. elif 

> 위에서 언급한 것 처럼 파이썬의 if는 가독성이 좋지 않다 따라서 elif 를 사용하여 여러 조건을 만들어 줄 수 있다.

```python
# if * 2
>>> pocket = ['paper', 'handphone']
>>> card = True
>>> if 'money' in pocket:
... 	print("택시를 타고가라")
... else:
... 	if card:
... 		print("택시를 타고가라")
...		else:
...			print("걸어가라")
...
택시를 타고가라

# elif 활용
>>> pocket = ['paper','cellphone']
>>> card = True
>>> if 'money' in pocket:
... 	print("택시를 타고가라")
... elif card:
...		print("택시를 타고가라")
... else:
... 	print("걸어가라")
...
택시를 타고가라
```



***



### 2.2. while문

> 반복해서 문장을 수행해야 할 경우 while 문을 사용한다. 아래는 while 문의 **기본 구조** 이다.

```
>>> while 조건문:
... 	수행할 문장1
...		수행할 문장2
... 	수행할 문장3
```

> while문의 코드 진행을 이해를 위한 간단한 프로그램

```python
>>> treeHit = 0
>>> while treeHit < 10:
... 	treeHit = treeHit +1 	#Tip : C 언어와 같이 treeHit += 1 도 가능하다.
... 	print("나무를 %d번 찍었습니다." %treeHit)
...		if treeHit == 10:
...			print("나무가 넘어갑니다")
...
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무가 넘어갑니다.
```

#### 2.2.1. while문을 사용하여 관리프로그램

> 여느 다른 프로그램과 같이 while문을 사용하면 계정 관리 프로그램을 만들수 있다.
>
> **Tip** : input() 함수는 사용자로 부터 입력 값을 받을 수있는데 default 값으로 string 으로 받기 때문에 정수로 사용하기 위해서는 형전환을 해야한다. 

``` python
>>> prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """
>>>
>>> number = 0
>>> while number != 4:
... 	print(prompt)
...		number = int(input())
...

1. Add
2. Del
3. List
4. Quit

Enter number:
```



#### 2.2.2. while문 강제로 빠져나가기 (break)

> 다른 언어와 동일하게 **break** 를 사용하여 while문 또는 for문 에서 다음 진행 코드로 가기위해 빠져 나오는게 가능하다. 
>
> **IMPORTANT** : while의 조건문을 True 라고 해놓을 경우 무한 루프에 걸려 메모리가 가득 찰 때 까지 작동하다가 overflow가 되어 프로그램이 종료 될수 있다. 이런경우 Ctrl + C 를 눌러 while 문을 빠져나올 수 있다.

```python
>>> coffee = 10
>>> while True:
...		money = int(input("돈을 넣어주세요 : "))
...		if money == 300:
... 		print("커피를 줍니다.")
...			coffee = coffee -1
...		elif money > 300:
...			print("거스름돈 %d를 주고 커피를 줍니다" %(money-300))
...			coffee -= 1
...		else:
...			print("돈을 다시 돌려주고 커피를 주지 않습니다.")
...			print("남은 커피의 양은 %d개 입니다." %coffee)
...		if coffee == 0:
...			print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
...			break
...	
```



#### 2.2.3. while문 맨 처음으로 돌아가기 (continue)

```python
# 홀수만 출력하는 프로그램을 만들수 있다.
>>> a = 0
>>> while a < 10:
... 	a = a + 1
... 	if a%2 == 0:
...			continue
...		print(a)
...
1
3
5
7
9
```



***



### 2.3. for문

> 리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 **변수에 대입**되어 "수행할 문장 1", "수행할 문장2" 등이 수행된다. 아래는 for문의 기본 구조이다.

```python
>>> for 변수 in 리스트(또는 튜플, 문자열):
... 	수행할 문장1
...		수행할 문장2
...
```



#### 2.3.1. for문 예제들

```python
#case 1
>>> test_list = ['one', 'two', 'three']
>>> for i in test_list
... print(i)
...
one
two
three

#case 2
>>> a = [(1,2),(3,4),(5,6)]
>>> for (first,last) in a:
...		print(first + last)
...
3
7
11

#case 3
>>> marks = [90,25,67,45,80]
>>> number =0
>>> for mark in marks:
... 	number = number +1
...		if mark >= 60:
...			print("%d번 학생은 합격입니다." %number)
...		else:
...			print("%d번 학생은 불합격입니다." %number)
...
1번 학생은 합격입니다.
2번 학생은 불합격입니다.
3번 학생은 합격입니다.
4번 학생은 불합격입니다.
5번 학생은 합격입니다.
```



#### 2.3.2. for 문과 continue



#### 2.3.3. for 문과 range함수

> 순차적으로 진행이 되어야 하는 경우 range() 함수르 사용하면 된다.



#### 2.3.4. 리스트 안에 for문 포함하기



### 2.4. Quiz

#### 2.4.1 주민등록 번호를 입력하면 성별을 출력

```python
# 1st
>>> a = input("주민번호 입력 :")
>>> if a[7]=='1' or a[7]=='3':
...		print("남자")
... elif a[7]=='2' or a[7]=='4':
...		print("여자")
... else:
...		print("잘못입력했습니다.")

# 2nd
>>> total = input("주민번호 입력 :")
>>> head = total[0:6]
>>> tail = total[7:]
>>> tail = int(tail)
>>> tail = tail//1000000
>>> 
>>> if tail%2 == 0:
... 	print("여성")
>>> else:
... 	print("남성")
```



#### 2.4.2. 2~9단 까지 출력

```python
# 1st
>>> for x in range(2,10):
...     print("\n==[%d단]==" %x)
...     for y in range (1,10):
...		     print("%d x %d = %d" %(x,y,x*y))

# 2nd
>>> for y in range(1,10):
...    for x in range(2,10):
...        #print("%d x %d = %2d" %(y,x,x*y),end='    ')           
...        print("{} x {} = {:2}".format(y,x,x*y),end='    ')
...    print()

# print()함수는 end값을 \n 을 가지고 있어서 \n을 4칸의 빈공간으로 바꾼다라는 뜻이다.
```



#### 2.4.3. 커피가격

> 사전에 {커피이름 : 가격}을 등록하고 커피이름만 보여준 후 커피이름을 입력하면 가격을 보여준다. coffee={'아메리카노':2500,'카페라떼':3000,'카푸치노':3500}

```python
# 1st
>>> coffee={'아메리카노':2500,'카페라떼':3000,'카푸치노':3500}
>>> print("메뉴 : 아메리카노\t카페라떼\t카푸치노")
>>> ch = input("선택 : ")
>>>
>>> if ch in coffee:
...     print("%s원입니다." %coffee[ch])
... else:
...     print("원하시는 메뉴가 존재하지 않습니다.")

# 2nd
>>> coffee={'아메리카노':2500,'카페라떼':3000,'카푸치노':3500}
>>> for c in coffee:
... 	print(c,end='  ')
>>> print()
>>>
>>> order = input("선택 :")
>>> for k,v in coffee.items(): # 튜플로 리턴 (키=k,값=v)
... 	if k==order:
... 		print(v)
```



#### 2.4.4. 덧셈문제 맞추기

> 1~50 사이 숫자 중 임의의 숫자를 선택해서 덧셈 문제를 내면 맞추는 게임

```python
# Simple method
>>> import random
>>> 
>>> cnt = 0
>>> for i in range(0,5):
...     a = random.randint(1,50)
...     b = random.randint(1,50)
...     print("%d + %d = " %(a,b))
...     c=int(input())
...     if a+b==c:
...         print("정답!")
...         cnt+=1
...     else: 
...         print("오답!")
>>> print("총 %d 개 정답!" %cnt)

# Hard method
# random.choice() 를 사용 하여 내가 원하는 요소안에서 랜덤으로 뽑을 수 있다.
# 내장함수 eval() 를 사용하여 operators를 처리하였다.
>>> import random
>>>
>>> cnt = 0
>>> op_tuple = ('+','-','/','*')
>>> for i in range(0,5):
...     a = random.randint(1,50)
...     b = random.randint(1,50)
...     op = random.choice(op_list)
...     print("%d %c %d = " %(a,sym,b))
...     c=int(input())
...     if int(eval("%d %c %d" %(a, sym, b)))==c: # 나누기 때문에 int()
...         print("정답!")
...         cnt+=1
...     else: 
...         print("오답!")
>>> print("총 %d 개 정답!" %cnt)
```



#### 2.4.5. 시간 맞추기 게임

> 시간과 관련된 time 모듈에는 유용한 함수가 굉장히 많다. 사용을 하기 위해서는 import time 을 해야 한다.
>
> 문제 : 게임을 시작할 때 사용자가 엔터기를 입력하면 시작한다. 속으로 20 초를 카운트하고 엔터키를 입력하여 가장 근접한 시간 맞추는 게임 time.time()이용 

```python
>>> import time
>>> 
>>> input("엔터를 누르고 20초를 셉니다.")
>>> start = time.time()
>>> input("20초 후에 다시 엔터를 누릅니다.")
>>> end = time.time()
>>> 
>>> diff = end - start
>>> print("실제 시간 :", diff, "초")
>>> print("차이 :", abs(diff-20), "초")
```



#### 2.4.6. 숫자 맞추기 게임

> 1 ~ 100 사이의 숫자 중에 하나를 컴퓨터가 정하면 그 숫자를 맞춘다. 시간과 횟수도 check 하라

```python
>>> import random
>>> import time
>>> 
>>> target=random.randint(1,100)
>>> cnt = 0
>>> print('답 : ',target)
>>> input("엔터를 누르면 시작합니다!")
>>> start = time.time()
>>> 
>>> while True:
...     guess = int(input("1~100 사이 숫자를 입력하세요 :"))
...     cnt += 1 
...     if guess==target: 
...         print("정답입니다")
...         break
...     elif guess<target:
...         print("더 큰 수를 입력하세요")
...     else:
...         print("더 작은 수를 입력하세요")
>>> end = time.time()
>>> 
>>> diff = end - start
>>> print("걸린시간은 {:.0f}초 입니다.".format(diff))
>>> print("걸린횟수는 %d 입니다." %cnt)
```



#### 2.4.7. 로또번호 생성

> 1~45사이의 번호 6개를 추출한다. 중복은 허락하지 않으며 총 5번에 겇쳐 번호를 추출하여 정렬하여 출력해준다. **#import random** 안에는 **sample** 라는 함수가 있다. 이 함수는 중복을 허락 하지 않기 때문에 더 쉽게 만들 수 있다.

```python
# échec
>>> import random
>>> 
>>> for x in range(0,5): 
...     s = set()
...     for i in range(0,6): 
...         s.add(random.randint(1,45))
...     a_l = list(s)
...     a_l.sort()
...     print("로또 : ",a_l)

# réussite
>>> for i in range(5):
...     lotto = [0,0,0,0,0,0]
...     for x in range(6):
...         num=0
...         while(num in lotto):
...             num=random.randint(1,46)
...         lotto[x]=num
...     print("로또 : ",sorted(lotto))

# Using function sample 
>>> for i in range(1,6):
...     print("로또 ; ",sorted(random.sample(range(1,46),6)))
```



#### 2.4.8. 야구게임

> 중복되지 않는 3자리 숫자를 컴퓨터가 정하면 그 숫자를 맞출 때 까지 반복한다. 
>
> * 숫자와 자리 위치까지 일치하면 스트라이크 
> * 숫자는 있는데 자리는 맞지 않는다면 볼
>
> 스트라이크가 3개가 되면 맞춘 것이므로 멈춘다. 몇 번 만에 맞춘 것인지 횟수도 체크한다.

```python
>>> import random
>>> 
>>> target = random.sample(range(100,999),3) 
>>> # 3개의 숫자를 뽑으면 알아서 리스트로 들어간다. 
>>> print(target)
>>> strick=0
>>> check=0
>>> print("시작")
>>> 
>>> while strick != 3:
...     strick = 0
...     ball = 0
...     guess = list(input("3자리 숫자를 입력하세요 :"))
...     print(guess)
...     for a in guess:
...         for b in target:
...             if int(a) == b:
...                 if guess.index(a) == target.index(b):
...                     strike+=1
...                 else:
...                     ball+=1
...     check+=1
...     print("strike:%d, ball:%d, try:%d" %(strike,ball,check))
>>> print("정답")   

```



### 2.4.9. 타자게임

>  Input 함수를 이용하여 사용자가 타자 게임을 시작할 준비를 하고 Enter 를 누를 때까지 기다림. 여러 개의 단어 중 5개의 단어를 무작위로 추출하여 보여주고 정확하게 입력하면 다음 단어로 넘어가도록한다. 시작시간과 끝나는 시간을 체크하여 5개의 단어를 입력하는데 얼마의 시간이 걸렸는지 알려준다.

```python
>>> import random
>>> import time
>>> 
>>> n=1
>>> w = ["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
>>> q=random.choice(w)
>>> input("시작!")
>>> start = time.time()
>>> 
>>> while n<=5:
...     print("*문제",n)
...     print(q)
...     x=input()
...     if q == x:
...         print("통과!")
...         n+=1
...         q=random.choice(w)
...     else:
...         print("오타! 다시도전!")
>>> 
>>> end = time.time()
>>> t=end-start
>>> print("타자 시간 : {:.0f}초".format(t))
```



