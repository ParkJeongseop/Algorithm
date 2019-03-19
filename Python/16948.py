n = int(input())
r1, c1, r2, c2 = map(int, input().split())

stacklist = [[r1, c1, 0]]
visited = []
answer = -1

while len(stacklist) > 0:
    r = stacklist[0][0]
    c = stacklist[0][1]
    count = stacklist[0][2]
    if [r, c] not in visited:
        visited.append([r, c])
        if (r, c) == (r2, c2):
            answer = count
            break
        else:
            if r-2 >= 0 and c-1 >= 0:
                stacklist.append([r-2, c-1, count+1])
            if r-2 >= 0 and c+1 < n:
                stacklist.append([r-2, c+1, count+1])
            if c-2 >= 0:
                stacklist.append([r, c-2, count+1])
            if c+2 < n:
                stacklist.append([r, c+2, count + 1])
            if r+2 < n and c-1 >= 0:
                stacklist.append([r+2, c-1, count + 1])
            if r+2 < n and c+1 < n:
                stacklist.append([r+2, c+1, count+1])
    del stacklist[0]

print(answer)