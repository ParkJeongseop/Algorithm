n = int(input())

for i in range(n):
    print(" "*(n-i-1),end='')
    print("*"*(i+1),end='')
    if i+1 != n:
        print()