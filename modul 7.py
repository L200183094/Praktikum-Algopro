d = {'Triangle' : 'A = 0.5*a*t', 'Square' : 'A = s**2', 'Rectangle' : 'A = p*l', 'Circle' : 'A = pi*r**2', 'Parallelogram' : 'A = a*t'}
print('''
No |    Nama Bangun    | Rumus Luas
---|-------------------|--------------
1  |  Triangle         | %s
2  |  Square           | %s
3  |  Rectangle        | %s
4  |  Circle           | %s
5  |  Parallelogram    | %s
'''%(d['Triangle'],d['Square'],d['Rectangle'],d['Circle'],d['Parallelogram']))

#activity 2 password by : farah husna
n = 0
while n<3:
    x = input ('insert password : ')
    n = n+1
    if x == 'farah':
        print ('login succeeded')
        n = 3
    if x != 'farah':
        if n == 3:
            print('sorry, you have tried 3 times. you can not login')
        else:
            print('sorry, your password is wrong')

#activity 3 . congratulation. by : farah husna
x = ('morning', 'noon', 'afternoon', 'evening', 'night')
y = input('what is your name? :')
t = float(input('what time is it now? (format 24 jam) :'))
if t >= 1.00 and t<= 09.59:
    t=x[0]
elif t >= 10.00 and t <= 11.59:
    t=x[1]
elif t >= 12.00 and t <= 14.59:
     t=x[2]
elif t >= 15.00 and t <= 17.59:
    t=x[3]
elif t >= 18.00 and t <=24.59:
    t=x[4]

print ('''Good %s %s '''%(t,y))
