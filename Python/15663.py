n_num, m = map(int, input().split())
n = map(int, input().split())
n = sorted(n)
used = []

def nm(list):
    if len(list) == 0:
        for i in n:
            if len(list) == m-1:
                if i not in used:
                    print(i)
                    used.append(i)
            else:
                nm([i])
    elif len(list) == m-1:
        for i in n:
            if i not in list:
                list.append(i)
                if ' '.join(map(str, list)) not in used:
                    print(*list)
                    used.append(' '.join(map(str, list)))
                list.pop()
    elif len(list) < m-1:
        for i in n:
            if i not in list:
                list.append(i)
                nm(list)
                list.pop()

nm([])