n = input()
numlist = [0 for i in range(10)]

for i in range(len(n)):
    numlist[int(n[i])] += 1

numlist[6], numlist[9] = (numlist[6] + numlist[9])//2 ,(numlist[6] + numlist[9])//2 + (numlist[6] + numlist[9])%2
print(max(numlist), end='')