n,m = map(int, input().split())
list = [i+1 for i in range(n)]

print("<",end='')

location = 0
for i in range(1,n+1):
    location += m
    location%=len(list)
    print(list[location-1],end='')
    del list[location-1]
    if i == n:
        print(">",end='')
    else:
        location-=1
        print(", ",end='')