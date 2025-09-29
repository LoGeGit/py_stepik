text = input()
arr = text.split()
arr.sort()
conutDubleNumber = 0
i = 0
while i in range(len(arr)-1):
    while arr[i+1] == arr[i]:
        conutDubleNumber += 1
        i += 1

    if conutDubleNumber > 0:
        print(arr[i])
    i +=1
    conutDubleNumber = 0 
