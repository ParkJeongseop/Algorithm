n = int(input())
scores = map(int, input().split())
scores = sorted(scores)
sum = 0
for score in scores:
    sum += score/scores[-1]*100

print(sum/n)