n, m = map(int, input().split())

def nm(list):
    if len(list) == 0:
        if len(list) == m-1:
            for i in range(1, n + 1):
                if i not in list:
                    print(*list, i)
        else:
            for i in range(n):
                nm([i+1])
    elif len(list) == m-1:
        for i in range(1, n+1):
            if i not in list:
                print(*list, i)
    elif len(list) < m-1:
        for i in range(1, n+1):
            if i not in list:
                list.append(i)
                nm(list)
                list.pop()

nm([])