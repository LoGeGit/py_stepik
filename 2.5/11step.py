text = input()
arr = text.split()
sum = 0
ans = ''
for i in range(len(arr)):
    if i+1 == len(arr):
        sum = int(arr[i-1] + int(arr[0]))
        ans += str(sum) + ' '
    else:
        sum = int(arr[i-1])+ int(arr[i+1])   
        ans += str(sum) + ' '
        sum = 0


print(ans)