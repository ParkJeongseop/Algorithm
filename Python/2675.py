for i in range(int(input())):
    st = input().split()
    for j in range(len(st[1])):
        print(st[1][j]*int(st[0]), end='')
    print()