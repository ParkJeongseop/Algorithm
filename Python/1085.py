x, y, w, h = map(int, input().split())

print(abs(x-w)if abs(x-w) < abs(y-h) else abs(y-h))