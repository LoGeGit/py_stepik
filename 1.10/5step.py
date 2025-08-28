mintime = int(input())
maxtime = int(input())
sleeptime = int(input())
if mintime<=sleeptime<=maxtime:
    print('Это нормально')
elif mintime>sleeptime :
    print('Недосып')
else:
    print('Пересып')
    
