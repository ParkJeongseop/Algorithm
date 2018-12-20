long = input()

answer = long[0]
for i in range(1,len(long)):
    if long[i] == '-':
        answer+=long[i+1]
print(answer,end='')