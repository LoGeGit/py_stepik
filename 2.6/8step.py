count = int(input())
i = 1
inp = 0
num = 0
if count <= 2:
    for i in range(count+1):
        if num == count:
            break
        for inp in range(i):
            if num == count:
                break
            print(i,end = ' ')
            num +=1
    
else:
    for i in range(count):
        if num == count:
            break
        for inp in range(i):
            if num == count:
                break
            print(i,end = ' ')
            num +=1
    