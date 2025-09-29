text = input()
arr = text.split()
arr.sort()
arr += ' '
num = 0
i = 0
while i in range(len(arr)-1):
    while arr[i+1] == arr[i]:
            num += 1
            i += 1

    if num > 0:
        num = 0 
        print(arr[i])
        i+=1
    i +=1