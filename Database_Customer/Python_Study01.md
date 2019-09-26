// Reference Book : [점프 투 파이썬](https://wikidocs.net/book/1)

// Written by WoohyunSHIN. I reconstitute the reference book as my style for studying. If you have question or I commit an infrigement of copyright, send me a mail <swh159@gmail.com> please thank you.

# Python

​	**Def )** 파이썬은 널리 쓰이는 범용, 고급 언어이다. 파이썬의 설계 철학은 코드 가독성에 중점을 두고 있으며, 파이썬의 문법은 프로그래머가 (C와 같은 언어에서 표현 가능한 것보다도) 더 적은 코드로도 자신의 생각을 표현하도록 한다. 파이썬은 프로그램의 크기에 상관없이 명확하게 프로그램 할 수 있는 구성 요소들을 제공한다. - Wikipedia

​	**특징 )** 

1. 인터프리터 방식의 언어(<--> 컴파일러 방식)
2. 객체 지향 언어
3. 무료, 간결 

***

## 1. 자료형

> 파이썬의 자료형으로는 숫자형, 문자열 자료형, 리스트 자료형, 튜플 자료형, 집합 자료형이 존재한다.

***

### 1.1. 숫자형

> 숫자형 자료형으로는 정수, 실수, 복소수, 2진수, 8진수, 16진수 같은 것이 존재한다.

* Integer

```python
>>> a = 123
>>> a = -178
>>> a = 0
```

* Floating-point

```python
>>> a = 1.2
>>> a = -3.45
```

또는 **e** 또는 **E** 를 사용하여 10^8 또는 10^-8 등을 나타낼수 있다.

```python
a = 4.24E8
a = 4.24e-8
```

* 

2진수를 만들기 위해서는 문자 **0b** 로 시작하면 된다.

```python
a = 0b101101101
```

* Octal

8진수를 만들기 위해서는 숫자가 **0o** 또는 **0O** 로 시작하면 된다.

```python
a = 0o177
```

* Hexadecimal

16진수를 만들기 위해서는 0x로 시작하면 된다.

```
>>> a = 0x8ff
>>> b = 0xABC
```

* Complex number

복소수를 사용하기 위해서는 **i** 대신 **j** 또는 **J** 를 사용하면 된다. 

```python
>>> a = 1+2j
>>> b = 3-4J

>>> a.real	
1.0 #a의 실수값을 리턴한다 
>>> a.imag
2.0 #a의 허수값을 리턴한다
>>> a.conjuate()	
(1-2j) #a의 켤레복소수를 리턴한다
>>> abs(a)	
2.2360 #a의 절대값을 리턴한다
```



***



### 1.2. 숫자형 연산자 

> 기본적인 사칙연산 { +,-,*,/ } 가 존재하며 특수한 연산자로써 **,%,// 등이 존재한다.

#### 1.2.1. ** 연산자

```python
>>> a=3
>>> b=4
>>> a**b
81	#a^b 값을 리턴한다
```

#### 1.2.2. % 연산자

```python
>>>  7%3
1	#나눗셈 후 나머지를 리턴한다
>>> 3%7
3 #나눗셈 후 나머지를 리턴한다
```

#### 1.2.3. // 연산자

```python
>>> 7/4
1.75

>>> 7//4
1	#나눗셈 후 소수점 아랫자리를 버린다.
```



***



### 1.3.  문자열(String)

> 파이썬에는 문자열을 만드는 여러 가지 방법이 존재한다. 예시를 통해서 알아보자

#### 1.3.1. 큰 따옴표(")로 양쪽 둘러싸기

```python
>>> food = "Python's favorite food is perl"
>>> food
Python's favorite food is perl 
# 문장안의 ' 작은 따옴표를 살리고 싶은 경우 사용한다.
```

#### 1.3.2.  작은 따옴표(')로 양쪽 둘러싸기

```python
>>> say = '"Python is very easy" he says.'
>>> say 
"Python is very easy" he says.
# 문안의 " 큰 따옴표를 살리고 싶은 경우 사용한다.
```

#### 1.3.3. C언어와 같이 백슬래시( \ ) 를 사용하면 큰, 작은 따옴표들을 문자열에 포함시킬 수 있다. 

```python
>>> food = "Python\'s favorite food is perl"
>>> food
Python's favorite food is perl

>>> say = "\"Python is very easy\" he says."
>>> say
"Python is very easy" he says.
```

#### 1.3.4. 여러 줄인 문자열을 변수에 대입하고 싶을 때는 **"""** 또는 **'''** 를 사용한다.

```python
>>> multiline="""
... Life is too short
... You need python
..."""

>>> multiline
Life is too short
You need python
```



***



### 1.4. 문자열 연산

> 다른 언어와는 달리 파이썬에서만 찾아볼수 있는 재미있는 기능으로써 파이썬만의 장점이다.

#### 1.4.1. 문자열 더하기

```python
>>> head = "Python"
>>> tail = "is fun!"
>>> head + tail
'Python is fun!'
```

#### 1.4.2. 문자열 곱하기

```python
>>> a = "python"
>>> a*2
'pythonpython'
```

#### 1.4.3. 문자열 곱하기 응용

```python
>>> print("="*50)
>>> print("My Program")
>>> print("="*50)
==================================================
My Program
==================================================
```



***



### 1.5. 문자열 인덱싱과 슬라이싱

> Indexing이란 무엇인가를 '가리킨다' 라는 의미이고, Slicing은 무엇인가를 '잘라낸다' 는 의미이다.

#### 1.5.1. 인덱싱이란 ?

```python
>>> a = "Life is too short, You need Python"
# 'L'이 0번 부터 시작하여 'n'이 33번까지 각 단어마다 인덱스가 걸려있다. 따라서 아래의 예시를 보면 이해를 하기 쉽다.

>>> a[0]
'L'

>>> a[12]
's'

>>> a[-2] 
'o' # 뒤에서 두번째 숫자
```

#### 1.5.2. 슬라이싱이란 ?

>  인덱스를 활용하여 연속적인 단어를 한번에 뽑아낼수 있도록 사용하는 것을 말한다. 사용법은 **a[*시작번호*:*끝번호*]** 의 형식으로 사용하면 된다.

```python
>>> a = "Life is too short, You need Python"

>>> a[0:4]
'Life'

>>> a[0:5]
'Life ' # 위의 예시와 같아 보이지만 공백문자가 들어간 완전히 다른 문자열이다. 

>>> a[19:]
'You need Python'
```

> **IMPORTANT** : 슬라이싱으로 문자열을 나누는 것은 슬라이싱 기법 중 가장 많이 사용되는 것중 하나이다.

```python
>>> a = "20010331Rainy"
>>> year = a[:4]	# 처음부터 a[3]번 까지
>>> day = a[4:8]	# a[4] ~ a[7] 까지
>>> weather = a[8:]

>>> year
'2001'
>>> day
'0331'
>>> weather
'Rainy'
```

#### 1.5.3. Pithon 을 Python 으로 바꾸기

> 문자열, 튜플 등의 자료형은 그 요소값을 변경할 수 없다. 따라서 immutable한 자료형이라고 한다. 그말인 즉, 문자열의 요소값은 바꿀 수 있는 값이 아니다 라는 말이다. 아래의 예시는 어떻게 바꿀 수 있는지에 대한 결과이다.

```python
>>> a = "Pithon"
>>> a = a[:1] + "y" + a[2:] # 문자열를 슬라이싱한 후 새로 다시 만든다.
>>> a
'Python'
```



***



### 1.6. 문자열 포매팅

> 포매팅이란 문자열 내에 어떤 값을 삽입하는 방법이다. 포매팅 코드로 {%s, %c, %d, %f, %o, %x, %%} 이 있다. 

####1.6.1. 숫자 대입

```python
>>> "I eat %d apples." %3	
'I eat 3 apples.'	#%d는 자연수 포맷코드
```

#### 1.6.2. 문자열 대입

> 문자열 포맷코드인 %s는 어떤 형대의 값이든 변환해 넣을 수 있다. 그 말인 즉 %s 는 자연수, 정수, 실수도 가능하다. 

```python
>>> "I eat %s apples." %"five"
'I eat five apples' #%s는 문자열 포맷코드

>>> "The pie is %s" %3.14
'The pie is 3.14'
```

#### 1.6.3. 숫자 값을 나타내는 변수 대입

```python
>>> number = 3
>>> "I eat %d apples." %number
'I eat 3 apples'
```

#### 1.6.4. 2개 이상의 값 대입

```python
>>> number =10
>>> day = "three"
>>> "I ate %d apples so I was sick for %s days." %(number,day)
'I ate 10 apples so I was sick for three days.'
```

#### 1.6.5. 정렬과 공백

```python
>>> "%10s" % "hi"
'        hi' 
# 10개의 공간을 만들고 앞의 8개 공간을 빈칸으로 놓아두고 hi를 집어넣어라 == 오른쪽 정렬

>>> "%-10s" % "hi"
'hi   jane.'
# 10개의 공간을 만들고 hi를 왼족 정렬 시킨다.
```

#### 1.6.6. 소수점 표현하기

> 소수점 자리의 길이가 너무 길때 소수점 자리 이후 x 번째 까지만 보겠다 라고 할때 사용한다.

```python
>>> "%0.4f" % 3.1415923896
'3.1415'

>>> "%10.4f" % 3.1415923896
'    3.1415'	
# 10개의 공간을 만들고 소숫점 4개의 숫자만 살린 후 뒤에서 부터 기입한다.
```

#### 1.6.7. format 함수를 이용한 포매팅

> 문자열이 가진 매서드 format 함수를 이용하여 포매팅을 할 수도 있다. **{index}** 자리에 format() 안의 값이 들어간다.

```python
>>> "I eat {0} apples".format(3)
'I eat 3 apples'

>>> "I eat {0} apples".format('five')
'I eat five apples'

>>> number = 10
>>> day='three'
>>> "I ate {0} apples so I was sick for {1} days".format(number, day)
'I ate 10 apples so I was sick for three days'

>>> "I ate {1} apples so I was sick for {0} days".format(number, day)
'I ate three apples so I was sick for 10 days'

# {0}, {1} 은 포맷에서 받는 arguments 의 index라고 보면 된다.
```

#### 1.6.8. f 문자열 포매팅

> 파이썬 3.6 버전 부터는 f 문자열 포매팅 기능을 사용할 수 있다. 아래와 같이 문자열 앞에 f 접두사를 붙이면 f 문자열 포매팅 기능을 사용할 수 있다.

```python
>>> name = '홍길동'
>>> age = 30
>>> f'나의 이름은 {name} 나이는 {age}'
'나의 이름은 홍길동 나이는 30'
```

> < 딕셔너리> 는 f 문자열 포매팅을 아래와 같이 사용할 수 있다. 딕셔너리 이기 때문에 key 값을 사용하여 value 값을 접근한다.

```python
>>> d = {'name' : '홍길동', 'age' : 30}
>>> f'나의 이름은 {d["name"]} 나이는 {d["age"]}'
'나의 이름은 홍길동 나이는 30'
```



***



### 1.7. 문자열 관련 함수

> java에서 사용했던 것과 같이 내재 되어있는 함수를 사용할때는 '.' 을 이용하여 사용한다.



#### 1.7.1. 문자 개수 세기 (count)

```python
>>> a = "hobby"
>>> a.count('b')
2

>>> a.count('')
6		# 글자의 갯수를 반환하는거 같은데 hobby 는 5개지만 마지막 /null 문자까지 반환한거 같다.
```

#### 1.7.2. 문자의 위치 정보 반환 (find, index)

> find 매서드 같은 경우 찾는 문자또는 문자열이 없을 경우 -1을 반환한다. 반면에 index 매서드 같은 경우 오류 메세지를 반환한다.

```python
>>> a = "Python is best choice"
>>> a.find('o')
4		# 처음 나오는 o의 위치 반환

>>> a.index('b')
10
>>> a.index('best')
10	# 시작부분의 위치 정보를 반환
```

#### 1.7.3. 문자열 삽입 (join)

```python
>>> ','.join('abcd')
'a,b,c,d'

>>> ','.join['ab','bb','cd']
'ab,bb,cd'
# 일반 string의 최소 단위는 character 이기 떄문에 a,b,c,d 로 output 되나, list 의 최소 단위는 element 이기 때문에 ab,bb,cd 로 나타내진다.
```

#### 1.7.4. 대, 소문자로 변경 (upper, lower)

```python
>>> a = 'hi'
>>> a.upper()
'HI'

>>> a = 'HI'
>>> a.lower()
'hi'
```

#### 1.7.5.  공백 지우기 (lstrip, rstrip, strip)

```python
>>> a = '  hi  ' 
>>> a.lstrip()
'hi  '

>>> a = '  hi  '
>>> a.rstrip()
'  hi'

>>> a = '  hi  '
>>> a.strip()
'hi'	# 양쪽 공백 지우기

```

#### 1.7.6. 정렬

> 원하는 칸 숫자만큼 칸을 만들고 character를 집어넣는다. 
>
> Tip.  뾰족한 방향으로 정렬이 된다. 

```python
>>> "{0:<10}".format("hi")
'hi        ' # 왼쪽 정렬

>>> "{0:>10}".format("hi")
'        hi' # 오른쪽 정렬

>>> "{0:^10}".format("hi")
'    hi    ' # 가운데 정렬


```

#### 1.7.7. 문자열 바꾸기 (replace)

```
>>> a = "Life is too short"
>>> a.replace("Life", "Your leg")
'Your leg is too short'
```

#### 1.7.8. 문자열 나누기 (split)

> case 1. split() 처럼 아무런 argument 을 넣어주지 않으면 빈칸을 기준으로 문자열을 나누게 되며, 결과 값 처리를 리스트 단위 대괄호[  ]로 리턴을 한다. 
>
> case 2. split(':') 처럼 괄호 안에 특정한 argument 을 지정해 주면 괄호안의 값을 구분자로 하여 문자열을 나누어 주게 된다.

```python
# case 1
>>> a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']

# case 2
>>> a = "a:b:c:d"
>>> a.split(":")
['a','b','c','d']
```



***



### 1.8. 리스트 (List)

> 리스트는 대괄호 [ ] 를 쓰며 값을 구분하기 위해서 ',' 를 사용한다. 인덱스를 가지며 인덱스란 말은 순서가 존재한다 라는 뜻이다. 배열 (array) 와 크게 다른점은 배열은 모든 데이터의 종류가 동일 해야하지만 리스트는 자료형과 상관없이 데이터를 가질 수 있다.

```python
>>> a = [ ] # 비어있는 리스트는 a = list() 로 생성할 수도 있다.
>>> b = [1,2,3]
>>> c = ['Life', 'is', 'too', 'short']
>>> d = [1,2,'Life','is']
>>> e = [1,2, ['Life','is']]
```

#### 1.8.1. 리스트 연산 

> 더하기(+), 반복하기(*), 길이구하기 등이 가능하다.
>
> **IMPORTANT** : len() 함수는 리스트, 튜플, 딕셔너리 자료형 등 다양한 자료형에서 사용가능하다.

```python
# 리스트 더하기
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> a+b
[1,2,3,4,5,6]

# 리스트 반복하기
>>> a = [1,2,3]
>>> a*3
[1,2,3,1,2,3,1,2,3]

# 길이 구하기
>>> a = [1,2,3]
>>> len(a)
3
```

#### 1.8.2. 리스트의 수정과 삭제(del)

```python
# 수정
>>> a = [1,2,4]
>>> a[2] = 4
>>> a
[1,2,4]

# 삭제
>>> a = [1,2,3]
>>> del a[1]
>>> a
[1,3]

# 단체 삭제
>>> a = [1,2,3,4,5]
>>> del a[2:]
>>> a
[1,2]
```



***



### 1.8. 리스트 관련 함수들

> 리스트 또한 변수명 뒤에 ','를 붙여서 여러 가지 리스트 관련 함수들을 이용할 수 있다.

#### 1.8.1. 요소 추가 (append)

> **Tip** : 가장 뒤의 인덱스에 추가를 한다.

```python
>>> a = [1,2,3]
>>> a.append(4)
>>> a
[1,2,3,4]
```

#### 1.8.2. 끼워넣기 (insert)

> append 와 달리 원하는 위치에 값을 끼워넣는다. **insert(*위치*,*값*)**

```python
>>> a = [1,2,3]
>>> a.insert(0,4)
>>> a
[4,1,2,3]
```

#### 1.8.3. 제거 (remove)

> 첫번째로 오는 target 을 삭제 시키는 역활을 한다.

```python
>>> a = [1,2,3,1,2,3]
>>> a.remove(3)
>>> a
[1,2,1,2,3]
```

#### 1.8.4. 정렬 (sort)

> 기본적으로 오름차순을 디폴트로 하며 내림차순으로 만들수도 있다.

```python
# 오름차순
>>> a = [1,4,3,2]
>>> a.sort()
>>> a
[1,2,3,4]

# 내림차순
>>> a = [1,4,3,2]
>>> a.sort(reverse=False)
>>> a
[4,3,2,1]
```

#### 1.8.5. 뒤집기 (reverse)

> reverse 함수는 정렬과 비슷해 보이지만 정렬과 달리 순서를 역순으로 거꾸로 뒤집어 준다. 

```python
>>> a = ['a','c','b','z']
>>> a.reverse()
>>> a
['z','b','c','a']
```

#### 1.8.6. 끄집어내기(pop)

> pop()은 라스트의 맨 마지막 요소를 돌려 주고 그 요소는 삭제하는 함수이다.

```python
>>> a = [1,2,3]
>>> a.pop(1)
2
>>> a
[1,3]
```

#### 1.8.7. 요소 x의 개수 세기(count)

```
>>> a = [1,2,3,1]
>>> a.count(1)
2
# argument 1 이 2개 들어 있다.
```

#### 1.8.8. 리스트 확장(extend)

```
>>> a = [1,2,3]
>>> a.extend([4,5])
>>> a
[1,2,3,4,5]

>>> b = [6,7]
>>> a.extend(b)
>>> a
[1,2,3,4,5,6,7]
```



****



### 1.9 튜플(tuple)

> 튜플은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 아래와 같다.
>
> 1. 리스트는 [ ] 로 둘러 싸지만 튜플은 ( ) 로 둘러싼다.
> 2. **(중요) **리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.

```python
>>> t1 = ( )
>>> t2 = (1, )
>>> t3 = (1,2,3)
>>> t4 = 1,2,3
>>> t5 = ('a','b',('ab','cd'))
```



**Tip** : 아래와 같이 튜플 요소의 값을 삭제 또는 변경 할 시 오류가 발생하며 진행되지 않는다.

```python
# 삭제시도
>>> t1 = (1,2,'a','b')
>>> del t1[0]

# 변경시도
>>> t1 = (1,2,'a','b')
>>> t1[0] = 'c'
```

**Tip** : 튜플에서 가능한 것은 **{인덱싱, 슬라이싱, 더하기, 곱하기, 길이 구하기}**는 가능하다.

```python
# 인덱싱
>>> t1 = (1,2,'a','b')
>>> t1[0]
1
>>> t1[3]
'b'

# 슬라이싱
>>> t1 = (1,2,'a','b')
>>> t1[1:]
(2,'a','b')

# 더하기
>>> t1 = (1,2,'a','b')
>>> t2 = (3,4)
>>> t1 + t2
(1,2,'a','b',3,4)

# 곱하기
>>> t2 = (3,4)
>>> t2 * 3
(3,4,3,4,3,4)

# 길이 구하기
>>> t1 = (1,2,'a','b')
>>> len(t1)
4
```



***



### 1.10 딕셔너리

> **정의** : Key와 Value 라는 것을 한 쌍으로 가지는 자료형이다. 딕셔너리는 리스트나 튜플 처럼 인덱스를 사용하지 않고 Key 를 사용하여 Value 값을 접근한다. 기본적인 딕셔너리의 모습은 아래와 같이 생겼다. 

```python
{Key1:Value1, Key2:Value2, Key3:Value3, ... }
```

> **Key : Value** 형태로 이루어져 있고 쉼표(,)로 구분되어 있다. Key에는 변하지 않는 값을 사용하고, Value 에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다.

```python
>>> a = {1: 'hi'}
>>> a = {'a':[1,2,3]}
```

> **딕셔너리 쌍 추가 or 요소 삭제하기** 
>
> * 새로운 key와 value를 추가하고 싶으면 **변수명[key] = value** 의 형식으로 추가를 하면 된다.
> * key와 value를 삭제하고 싶으면 **del 변수명[key]** 의 형식으로 key와 value를 삭제시키면된다.

```python
# 쌍 추가하기
>>> a = {1:'a'}
>>> a[2] = 'b'	# 새로운 쌍 추가
>>> a
{1:'a', 2:'b'}

>>> a[3] = [1,2,3]
>>> a
{1:'a', 2:'b', 3:[1,2,3]}

# 삭제
>>> del a[1]
>>> a
{2:'b', 3:[1,2,3]}
```



***



###1.11. 딕셔너리 사용법과 함수들

####1.11.1. 딕셔너리에서 Key사용해 Value 얻기

> 리스트나 튜플, 문자열은 요소값을 얻어내고자 할 떄 **인덱싱** 이나 **슬라이싱** 기법을 이용하여 얻어난다. 반면 딕셔너리는 **변수[key]** 의 값을 사용하여 Value 를 얻을 수 있다.

```python
>>> grade = {'pey':10, 'juilliet':99}
>>> grade['pey']
10
```

**IMPORTANT**

> 딕셔너리로 key와 value 쌍을 만들 때 key는 오직 단일 값이 되어야 한다. 만약  값이 같다면 무시가 된다. 아래는 예시이다. 또한 key 값으로는 리스트를 쓸 수 없다. value 값으로는 리스트를 사용할 수 있으나 key의 값을 리스트로 잡을 경우 오류가 뜬다.

```python
>>> a = {1:'a',1:'b'}
>>> a
{1:'b'}

>>> a={[1,2]:'hi'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

####1.11.2 Key 리스트 만들기(keys)

> 단일 key값이 리스트가 될순 없지만 key 값들을 모아서 리스트를 만들어 주는 함수는 존재한다. list(a.keys())는 딕셔너리의 a의 key만을 모아서 리스트 형식으로 객체를 돌려준다.

```python
>>> a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
>>> list(a.keys())
['name','phone','birth']
```

####1.11.3 Value 리스트 만들기(values)

> Key를 얻는 걷과 마찬가지 방법으로 Value 만 얻고 싶다면 values 함수를 사용하면 된다.

```python
>>> a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
>>> list(a.values())
['pey','0119993323','1118']
```

####1.11.4 key:value 쌍 모두 지우기(claer)

> clear 함수는 딕셔너리 안의 모든 요소를 삭제한다.

```python
>>> a.clear()
>>> a
{} 
```

####1.11.5 해당 Key가 딕셔너리 안에 있는지 조사하기(in)

> boolen 값을 반환받을 수 있다.

```python
>>> a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
>>> 'name' in a
True
>>> 'email' in a
False
```





삭제

```
>>> del a[2] #인덱스 2가 아니라 키값 2 이다.
```



### 1.10. 딕셔너리 관련 함수들



### 1.11. 집합 자료형

