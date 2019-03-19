price = [350.34, 230.90, 190.55, 125.30, 180.90]
for i in range(int(input())):
    num = input().split()
    answer = 0
    for i in range(5):
        answer += price[i]*int(num[i])
    if answer*100%10 <= 5:
        answer = int(answer*100)
    else:
        answer = int(answer*100)+1
    print("$"+str(answer)[0:-2]+"."+str(answer)[-2]+str(answer)[-1])
