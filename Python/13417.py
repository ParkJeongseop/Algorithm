n = int(input())

for i in range(n):
    input()
    word = input().split()
    answer = word[0]
    for k in range(1, len(word)):
        if ascii(word[k]) <= ascii(answer[0]):
            answer = word[k] + answer
        else:
            answer += word[k]
    print(answer, end='')
    if not i+1 == n:
        print()