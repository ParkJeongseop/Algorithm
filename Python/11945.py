n, m = map(int, input().split())

for i in range(n):
    st = input()
    for j in range(m):
        print(st[m-j-1],end='')
    print()