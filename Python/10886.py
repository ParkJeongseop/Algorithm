n = int(input())
count = 0
for i in range(n):
    count += int(input())
print("Junhee is " + (""if count > (n-count) else "not ") + "cute!")