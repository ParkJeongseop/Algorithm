n, k = map(int, input().split())
coin = []

for i in range(n):
    coin.append(int(input()))

answer = 0

for i in range(n-1, -1, -1):
    if k//coin[i] > 0:
        answer += k//coin[i]
        k %= coin[i]
print(answer)