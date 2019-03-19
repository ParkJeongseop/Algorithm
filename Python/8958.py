n = int(input())

for i in range(n):
    st = input()
    score = 0
    stack  = 0
    for j in range(len(st)):
        if st[j] == "O":
            stack += 1
            score += stack
        else:
            stack = 0
    print(score)