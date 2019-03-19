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
            if i >= list[-1]:
                print(*list, i)
    elif len(list) < m-1:
        for i in n:
            if i >= list[-1]:
                list.append(i)
                nm(list)
                list.pop()

nm([])