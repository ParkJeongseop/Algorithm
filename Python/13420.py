n = int(input())

for i in range(n):
    qus = input().split()
    if qus[1] == '+':
        if int(qus[0])+int(qus[2]) == int(qus[4]):
            print("correct",end='')
        else:
            print("wrong answer",end='')
    elif qus[1] == '-':
        if int(qus[0])-int(qus[2]) == int(qus[4]):
            print("correct",end='')
        else:
            print("wrong answer",end='')
    elif qus[1] == '*':
        if int(qus[0])*int(qus[2]) == int(qus[4]):
            print("correct",end='')
        else:
            print("wrong answer",end='')
    elif qus[1] == '/':
        if int(qus[0])/int(qus[2]) == int(qus[4]):
            print("correct")
        else:
            print("wrong answer",end='')
    if i+1 != n:
        print()