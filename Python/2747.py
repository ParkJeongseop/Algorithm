def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif temp[n] != 0:
        return temp[n]
    else:
        temp[n] = fibo(n-1) + fibo(n-2)
        return temp[n]
n = int(input())
temp = [0 for i in range(n+1)]
print(fibo(n),end='')