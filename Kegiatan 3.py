Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Farah Husna Paramadina'
>>> NIM = 'L200183094'
>>> X = '1' +NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> X
'1094'
>>> ##NIM[7:] is 3 number from behind
>>> a
1094
>>> ##(' ') can be changed, so the string can be an integer
>>> b
22
>>> ##that is a length of character of Nama in string
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> a/b
49.72727272727273
>>> a//b
49
>>> #type(a) is integer
>>> #type(b) is integer
>>> ##the result of a/b is float
>>> ##the result of a//b is integer
>>> 10*(a-999)
950
>>> ## can calculated by mathematics function first(a-999) is(1094-999) = 95 than multiply with 10 so 95x10 = 950
>>> b**2
484
>>> ##that is mathemathic function b=22, so square of 22 is 484
>>> a%b
16
>>> ##that is mathematics function, 1094 : 22 = 49, 1094-49 = 16, and the modulus is 16
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> a/c
87.52
>>> ##the integer and float can be calculate
>>> a//c
87.0
>>> ##the integer andfloat can be calculate and the result is float
>>> a%c
6.5
>>> ##the modulus is 6.5
>>> c>b
False
>>> ## its false because 12.5 !> 22
>>> type(c>b)
<class 'bool'>
>>> ##bool is beetwen 'true' and 'false'
>>> a>b and b>c
True
>>> ##that is true
>>> a>1100 or b<10
False
>>> ##both of them is false
>>> 
