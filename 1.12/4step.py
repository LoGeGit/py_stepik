import math
form = input()
if form == 'прямоугольник':
    a = int(input())
    b = int(input())

    print(a*b)
elif form == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())

    p = (a + b + c) / 2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))

    print(s)

elif form == 'круг':
    r = int(input())
    
    print(3.14 * (r**2))
    

