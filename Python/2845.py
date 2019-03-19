l, p = map(int,input().split())
news = input().split()
people = l*p
for i in news:
    print(str(int(i)-people),end=' ')