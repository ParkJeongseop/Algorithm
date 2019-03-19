list = input().split()
list = [int(i) for i in list]

while not list == [1, 2, 3, 4, 5]:
    for i in range(4):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            tmp = [str(i) for i in list]
            print(' '.join(tmp))