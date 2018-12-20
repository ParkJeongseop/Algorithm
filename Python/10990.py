n = int(input())

for i in range(n):
    print(" "*(n-1-i) + "*",end='')
    if i!=0:
        print(" "*(2*i-1) +"*")
    else:
        print()