

// Reference Book : [점프 투 파이썬](https://wikidocs.net/book/1)

// Written by WoohyunSHIN. I reconstitute the reference book as my style for studying. If you have question or I commit an infrigement of copyright, send me a mail <swh159@gmail.com> please thank you.

# Python

***

#4. 함수

> 프로그래밍을 하다 보면 똑같은 내용을 반복해서 작성하고 있는 자신을 발견할 때가 종종있다. 특히 파이썬 같은 경우 들여쓰기의 가독성이 좋지 않기 때문에 많은 기능을 함수화 시켜 놓는게 필수 적이다. 

## 4.1. 파이썬의 함수 구조

> return 은 종료를 뜻하기도 하고 또는 다시 반환할 값을 지정할 수 있다. 예를 들어 **return a+b** 처럼 함수를 끝낼 수 있다. 다양한 함수들이 존재하는데
>
> - 일반적인 함수
>
> ```python
> >>> def add(a,b):
> ... 	result = a + b
> ... 	return result
> ```
>
> - 입력값이 없는 함수
>
> ```python
> >>> def say():
> ... 	return "Hi"
> ```
>
> - 결과값이 없는 함수
>
> ```python
> >>> def add(a,b):
> ... 	print("%d, %d의 합은 %d 입니다."%(a,b,a+b))
> ```
>
> - 입력값도 결과값도 없는 함수
>
> ```python
> >>> def say()
> ...	print('Hi')
> ```

```python
>>> def 함수명(매개변수):
... 	<수행할 문장1>
... 	<수행할 문장2>
... 	<수행할 문장3>
... 	return 
```

**IMPORTANT** :

#### 매개변수(parameter) vs 인수(argument) ?

```python
# a,b 는 parameter
>>> def add(a,b):
... 	return a+b

# 3,4 는 인수
>>> print(add(3,4))
```

***

## 4.2. 입력값이 몇개가 될지 모를때는 어떻게 해야할까 ?

> C 언어 같은 경우 malloc 을 사용하여 메모리 heap 에 공간을 잡아 놓고 사용해야하는데 파이썬은 이 부분해결을 아래와 같이 편하게 해결하도록 해놓았다. 모양은 **( )** 튜플 자료형으로 여러개의 매개 변수를 집어 넣을 수 있게 설정되어있다.

```python
>>> def add_many(*args):
... 	result = 0
... 	for i in args:
... 		result += i
... 		return result

# 변수의 갯수를 정해놓은 것과 달리 마음대로 집어 넣을 수 있다.
>>> print(add_many(1,2,3,4,5,6,912))
933
```

### 4.2.1. 키워드 파라미터 (kwargs)

keyword arguments 는 일반 arguments 와 달리 별표시(*) 를 **2개** 사용한다. 아래의 코드에서 확인해 보자. **kwargs 처럼 매개변수 명 앞에 

```python
>>> def print_kwargs(**kwargs)
... 	print(kwargs)
...
>>>
>>> print_kwargs(a=1)
{'a':1}

>>> print_kwargs(name='foo', age=3)
{'age':3,'name':'foo'}
```





### (수정해야한다) 3.5.2. 고객관리 프로그램(DB_function)

> 콘솔형 고객 정보 관리 시스템 구축

```python
import re
custlist=[]
page = -1

def exe(choice):
    if choice=="I":
        insertData()

    elif choice=="C":
        curSearch()

    elif choice=="P":
        preSearch()

    elif choice=="N":
        nextSearch()

    elif choice=="U":
        updateData()

    elif choice=="D":
        deleteData()

    elif choice=="Q":
        quit()

def insertData():
    customer = {"name":"", "sex":"", "email":"", "birthyear":""}
    customer["name"] = input("name = ")

    while True:
        customer["sex"] = input("sex = ")
        customer['sex']=customer['sex'].upper()
        if customer["sex"] in ("F","M"):
            break

    while True: # 정규식으로 이메일 검사하기
        regex = re.compile("^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,5}$")
        # ^[a-z][a-z0-9]{4,10} : 소문자 a~z 까지 첫글자로 시작하는 5개~11개 짜리 ID
        # [a-zA-Z]{2,6} : 대문자든 소문자든 상관없이 최소 2자리~6자리까지 들어올수 있다.
                    
        while True:
        # p = re.compile("[^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$]")
            customer["email"] = input("email = ")
            golbang = regex.search(customer["email"])
            if golbang != None:
                break
            else:
                print('"@"를 포함한 정확한 이메일을 써주세요.')
        
        check=0
        for i in custlist:
            if i["email"]==customer["email"]:
                check=1
        if check==0:
            break
        print("중복되는 이메일이 있습니다.")

    while True:
        customer["birthyear"] = input("birthyear = ")
        if len(customer["birthyear"])==4 and customer["birthyear"].isdigit():
            # 문자열에 있는 값들이 숫자값으로 조합이 되어있는지 알아보는 함수이다.
            break
        
    print(customer)
    custlist.append(customer)
    print(custlist)
    global page
    page = len(custlist)-1    

def curSearch():
    global page
    if page >= 0:
        print("현재 페이지는 {}쪽 입니다".format(page+1))
        print(custlist[page])
    else:
        print("입력된 정보가 없습니다.")    

def preSearch():
    global page
    if page <= 0:
        print("첫 번 째 페이지이므로, 이전 페이지 이동이 불가합니다.")
        print(page)
    else:
        page -= 1
        print("현재 페이지는 {}쪽 입니다".format(page+1))
        print(custlist[page])  

def nextSearch():
    global page
    if page >= len(custlist)-1:
        print("마지막 페이지이므로, 다음 페이지 이동이 불가합니다.")
        print(page)
    else:
        page += 1
        print("현재 페이지는 {}쪽 입니다".format(page+1))
        print(custlist[page])   

def updateData():
    while True:
        check_email = input("수정을 원하는 데이터의 이메일을 입력하세요 : ")
        idx = -1

        for i in range(0,len(custlist)):
            if check_email==custlist[i]["email"]:
                idk = i
                break

        if idk == -1:
            print("등록되지 않은 이메일입니다.")
            break 

        while True:
            select=int(input('''
            수정을 원하는 정보를 선택
            1. name
            2. sex
            3. birthyear
            4. quit
            선택 : '''))
            if select == 1:
                custlist[idk]['name']=input("name =")
                break
            elif select == 2:
                while True:
                    custlist[idk]["sex"] = input("sex = ")
                    custlist[idk]['sex']=custlist[idk]['sex'].upper()
                    if custlist[idk]["sex"] in ("F","M"):
                        break
                break
            elif select == 3:
                while True:
                    custlist[idk]["birthyear"] = input("birthyear = ")
                    if len(custlist[idk]["birthyear"])==4 and custlist[idk]["birthyear"].isdigit():
                        break
                break
            elif select == 4:
                break
            else:
                print("다시입력하시오")            
        break

def deleteData():
    global page
    delok=0
    check_email = input("삭제을 원하는 데이터의 이메일을 입력하세요 : ")
    
    for i in range(0,len(custlist)) :
        if check_email == custlist[i]["email"]:
            print("{} 고객님의 정보가 삭제되었습니다.".format(custlist[i]["name"]))
            del custlist[i]
            print(custlist)
            page=len(custlist)-1
            delok=1
            break

    if delok == 0:
        print("등록되지 않은 이메일입니다.")   

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()
    exe(choice)
```

