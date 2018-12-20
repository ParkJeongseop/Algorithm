for i in range(3):
    list = input().split()
    count = 0
    for j in range(4):
        if list[j] == '1':
            count += 1
    if count == 4:
        print("E")
    elif count == 3:
        print("A")
    elif count == 2:
        print("B")
    elif count == 1:
        print("C")
    else:
        print("D")
