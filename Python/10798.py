board = []
for i in range(5):
    board.append(input())
answer = ""

for i in range(15):
    for j in range(5):
        if len(board[j]) > i:
            answer += board[j][i]
print(answer)