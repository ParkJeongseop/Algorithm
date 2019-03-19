import math
m = int(input())
n = int(input())

full_power = []
for i in range(math.ceil(pow(m, 0.5)), int(pow(n, 0.5))+1):
    full_power.append(i**2)

if len(full_power)>0:
    sum = 0
    min = full_power[0]

    for i in full_power:
        sum += i
        if i<min:
            min = i

    print(sum)
    print(min)
else:
    print("-1")
