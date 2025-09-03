num = int(input())

firstsum = (num // 100000) + (num % 100000 // 10000) + (num % 10000 // 1000)
secsum = (num % 10) + (num % 100 // 10 ) + (num  % 1000 // 100)

if firstsum == secsum:
    print('Счастливый')
else:
    print('Обычный')