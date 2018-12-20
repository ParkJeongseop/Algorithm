number = int(input())
n = number

n = int(str(n%10) + str((n%10 + n//10)%10))
answer = 1

while n != number:
    n = int(str(n % 10) + str((n % 10 + n // 10) % 10))
    answer += 1

print(answer)