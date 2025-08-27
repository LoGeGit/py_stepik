timeforsleep = int(input())
hoursleep = int(input())
minutesleep = int(input())

wholeMinSleep = hoursleep * 60 + minutesleep + timeforsleep
hourup = wholeMinSleep // 60
minutesup = wholeMinSleep % 60


print(hourup)
print(minutesup)