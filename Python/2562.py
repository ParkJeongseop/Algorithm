max = 0
id = 0
for i in range(9):
    number = int(input())
    if number > max:
        max = number
        id = i+1
print(max)
print(id)