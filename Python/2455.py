answer = 0
status = 0

for i in range(4):
    a, b = map(int, input().split())
    status -= a
    status += b
    if status > answer:
        answer = status
print(answer)