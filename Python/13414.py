k, l = map(int, input().split())
students = []

for i in range(l):
    temp = int(input())
    for j in range(len(students)):
        if students[j] == temp:
            del students[j]
            break
    students.append(temp)
    if len(students) > k:
        break

for i in range(k):
    print(students[i])