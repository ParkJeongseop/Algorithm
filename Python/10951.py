while True:
    str = input()
    if len(str)>2:
        a, b = map(int, str.split())
        print(a+b)
    else:
        break