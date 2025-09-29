firstmult = int(input())
secmult = int(input())
firstnum = int( input())
secnum = int(input())
print(end = '\t')
for i in range(firstnum,secnum+1):
    print(i,end='\t')
print ()
for i in range(firstmult,secmult+1):
    print(i,end = '\t')
    for ii in range(firstnum,secnum+1):
        print (i*ii,end = '\t')
    print ()
        