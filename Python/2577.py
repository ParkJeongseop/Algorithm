num = 1
for i in range(3):
    num *= int(input())

count = [0 for i in range(10)]

for i in range(len(str(num))):
    count[int(str(num)[i])] += 1

for i in count:
    print(i)