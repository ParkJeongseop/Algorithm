n = int(input())

for i in range(n):
    print(' '*i + '*'*(2*n-2*i-1),end='')
    if i+1 != n:
        print()