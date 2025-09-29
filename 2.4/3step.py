genom = input()
count = genom.lower().count('c') + genom.lower().count('g')
print(count / len(genom) *100)