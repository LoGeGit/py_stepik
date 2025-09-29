firststr = input()+' '

count = 1
index = 0
while index < len(firststr)-1:
    while firststr[index+1] == firststr[index]:
        count +=1
        index +=1
    print(firststr[index] + str(count),end = '')
    count = 1
    index+=1
