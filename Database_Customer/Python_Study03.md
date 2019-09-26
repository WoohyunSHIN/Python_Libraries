// Reference Book : [점프 투 파이썬](https://wikidocs.net/book/1)

// Written by WoohyunSHIN. I reconstitute the reference book as my style for studying. If you have question or I commit an infrigement of copyright, send me a mail <swh159@gmail.com> please thank you.

# Python

***

#3. 파일 읽고 쓰기

> 파일을 통한 입출력 방법에 대해서 알아보자

## 3.1. 파일 생성 및 열고 출력값 적기('w')

### 3.1.1. 파일 생성하기

파일을 생성하기 위해 우리는 open 이라는 파이썬 내장함수를 사용했다. open 함수는 다음과 같이 "파일 이름"과 "파일 열기 모드"를 입력값으로 받고 결과값으로 파일 객체를 돌려준다.

```python
f = open("새파일.txt", "w")
f.close()

파일객체 = open(파일이름, 파일 열기모드)
```

**[파일 열기 모드]**

1. **r** : 읽기모드 - 파일을 읽기만 할 때 사용
2. **w** : 쓰기모드 - 파일에 내용을 쓸 때 사용 
3. **a** : 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

**IMPORTANT** : 파일 쓰기 모드로 열게 되면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일이 생성된다.

```python
>>> f = open("/Users/Shinwoohyun/Desktop/Github/ML_Projet/ML_Projet/newfile.txt", 'w')
>>> f.close()
# 해당 절대경로에 새로운 파일이 생성 되었다.
```

***

### 3.1.2. 파일을 쓰기 모드로 열어 출력값 적기

여기서는 위의 파일에 에디터를 열고 프로그램의 출력값을 파일에 직접 써 보자.

```python
>>> f = open("/Users/Shinwoohyun/Desktop/Github/ML_Projet/ML_Projet/newfile.txt", 'w')
>>> for i in range(1,11):
... 	data = "%d번째 줄입니다.\n" %i
... 	f.write(data)
>>> f.close()
```

***

## 3.2. 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법('r')

### 3.2.1. readline() 함수 이용

해당 함수는 파일의 **첫 번째 한 줄**을 읽어 리턴하는 경우이다. 추가로 여러 줄을 리턴받고 싶다면 제어문을 사용하여 모든 데이터를 리턴 할 수 있다.

```python
# 1줄만 리턴
>>> f = open("/Users/Shinwoohyun/Desktop/Github/ML_Projet/ML_Projet/newfile.txt", 'r')
>>> line = f.readline()
>>> print(line)
>>> f.close()
1번째 줄입니다.

# 모든 데이터 리턴
>>> f = open("/Users/Shinwoohyun/Desktop/Github/ML_Projet/ML_Projet/newfile.txt", 'r')
>>> while True:
... 	line = f.readline()
... 	if not line: break
... 	print(line)
>>> f.close()
```



### 3.2.2. readlines() 함수 이용

해당 함수는 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 **리스트**로 리턴한다. 따라서 아래의 lines는 **["1 번째 줄입니다.\n","2 번째 줄입니다.\n","3 번째 줄입니다.\n","4 번째 줄입니다.\n",…,"10 번째 줄입니다.\n"]** 의 리스트 변수가 된다.

```python
>>> f = open("/Users/Shinwoohyun/Desktop/Github/ML_Projet/ML_Projet/newfile.txt", 'r')
>>> lines = f.readlines()
>>> for line in lines:
... 	print(line)
>>> f.close
```



### 3.2.3. read() 함수 이용

해당 함수는 파일의 내용 전체를 문자열로 리턴한다.

```python
>>> f = open("/Users/Shinwoohyun/Desktop/Github/ML_Projet/ML_Projet/newfile.txt", 'r')
>>> data = f.read()
>>> print(data)
>>> f.close()
```

***

## 3.3. 파일에 새로운 내용 추가하기 ('a')

쓰기 모드 ('w')로 파일을 열 때 이미 존재하는 파일을 열 경우 그 파일의 내용이 모두 사라지게 된다. 하지만 원래 있던 값을 유지하면서 새로운 값을 추가하길 원한다면 ('a') 로 열면 된다.

```python
>>> f = open("/Users/Shinwoohyun/Desktop/Github/ML_Projet/ML_Projet/newfile.txt", 'a')
>>> for i in range(11,20):
... 	data = "%d번째 줄입니다.\n" %i
... 	f.write(data)
>>> f.close
```



***



## 3.4. with 문

지금까지는 아래와 같은방식으로 파일을 열고 닫아 왔다. 항상 파일을 열면 같이 close를 해주는 것이 좋다 하지만 그것에는 불편함이 따른다. with문을 이용하면 이 불편한 점을 해결 할수 있다.

```python
# 일반문
>>> f = open("/Users/Shinwoohyun/Desktop/Github/ML_Projet/ML_Projet/foo.txt", 'w')
>>> f.write("Life is too short, you need python")
>>> f.close()

# with문
>>> with open("/Users/Shinwoohyun/Desktop/Github/ML_Projet/ML_Projet/foo.txt", "w") as f:
... f.write("Life is too short, you need python")

```



## 3.5. 연습문제

### 3.5.1 타자게임 (++)

>  **2.4.9. 타자게임** 에서 했던거와 동일하게 문제를 맞추는 것을 진행한다 다만 while 문을 사용하여 문제를 외부에서 불러올 것인지 아니면 내부에 있는 문제를 그대로 사용할 것인지 나누고 단순 종료 버튼도 만든다. 

```python
>>> import random
>>> import time
>>> 
>>> n=1
>>> w = ["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
>>> input("시작!")
>>> start = time.time()
>>> 
>>> while True:
...     print("1.문제불러오기\n2.타자게임\n3.종료하기")
...     menu = input("메뉴를 선택하세요 : ")
... 
...     if menu == "1" :
...         f=open("/Users/Shinwoohyun/Desktop/Github/ML_Projet/ML_Projet/w_expo.txt","r")
...         line = 1 # while문 진입을 위해서 사용
...         w.clear()
...         while line:
...             line = f.readline().replace("\n","")
...             if not(line==""):
...                 w.append(line)
...         print(w)
... 
...     elif menu == "2" :
...         q=random.choice(w) 
...         while n<=5:
...             print("*문제",n)
...             print(q)
...             x=input()
...             if q == x:
...                 print("통과!")
...                 n+=1
...                 q=random.choice(w)
...             else:
...                 print("오타! 다시도전!")
... 
...     elif menu == "3" : break
>>> end = time.time()
>>> t=end-start
>>> print("타자 시간 : {:.0f}초".format(t))
```



### 3.5.2. 고객관리 프로그램(DB)

> 콘솔형 고객 정보 관리 시스템 구축

1. 기능 : 고객 정보 입력(I), 현재/이전/다음 고객 정보 조회(C/P/N), 고객 정보 수정(U), 고객 정보 삭제(D), 고객 정보 종료(Q)
- 괄호 안 영문자를 입력하면 각 기능이 구현되게 만든다  
- 종료(Q)를 입력하기 전까지 기능 선택 메시지가 계속 뜨도록 만든다  
- 각 기능은 함수로 관리한다  
- 입력된 각 정보는 인덱스 값에 따라 페이지를 가진다  
   -> 첫 정보 입력시 인덱스는 0이므로, 입력 전 기본 page 값은 -1로 설정한다

2. 입력(I)
- dictionary로 각 키의 값을 받고 빈 리스트에 채워나간다
- 성별(sex) : M, m, F, f로만 입력 가능  
                -> 소문자로 입력하는 경우 대문자로 자동 변환  
                -> sex 값이 M 또는 F가 아닐 경우 다시 입력  
- 이메일(email) : 입력값 내 '@'가 반드시 있어야 함  
                    -> 정규표현식 사용  
                    -> re를 import 하여 이메일 입력값 내 '@' 존재 여부 파악  
                    -> 없는 경우 '@'를 포함하라는 문구와 함께 재입력 하도록 함
- 출생년도(birthyear) : 4자리로 입력 해야  
                          -> len 값으로 입력 값의 길이를 구함  
                          -> 4자리가 아닐 경우 재입력 하도록 함
- 출생년도까지 입력이 완료되었을 경우  
     -> 키 값 입력이 완료된 customer 딕셔너리를 custlist 리스트에 추가(append)한다  
     -> 고객 정보가 새로 입력 되었으므로 page 값에 1을 더한다

3. 조회(C, P, N)
- 인덱스는 0부터 시작하나 페이지는 통상 1부터 시작하므로 페이지 출력시 page+1 값을 반환한다
- 이전 페이지 조회(P)의 경우, 첫 번 째 페이지인 상태에서 이전 페이지로 이동이 불가하므로 현재 페이지인 첫 번 째 페이지를 반환
- 다음 페이지 조회(N)의 경우, 마지막 페이지인 상태에서 다음 페이지로 이동이 불가하므로 현재 페이지인 마지막 페잊이를 반환
                
4. 삭제(D)
- unique한 키를 기준으로 삭제정보를 선택한다 -> 여기서는 이메일로 가정
- 삭제 성공 여부 변수(delok)  
   -> 입력한 이메일이 등록된 정보 내에 있을 경우 삭제  
   -> 삭제가 성공하면 delok=1 (default 값 0)  
   -> 등록된 정보 내에 없는 이메일일 경우(delok=0) 등록되지 않았다고 출력 
5. 수정(U)
- unique한 키를 기준으로 수정정보를 선택한다 -> 여기서는 이메일로 가정
- 입력한 이메일과 일치하는 고객 정보의 인덱스를 idx에 입력  
   -> idx의 default 값은 -1  
   -> 일치 여부 확인 후에도 idx가 -1일 경우 등록되지 않았다고 출력
- 이메일 외에 이름, 성별, 출생년도 중 수정할 정보 선택
- 수정할 정보 선택 후 수정할 내용 입력
- 수정하고픈 변수가 없는 경우 exit 입력 시 수정창 종료

6. 종료(Q)

- 맨처음 while 반복문을 나간다 -> break

```python
import re
custlist=[]
page=-1
# page = 데이터가 몇개 들어가 있는지를 알려주는 역활을 할 것이다. stack 의 top의 역활

while True:
    print(page)
    choice=input("""
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    """).upper()

    if choice =="I":
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
        page = len(custlist)-1
        print(page)

    elif choice == "C":
        if page >= 0:
            print("현재 페이지는 {}쪽 입니다".format(page+1))
            print(custlist[page])
        else:
            print("입력된 정보가 없습니다.")        
         
    elif choice == "P":
        if page <= 0:
            print("첫 번 째 페이지이므로, 이전 페이지 이동이 불가합니다.")
            print(page)
        else:
            page -= 1
            print("현재 페이지는 {}쪽 입니다".format(page+1))
            print(custlist[page])           

    elif choice == "N":
        if page >= len(custlist)-1:
            print("마지막 페이지이므로, 다음 페이지 이동이 불가합니다.")
            print(page)
        else:
            page += 1
            print("현재 페이지는 {}쪽 입니다".format(page+1))
            print(custlist[page])  

    elif choice == "U": 
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
                  
    elif choice == "D":
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

    elif choice == "Q":
        print("프로그램 종료")
        break
    else:
        print("잘못 입력 하셨습니다.")
```

