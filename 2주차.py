#p.13 문자열 슬라이싱
>>> a="Life is too short, You need Python"
>>> a[0:4]
'Life'
>>> a[5:7]
'is'
>>> a[12:17]
'short'
>>> a[:17]
'Life is too short'
>>> a[19:-7]
'You need'
>>> a[:]
'Life is too short, You need Python'
>>>
>>> #p.14 문자열 단어 치환
>>> a="Pithon"
>>> a[1]
'i'
>>> a[1]='y'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> '문자열은 변경 불변이기 때문에 오류가 난다고 뜸'
'문자열은 변경 불변이기 때문에 오류가 난다고 뜸'

>>> a="Pithon"
>>> a[:1]
'P'
>>> a[2:]
'thon'
>>> a[:1]+'y'+a[2:]
'Python'
>>>
>>> #p.15 문자열 포맷팅
>>> "I eat %d apples."%3
'I eat 3 apples.'
>>> numver=3
>>> "I eat %d apples."%numver
'I eat 3 apples.'
>>>
>>> "I eat %s apples."%"five"
'I eat five apples.'
>>> number=10
>>> day="three"
>>> "I ate %d apples. so I was sick for %s days."%(number, day)
'I ate 10 apples. so I was sick for three days.'
>>>
>>> #p.17 문자열 포맷 코드에 숫자 이용
>>> "%10s"%"hi"
'        hi'
>>> "%-10sjane."%"hi"
'hi        jane.'
>>> "%0.4f" % 3.42134234
'3.4213'
>>> "%.4f"%3.42134234
'3.4213'
>>> "%10.4f"%3.42134234
'    3.4213'
>>>
>>> #p.19 format함수를 사용한 포매팅
>>> "I eat {0} apples.".format(3)
'I eat 3 apples.'
>>> "I eat {0} apples.".format("five")
'I eat five apples.'
>>> number=3
>>> "I eat {0} apples.".format(number)
'I eat 3 apples.'
>>>
>>> #p.20 format 함수를 사용한 포매팅-cont
>>> number=10
>>> day="three"
>>> "I ate {0} apples. so I was sick for {1} days.".format(number,day)
'I ate 10 apples. so I was sick for three days.'

>>> "I ate {number} apples. so I was sick for {day} days.".format(number=11,day=4)
'I ate 11 apples. so I was sick for 4 days.'

>>>  "I ate {0} apples. so I was sick for {day} days.".format(9,day=15)
  File "<stdin>", line 1
    "I ate {0} apples. so I was sick for {day} days.".format(9,day=15)
IndentationError: unexpected indent
>>>  "I ate {0} apples. so I was sick for {day} days.".format(10,day=3)
  File "<stdin>", line 1
    "I ate {0} apples. so I was sick for {day} days.".format(10,day=3)
IndentationError: unexpected indent
>>>
>>> "{0:<10}".format("hi")
'hi        '
>>> "{0:>10}".format("hi")
'        hi'
>>> "{0:^10}".format("hi")
'    hi    '
>>> "{0:^5}".format("hi")
' hi  '
>>> "{0:=^10}".format("hi")
'====hi===='
>>> "{0:!<10}".format("hi")
'hi!!!!!!!!'
>>>
>>> y=3.141592
>>> "{0:0.4f}".format(y)
'3.1416'
>>> "{0:10.4f}".format(y)
'    3.1416'
>>> "{{and}}".format()
'{and}'
>>>
>>> #p.23 f문자열 포매팅
>>> name='홍길동'
>>> age=30
>>> f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
>>>
>>> age=30
>>> f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'
>>>
>>> f'{"hi":<10}' #왼쪽 정렬
'hi        '
>>> f'{"hi":>10}' #오른쪽 정렬
'        hi'
>>> f'{"hi":^10}' #가운데 정렬
'    hi    '
>>> f'{"hi":=^10}'
'====hi===='
>>> f'{"hi":!<10}' #왼쪽 정렬하고 ! 문자로 공백 채우기
'hi!!!!!!!!'
>>>
>>> y=3.421548
>>> f'{y:0.4f}'
'3.4215'
>>> f'{y:10.4f}'
'    3.4215'
>>>
>>> f'{{and}}'
'{and}'
>>>
