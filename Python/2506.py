n = int(input())
scores = input().split()
scores = [int(i) for i in scores]

answer = 0
count = 0
for i in scores:
    if i == 1:
        count += 1
        answer += count
    else:
        count = 0
print(answer)