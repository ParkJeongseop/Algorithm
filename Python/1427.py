n = input()

list = [n[i] for i in range(len(n))]

for i in range(0,len(list)-1):
    for j in range(i,len(list)):
        if list[i] < list[j]:
            list[i], list[j] = list[j], list[i]

print(''.join(map(str,list)))