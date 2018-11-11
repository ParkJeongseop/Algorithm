n = int(input())

sum = 0
i = 1
while(sum+i < n):
    sum += i
    i += 1

if i%2 == 0:
    print(str(n-sum) + "/" +  str(i-n+sum+1),end='')
else:
    print(str(i-n+sum+1) + "/" + str(n-sum) ,end='')