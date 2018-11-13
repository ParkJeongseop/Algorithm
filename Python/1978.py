input()
list = list(map(int, input().split()))

answer = 0
for i in list:
    ck = True
    for j in range(2,i):
        if i%j == 0:
            ck = False
    if i!=1 and ck:
        answer += 1
print(answer,end='')