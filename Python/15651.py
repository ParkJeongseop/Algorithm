n, m = map(int, input().split())

def nm(list):
    if len(list) == 0:
        if len(list) == m-1:
            for i in range(1, n + 1):
                print(i)
        else:
            for i in range(n):
                nm([i+1])
    elif len(list) == m-1:
        for i in range(n):
            print(*list, i+1)
    elif len(list) < m-1:
        for i in range(n):
            list.append(i+1)
            nm(list)
            list.pop()
nm([])