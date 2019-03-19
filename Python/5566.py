answer = 0
location = 1

n, m = map(int, input().split())
board = []
dice = []
for i in range(n):
    board.append(int(input()))
for i in range(m):
    dice.append(int(input()))

while True:
    answer += 1
    location += dice[answer-1]
    if location >= n:
        break
    location += board[location-1]
    if location >= n:
        break

print(answer)