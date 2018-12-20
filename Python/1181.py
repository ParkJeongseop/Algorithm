n = int(input())
words = []
for i in range(n):
    words.append(input())

for i in range(n):
    for j in range(n-1,i+1,-1):
        if