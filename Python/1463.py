n=int(input())

answer = 0
while n!= 0:
    if n%3 == 0:
        n/=3
        print("1")
    elif n%2 ==0:
        n/=2
        print("2")
    else:
        n-=1
        print("3")
    answer+=1

print(answer,end='')