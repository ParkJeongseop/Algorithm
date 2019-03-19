n = int(input())
answer = 1
while pow(answer, 2) != n-answer-1:
    answer += 1
print(answer)