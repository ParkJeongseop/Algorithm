n = int(input())

for i in range(n-1):
    print(' ' * (n-i-1) + '*' * (2*i+1), end='')
    if i + 1 != n:
        print()

for i in range(n):
    print(' '*i + '*'*(2*n-2*i-1),end='')
    if i+1 != n:
        print()