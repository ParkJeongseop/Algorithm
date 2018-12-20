max = 1000000
list = [0 for i in range(max*2)]

n = int(input())

for i in range(n):
    list[int(input())+max] = 1

count = 0
for i in range(max*2):
    if list[i] == 1:
        print(i-max, end='')
        count += 1
        if count == n:
            break
        else:
            print()