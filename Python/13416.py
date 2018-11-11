n = int(input())

for i in range(n):
    days = int(input())
    sum = 0
    for day in range(days):
        data = [int(i) for i in input().split()]
        sum += max(data) if max(data)>0 else 0
    print(sum,end='')
    if not i+1 == n:
        print()