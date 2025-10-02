text = input()
arr = text.split()
arr.sort()
countDubleNumber = 0
i = 0
while i in range(len(arr)-1):
    
    while (arr[i+1] == arr[i]) :
        countDubleNumber += 1
        i += 1
        if i == len(arr)-1:
            break

    if countDubleNumber > 0:
        print(arr[i])
    i +=1
    countDubleNumber = 0 
