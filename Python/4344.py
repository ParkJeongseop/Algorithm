c = int(input())

for i in range(c):
    temp = list(map(int, input().split()))
    sum = 0
    for j in range(temp[0]):
        sum += temp[1+j]
    aver = sum/temp[0]
    count = 0
    for j in range(temp[0]):
        if temp[1+j] > aver:
            count += 1
    print('%0.3f' % round(count/temp[0]*100, 3) + "%")