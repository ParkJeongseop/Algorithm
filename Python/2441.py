n = int(input())

for i in range(n):
    print(" "*i,end='')
    print("*"*(n-i),end='')
    if i+1 != n:
        print()