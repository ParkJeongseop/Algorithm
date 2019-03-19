n = int(input())

ischeck = False
for i in range(0, n+1):
    if pow(2, i) == n:
        print("1")
        ischeck = True
        break

if not ischeck:
    print("0")