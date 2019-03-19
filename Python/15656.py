n_num, m = map(int, input().split())
n = map(int, input().split())
n = sorted(n)


def nm(list):
    if len(list) == 0:
        for i in n:
            if len(list) == m-1:
                print(i)
            else:
                nm([i])
    elif len(list) == m-1:
        for i in n:
            print(*list, i)
    elif len(list) < m-1:
        for i in n:
            list.append(i)
            nm(list)
            list.pop()


nm([])