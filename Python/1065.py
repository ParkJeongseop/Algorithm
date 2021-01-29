def check(n):
    if n < 100:
        return True
    
    a = int(str(n)[0]) - int(str(n)[1])
    for i in range(len(str(n))-1):
        if int(str(n)[i]) - int(str(n)[i+1]) != a:
            return False
    return True

n = int(input())
answer = 0

for i in range(1,n+1):
    if check(i):
        answer += 1

print(answer)
