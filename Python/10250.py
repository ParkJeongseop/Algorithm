t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    y = n%h
    x = n//h+1
    if y == 0:
        y = h
        x -= 1
    print(100*y+x)
