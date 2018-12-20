word = input()

count = [0 for i in range(26)]

for i in range(len(word)):
    idx = (ord(word[i])-ord('a')) if ord(word[i]) >= ord('a') else (ord(word[i])-ord('A'))
    count[idx] += 1

max = 0
idx = 0
double = False
for id in range(len(count)):
    if count[id] > max:
        max = count[id]
        idx = id
        double = False
    elif count[id] == max:
        double = True

if double:
    print("?")
else:
    print(chr((ord('A') + idx)))