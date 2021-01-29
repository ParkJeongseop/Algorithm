def d(n):
    answer = n
    for i in range(len(str(n))):
        answer += int(str(n)[i])
    return answer

arr = set()

i = 1
while d(i) <= 15000:
    arr.add(d(i))
    i += 1


for i in range(1, 10001):
    if i not in arr:
        print(i)
