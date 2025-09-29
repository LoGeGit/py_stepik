countnum = 0
numsum = 0
firstnum = int(input())
secnum = int(input())
for i in range(firstnum,secnum+1):
    if i % 3 == 0:
        numsum += i
        countnum +=1

print(numsum / countnum)