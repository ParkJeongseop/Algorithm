answer = 0
for i in range(5):
    score = int(input())
    if score > 40:
        answer += score
    else:
        answer += 40
print(int(answer/5))