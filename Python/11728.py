len_n, len_m = map(int, input().split())
n = input().split()
m = input().split()
n = [int(i) for i in n]
m = [int(i) for i in m]
p_n, p_m = 0, 0
answer = []

while not (p_n == len_n and p_m == len_m):
    if p_n == len_n:
        answer.append(m[p_m])
        p_m += 1
    elif p_m == len_m:
        answer.append(n[p_n])
        p_n += 1
    else:
        if n[p_n] == m[p_m]:
            answer.append(n[p_n])
            p_n += 1
            p_m += 1
        elif n[p_n] < m[p_m]:
            answer.append(n[p_n])
            p_n += 1
        else:
            answer.append(m[p_m])
            p_m += 1

answer = [str(i) for i in answer]
print(' '.join(answer))