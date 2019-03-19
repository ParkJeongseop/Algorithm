n, m = map(int, input().split())


def nm(list):
    if len(list) == 0:
        for i in range(n-m+1):
            nm([i+1])
    elif len(list) == m - 1:
        for i in range(list[-1]+1, n+1):
            print(*list, i)
    elif len(list) < m - 1:
        for i in range(list[-1]+1, n):
            list.append(i)
            nm(list)
            list.pop()
    else:
        print(*list)


nm([])