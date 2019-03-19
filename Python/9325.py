for i in range(int(input())):
    answer = 0
    answer += int(input())
    for j in range(int(input())):
        q, p = map(int, input().split())
        answer += q*p
    print(answer)