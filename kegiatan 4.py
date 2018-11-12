Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Farah Husna Paramadina'
>>> NIM = 194
>>> Tinggi = 1.6
>>> Berat = 45
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> Aku
(2000, 45, 1.6, 194, 'Farah Husna Paramadina')
>>> type(Aku)
<class 'tuple'>
>>> its can called tuple because, using ()
SyntaxError: invalid syntax
>>> ##its can called tuple because, using ()
>>> Aku[0]
2000
>>> a = NIM%4
>>> Aku[a]
1.6
>>> ## the modulus in a is 2, so Aku[a], is 1.6 is Tinggi
>>> type(Aku[a])
<class 'float'>
>>> ##because decimal
>>> Aku[a:4]
(1.6, 194)
>>> type(Aku[4])
<class 'str'>
>>> ##Aku[4] is Nama so it is a string
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> ##error becaue tuple cant be changed
>>> 
>>> type (Data)
<class 'list'>
>>> type(Data[4])
<class 'str'>
>>> Data[4][5]
' '
>>> Data[4][a:6]
'rah '
>>> ##fourth data is Nama, and [a:6] is 'rah'
>>> ##'rah' in the fourth data
>>> Data[0] = 'ok'
>>> Data
['ok', 45, 1.6, 194, 'Farah Husna Paramadina']
>>> ##type list can be changed
>>> Data[-a]
194
>>> range(a)
range(0, 2)

>>> ##because range start from 0
