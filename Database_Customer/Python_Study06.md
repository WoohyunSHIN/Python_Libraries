// Reference Book : [점프 투 파이썬](https://wikidocs.net/book/1)

// Written by WoohyunSHIN. I reconstitute the reference book as my style for studying. If you have question or I commit an infrigement of copyright, send me a mail <swh159@gmail.com> please thank you.

# Python

***

# 6. 클래스

> ​	클래스는 도대체 왜 필요한가 ? 클래스는 설계도이다. 영어 대문자로 시작하는 것을 약속으로 한다.
>
> ​	먼저 클래스는 지금까지 공부한 함수나 자료형처럼 프로그램 작성을 위해 꼭 필요한 요소는 아니다 하지만 프로그램 작성시 클래스를 적재적소에 이요하면 프로그래머가 얻을 수 있는 이득이 많다. 예를들어 3+7=10 을 계산하여 10이라는 값을 어딘가에 저장을 해놓고 +3 만 하면 13이라는 값을 보여준다. 즉 **계산기는 이전에 계산된 결과값을 항당 메모리 어딘가에 저장하고 있어야한다.**

```python
# 간단한 기능 없는 class 만들기
>>> class Cookie:
>>> 	pass
>>>
# a와 b 라는 Cookie 클래스의 인스턴스를 만들었다.
# a&b는 class Cookie 의 주소값을 담고있다. 
>>> a = Cookie()
>>> b = Cookie()

>>> print(type(a))
<class '__main__.Cookie'>
```



***

## 6.1. 클래스와 (객체, 인스턴스)

> ​	**클래스(class)**란 똑같은 무엇인가를 계속해서 만들어낼 수있는 설계 도면 같은 것이고, **객체(object)**란 클래스에 의해 만들어진 피조물을 뜻한다. 또한 이러한 객체별로 독립적인 성격을 갖는다.
>
> ​	 **인스턴스**란 클래스에 의해서 만들어진 객체를 인스턴스라고도 한다. 그렇다면 객체와 인스턴스의 차이는 무엇일까? 이렇게 생각해 보자. a = Cookie() 이렇게 만들어진 a는 객체이다. 그리고 a라는 객체는 Cookie의 인스턴스이다. 즉, 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용된다. 즉, "a는 인스턴스" 보다는 "a는 객체"라는 표현이 어울리며, "a는 Cookie의 객체" 보다는 "a는 Cookie의 인스턴스"라는 표현이 훨씬 잘 어울린다.

## 6.2. 사칙연산 클래스 만들기

> 클래스는 무작정 만들기 보다는 클래스에 의해 만들어진 객체를 중심으로 어떤 식으로 동작하게 할 것인지 미리 구상을 한 후에 생각했던 것들을 하나씩 해결하면서 완성해 나가는 것이 좋다.

**IMPORTANT**

1. **self**는 변수에 해당 클래스의 주소값을 반환해주는 역활을 한다. 또한 혼자서 돌아가는 인자인데 class에서 함수(=메서드)를 만들때 python에서는 꼭 선언을 해줘야한다. 하지만 사용할 때는 self는 없는것 처럼 사용한다.
2. self가 붙은 first는 class 안에 내가 가지고 쓸수 있는 first 라는 뜻이다 마치, Java 의 getter-setter중 setter 의 역활을 하는 것이다.
3. python에서는 first와 second를 class안에서 변수 선언을 해줄 필요가 없다. Java는 꼭 해야한다.

```python
>>> class FourCal:
... 	def setdata(self,first,second):
... 		self.first = first 
... 		self.second = second

# setdata 라는 method를 사용해서 데이터를 넣는 경우
>>> c = FourCal()
>>> c.setdata(4,2)
>>> print(c.first)
>>> print(c.second)
4
2

# "." 을 이용하여 클래스안에 first에 값을 집어넣는 경우
>>> c.first = 10
>>> c.second = 20
>>> print(c.first)
>>> print(c.second)
10
20
```



id 라는 함수는 변수의 주소값을 반환하는 함수이다.

```python
>>> class FourCal:
... 	def setdata(self,first,second):
... 		self.first = first 
... 		self.second = second

>>> d=FourCal()
>>> d.setdata(3,4)
>>> print(id(d))
>>> print(id(d.first))
>>> print(id(d.second))
4334889448
4313709808
4313709840
```



더하기 기능 만들기

```python
# 2개만 받아서
>>> class FourCal:
>>> 
...     def setdata(self,first,second):
        self.first =first
        self.second = second

    def add(self):
        result=self.first + self.second
        return result
>>> 
>>> a = FourCal()
>>> a.setdata(10,20)
>>> 
>>> sumresult = a.add()
>>> print(sumresult)
30

# 원하는 갯수를 받아서
>>> class FourCal:
>>> 
...     def setdata(self,*args):
...         self.list = args
... 
...     def add(self):
...         result=0
...         for i in range(0,len(self.list)):
...             result += self.list[i]
...         return result
... 
>>> a = FourCal()
>>> a.setdata(1,2,3,4,5,6,7,8,9)
>>> print(a.add())
45
```



## 6.3. 계산기를 만들어 보자

```python
>>> class FourCal
...   def setdata(self, first, second):
...     self.first = first
...     self.second = second
...   def add(self):
...     result = self.first + self.second
...     return result
...   def mul(self):
...     result = self.first * self.second
...     return result
...   def sub(self):
...     result = self.first - self.second
...     return result
...   def div(self):
...     result = self.first / self.second
...     return result

```

***

## 6.4. 생성자 (Constructor)

> 생성자란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다. 마치 리눅스의 /.skel 과 같이 처음 객체 생성할때 부여하는 초기값 들을 뜻한다.

```python
생성자는 __init__ 이라는 이름을 붙여서 만들고 사용한다.
```

```python
>>> class FourCal
>>>
... 	def __init__(self,first=0,second=0)
... 		self.first = first
... 		self.second = second
...
...   def setdata(self, first, second):
...     self.first = first
...     self.second = second
...
...   def add(self):
...     result = self.first + self.second
...     return result
>>>
>>> c=FourCal()
>>> print(c.add())
0 
# 왜냐하면 위에서 __init__ 값을 (0,0) 을 초기값으로 잡아 놓았기 때문이다.

```

***

## 6.5. 클래스의 상속(Inheritance)

> 파이썬에서 상속이란 개념은 현업에서 많이 사용하지 않는다. 파이썬 프로그래밍을 하면 상속을 어떻게 이용하는지에 대한 것만 알면 된다. 부모클래스로 부터 물려 받는 특징들을 뜻한다.
>
> 앞서 구현한 FourCal 클래스는 이미 만들어 놓았다고 가정한다. 여기에 a^b의 개념을 추가하고 싶다. 이러한 경우 어떻게 하는가 ?

```python
>>> class MoreFourCal(FourCal)
...		def pow(self)
... 		result = self.first ** self.second
... 		return result
```



## 6.6. 오버라이딩

> 파이썬에서는 오버로딩이라는 개념 자체가 Java와는 달리 필요하지 않다. 왜냐하면 init 를 사용하여 초기화할 때 값을 주면 되기 때문에 필요 없다.

> **오버라이딩**은 상속관계에서 나오는 개념이다. 부모의 특성을 물려받은 것을 **리모델링** 해서 사용하는 경우를 뜻한다. 아래의 내용은 앞서 구현한 FourCal 클래스는 이미 만들어 놓았다고 가정한다. 즉, 부모(=FourCal)가 만들어 놓은 method **div** 를 보완을 해서 사용하는 경우를 말한다.

```python
>>> class SafeFourCal(FourCal)
... 	def div(self):
... 		if self.second == 0:
... 			return 0
... 		else:
... 			return self.first/self.second
>>> c=FourCal(5,0)
>>> print(c.div())
Error: division by zero
  
>>> d=SafeFourCal(5,0)
>>> print(d.div())
0
```

***

## 6.7. 클래스 변수

> 클래스 변수인지 인스턴스 변수인지  

```python
>>> class M:
...     class_V =0
>>> 
>>> a=M()
>>> b=M()
>>> print(a.class_V)
>>> print(b.class_V)
0
0

>>> M.class_V=5
>>> print(a.class_V)
>>> print(b.class_V)
5
5

>>> a.class_V=6
>>> print(a.class_V)
>>> print(b.class_V)
6
5

```



##6.8. 고객관리 프로그램(DB_class)

> 콘솔형 고객 정보 관리 시스템 구축

```python
import re

class Customer:
    custlist=[]
    page = -1

    def insertData(self):
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
            for i in self.custlist:
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
        self.custlist.append(customer)
        global page
        page = len(self.custlist)-1 

    def curSearch(self):
        global page
        if page >= 0:
            print("현재 페이지는 {}쪽 입니다".format(page+1))
            print(self.custlist[page])
        else:
            print("입력된 정보가 없습니다.")   

    def preSearch(self):
        global page
        if page <= 0:
            print("첫 번 째 페이지이므로, 이전 페이지 이동이 불가합니다.")
            print(page)
        else:
            page -= 1
            print("현재 페이지는 {}쪽 입니다".format(page+1))
            print(self.custlist[page])  
        
    def nextSearch(self):
        global page
        if page >= len(self.custlist)-1:
            print("마지막 페이지이므로, 다음 페이지 이동이 불가합니다.")
            print(page)
        else:
            page += 1
            print("현재 페이지는 {}쪽 입니다".format(page+1))
            print(self.custlist[page])   
        
    def deleteData(self):
        global page
        delok=0
        check_email = input("삭제을 원하는 데이터의 이메일을 입력하세요 : ")
        
        for i in range(0,len(self.custlist)) :
            if check_email == self.custlist[i]["email"]:
                print("{} 고객님의 정보가 삭제되었습니다.".format(self.custlist[i]["name"]))
                del self.custlist[i]
                print(self.custlist)
                page=len(self.custlist)-1
                delok=1
                break

        if delok == 0:
            print("등록되지 않은 이메일입니다.")  

    def updateData(self):
        while True:
            check_email = input("수정을 원하는 데이터의 이메일을 입력하세요 : ")
            idx = -1

            for i in range(0,len(self.custlist)):
                if check_email==self.custlist[i]["email"]:
                    idk = i

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
                    self.custlist[idk]['name']=input("name =")
                    break
                elif select == 2:
                    while True:
                        self.custlist[idk]["sex"] = input("sex = ")
                        self.custlist[idk]['sex']=self.custlist[idk]['sex'].upper()
                        if self.custlist[idk]["sex"] in ("F","M"):
                            break
                    break
                elif select == 3:
                    while True:
                        self.custlist[idk]["birthyear"] = input("birthyear = ")
                        if len(self.custlist[idk]["birthyear"])==4 and self.custlist[idk]["birthyear"].isdigit():
                            break
                    break
                elif select == 4:
                    break
                else:
                    print("다시입력하시오")            
            break

    def firstinput(self):
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
            return choice

    def exe(self,choice):
        if choice=="I":
            self.insertData()
        elif choice=="C":
            self.curSearch()
        elif choice=="P":
            self.preSearch()
        elif choice=="N":
            self.nextSearch()
        elif choice=="U":
            self.updateData()
        elif choice=="D":
            self.deleteData()
        elif choice=="Q":
            quit()

    def __init__(self):
        while True:
            self.exe(self.firstinput())

Customer()

```

