n = int(input())

if n == 1:
    print(1)
else:
    n -= 1
    layer = 1
    while True:
        if n - layer * 6 > 0:
            n -= layer * 6
            layer += 1
        else:
            break

    print(layer+1)
