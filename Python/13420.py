n = int(input())

for i in range(n):
    qus = input().split()
    if int(eval(''.join(qus[:3]))) == int(qus[4]):
        print("correct")
    else:
        print("wrong answer")