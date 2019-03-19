while True:
    str = input()
    if str == "END":
        break
    else:
        for i in range(len(str)):
            print(str[-1-i],end='')
        print()