h, m = map(int, input().split())
if m < 45:
    h -= 1
    m += 15
else:
    m -= 45
if h < 0:
    h += 24
print(h, m)
