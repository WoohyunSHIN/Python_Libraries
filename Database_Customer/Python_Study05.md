// Reference Book : [점프 투 파이썬](https://wikidocs.net/book/1)

// Written by WoohyunSHIN. I reconstitute the reference book as my style for studying. If you have question or I commit an infrigement of copyright, send me a mail <swh159@gmail.com> please thank you.

# Python

***

# 5. 정규표현식

> 정규표현식(Regular Expression) 이란 복잡한 문자열을 처리할 때 사용하는 기법으로, 문자열을 처리하는 모든 곳에서 사용된다. 다른 방식으로 "정규식" 이라고도 한다.
>
> 왜 필요한가 ? https://wikidocs.net/1642

```python
# case : 정규표현식을 모를경우
>>> data = """
>>> park 800905-1049118
>>> kim  700905-1059119
>>> """
>>> 
>>> result=[]
>>> for line in data.split("\n")
...     word_result[]
...     for word in line.split(" ")
...         if len(word)==14 and word[:6].isdigit() and word[7:].isdigit()
...             word = word[:6] + "-" + "*******"
...         word_result.append(word)
...     result.append(" ".join(word_result))
>>> print("\n".join(result))
park 800905-1049118
kim  700905-1059119 

# case : 정규식을 아는 경우
>>> data = """
>>> park 800905-1049118
>>> kim  700905-1059119
>>> """
>>> 
>>> pat = re.compile("\d{6}[-]\d{7}")
>>> print(pat.sub("\g<1>-*******",data))
park 800905-1049118
kim  700905-1059119 
```

https://wikidocs.net/4308

**[ ]** 대괄호 안과 밖이냐에 따라 의미가 달라지는 것이 많다. 예를 들어 "^" "." 

## X.X 정규식을 이용한 문자열 검색 

***

### X.X.X. match

match 는 **처음** 부터 정규식과 매치되는지 조사한다.



```python
>>> import re
>>> 
>>> p = re.compile('[a-z]+')
>>> # 소문자 1번이상 반복되는것

# case 1
>>> m = p.match("python")
>>> print(m)
match=('python')

# case 2
>>> m = p.match("Python") 
>>> print(m)
None

# case 3
>>> m = p.match("pythOn")
>>> print(m)
match=('pyth')

```



### x.x.x. search

문자열 전체를 검색하여 정규식과 매치되는지 조사한다.

```
>>> import re
>>> 
>>> p = re.compile('[a-z]+')
>>> # 소문자 1번이상 반복되는것

# case 1
>>> m = p.search("python")
>>> print(m)
match=('python')

# case 2
>>> m = p.search("3 pythOn")
>>> print(m)
match=('pyth')
```



### x.x.x. findall

```
>>> import re
>>> 
>>> p = re.compile('[a-z]+')
>>> # 소문자 1번이상 반복되는것

# case 1
>>> m = p.search("3 pythOn")
>>> print(m)
['pyth','n']
```



### x.x.x. finditer

```
>>> import re
>>> 
>>> p = re.compile('[a-z]+')
>>> # 소문자 1번이상 반복되는것

# case 1
>>> m = p.finditer("as3 pythOn")
>>> print(m)
<callable_iterator object at 0x102edc9e8>

# case 2
>>> m = p.finditer("as3 pythOn")
>>> print(m)
<re.Match object; span=(0, 2), match='as'>
<re.Match object; span=(4, 8), match='pyth'>
<re.Match object; span=(9, 10), match='n'>
```



### x.x.x. 이메일 정규식 만들기

```

```

