
Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> a=[]
>>> b=[1,2,3]
>>> c=['Life','is','too','short']
>>> d=[1,2,'Life','short']
>>> e=[1,2,['Life','is']]
>>>
>>> #p.30 리스트의 indexing
>>> a=[1,2,3]
>>> a[0]
1
>>> a[-1]
3
>>> a=[1,2,3,['a','b','c']]
>>> a[-1]
['a', 'b', 'c']
>>> a[3]
['a', 'b', 'c']
>>> a[-1][0]
'a'
>>> a[-1][1]
'b'
>>> a[-1][2]
'c'
>>>
>>> #p.31 리스트의 slicing
>>> a=[1,2,3,4,5]
>>> a=-[0:2]
  File "<stdin>", line 1
    a=-[0:2]
         ^
SyntaxError: invalid syntax
>>> a=[0:2]
  File "<stdin>", line 1
    a=[0:2]
        ^
SyntaxError: invalid syntax
>>> a[0:2]
[1, 2]
>>> b=a[:2]
>>> c=a[2:]
>>> b
[1, 2]
>>> v
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'v' is not defined
>>> c
[3, 4, 5]
>>>
>>> a=[1,2,3,['a','b','c'],4,5]
>>> a[2:5]
[3, ['a', 'b', 'c'], 4]
>>> a[3][:2]
['a', 'b']
>>>
>>> #p.32 리스트 연산하기
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> a+b
[1, 2, 3, 4, 5, 6]
>>> a=[1,2,3]
>>> a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> a=[1,2,3]
>>> len(a)
3
>>>
>>> #p.33 리스트 수정/삭제
>>> a=[1,2,3]
>>> a[2]=4
>>> a
[1, 2, 4]
>>> a=[1,2,3]
>>> del a[1]
>>> a
[1, 3]
>>> a=[1,2,3,4,5]
>>> del a[2:]
>>> a
[1, 2]
>>>
>>> #p.34 리스트 관련 함수
>>> a=[1,2,3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> a.append([5,6])
>>> a
[1, 2, 3, 4, [5, 6]]
>>> a=[1,4,3,2]
>>> a.sort()
>>> a
[1, 2, 3, 4]
>>> a=['a','c','b']
>>> a.sort()
>>> a
['a', 'b', 'c']
>>> a=['a','c','b']
>>> a.reverse()
>>> a
['b', 'c', 'a']
>>> a=[1,2,3]
>>> a.index(3)
2
>>> a.index(1)
0
>>> a=[1,2,3]
>>> a.insert(0,4)
>>> a
[4, 1, 2, 3]
>>> a.insert(3,5)
>>> a
[4, 1, 2, 5, 3]
>>> a=[1,2,3,1,2,3]
>>> a.remove(3)
>>> a
[1, 2, 1, 2, 3]
>>> a=[1,2,3]
>>> a.pop()
3
>>> a
[1, 2]
>>> a=[1,2,3]
>>> a.pop(1)
2
>>> a
[1, 3]
>>> a=[1,2,3,1]
>>> a.count(1)
2
>>> a=[1,2,3]
>>> a.extend([4,5])
>>> a
[1, 2, 3, 4, 5]
>>> b=[6,7]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6, 7]
>>>
>>> #p.39 튜플 다루기
>>> t1=(1,2,'a','b')
>>> t1[0]
1
>>> t1[3]
'b'
>>> t1=(1,2,'a','b')
>>> t1[1:]
(2, 'a', 'b')
>>> t1=(1,2,'a','b')
>>> t2=(3,4)
>>> t3=t1+t2
>>> t3
(1, 2, 'a', 'b', 3, 4)
>>> t2=(3,4)
>>> t3=t2*3
>>> t3
(3, 4, 3, 4, 3, 4)
>>> t1=(1,2,'a','b')
>>> len(t1)
4
>>>
>>> #p.42 딕셔너리 item 추가/삭제
>>> a={1:'a'}
>>> a[2]='b'
>>> a
{1: 'a', 2: 'b'}
>>> a['name']='pey'
>>> a
{1: 'a', 2: 'b', 'name': 'pey'}
>>> a[3]=[1,2,3]
>>> a
{1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
>>>
>>> del a[1]
>>> a
{2: 'b', 'name': 'pey', 3: [1, 2, 3]}
>>>
>>> #p.43 딕셔너리의 사용
>>> grade={'pey':10, 'julliet':99}
>>> grade['pey']
10
>>> grade['julliet']
99
>>> a={1:'a',2:'b'}
>>> a[1]
'a'
>>> a[2]
'b'
>>> a['a']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'a'
>>> a={'a':1, 'b':2}
>>> a['a']
1
>>> a['b']
2
>>>
>>> a=[1:'a', 1:'b']
  File "<stdin>", line 1
    a=[1:'a', 1:'b']
        ^
SyntaxError: invalid syntax
>>> a
{'a': 1, 'b': 2}
>>>
>>> #p.44 딕셔너리 관련 함수
>>> a={'name':'pey', 'phone':'010-9999-4561', 'birth':'1118'}
>>> a.keys()
dict_keys(['name', 'phone', 'birth'])
>>> list(a.keys())
['name', 'phone', 'birth']
>>> for k in a.keys():
... print(k)
  File "<stdin>", line 2
    print(k)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>>
>>> a.values()
dict_values(['pey', '010-9999-4561', '1118'])
>>> dict_values(['pey', '010-9999-4561', '1118'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dict_values' is not defined
>>> for k in a.keys():
... print(k)
  File "<stdin>", line 2
    print(k)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> a.items()
dict_items([('name', 'pey'), ('phone', '010-9999-4561'), ('birth', '1118')])
>>> a.clear()
>>> a
{}
>>> a={'name':'pey', 'phone':'010-9999-4561', 'birth':'1118'}
>>> a.get('name')
'pey'
>>> a.get('phone')
'010-9999-4561'
>>> a.get('nokey', 'foo')
'foo'
>>> print(a.get('nokey'))
None
>>> print(a['nokey'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'nokey'
>>> 'name' in a
True
>>> 'email' in b
False
>>>
>>> #p.47 집합 자료형의 특징
>>> s1=set([1,2,3])
>>> s1
{1, 2, 3}
>>> s2=set("Hello")
>>> s2
{'l', 'H', 'o', 'e'}
>>> s1=set([1,2,3])
>>> l1=list(s1)
>>> l1
[1, 2, 3]
>>> l1[0]
1
>>> t1=tuple(s1)
>>> t1
(1, 2, 3)
>>> t1[0]
1
>>>
