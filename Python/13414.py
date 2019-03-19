k, l = map(int, input().split())
students = []

for i in range(l):
    students.append(input())

filt = set(students)

last = []
for i in range(l-1, -1, -1):
    if not {students[i]}.issubset(filt):
        last.append(students[i])

print(students)
print(last)
for i in range(len(last)-1, len(last)-k-1, -1):
    print(last[i])

#
# for i in range(l):
#     temp = int(input())
#     for j in range(len(students)):
#         if students[j] == temp:
#             del students[j]
#             break
#     students.append(temp)
#     if len(students) > k:
#         break
#
# for i in range(k):
#     print(students[i])