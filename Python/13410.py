n, k = map(int, input().split())

muli = []
for i in range(k):
    muli.append('0')
    term = n*(i+1)
    for j in range(len(str(term)), 0, -1):
        muli[i] += str(term)[j-1]

muli = [int(i) for i in muli]
print(max(muli), end='')