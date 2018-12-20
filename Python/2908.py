a, b = map(str, input().split())
a, b = a[2]+a[1]+a[0], b[2]+b[1]+b[0]
print(a if int(a)>int(b) else b)