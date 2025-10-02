arr = [0 for i in range(100)]

sum = 0
i = 1
num = int(input())
sum += num
arr[0] = num

while sum != 0:
    num = int(input())
    sum += num
    arr[i] = num
    i += 1
sum2 = 0
for inp in range(i):
    sum2 += arr[inp] * arr[inp]

print(sum2)