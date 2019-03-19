n = int(input())
p = sorted(map(int, input().split()))

answer = 0
for i in range(len(p)):
    for j in range(i+1):
        answer += p[j]

print(str(answer))