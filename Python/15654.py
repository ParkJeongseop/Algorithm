n_num, m = map(int, input().split())
n = map(int, input().split())
n = sorted(n)


def nm(list):
    if len(list) == 0:
        if len(list) == m-1:
            for i in n:
                if i not in list:
                    print(i)
        else:
            for i in n:
                nm([i])
    elif len(list) == m-1:
        for i in n:
            if i not in list:
                print(*list, i)
    elif len(list) < m-1:
        for i in n:
            if i not in list:
                list.append(i)
                nm(list)
                list.pop()


nm([])