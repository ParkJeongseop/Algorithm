n, m = map(int, input().split())
maze = [[0 for j in range(m)] for i in range(n)]
answer = 1
queue = [(0, 0)]

for i in range(n):
    tmpstr = input()
    for j in range(m):
        maze[i][j] = tmpstr[j]


isFinish = False
while not isFinish:
    answer += 1
    for i in queue:
        if i == (n-1, m-1):
            isFinish = True
        elif 

print(answer)


def mazerunner(x, y, count):
    if x == n-1 and y == m-1:
        if count+1 < answer:
            answer = count+1
    elif not maze[x][y] == 0:
        if maze[x] < n-1:
            mazerunner(x+1, y, count+1)
        if maze[y] < m-1:
            mazerunner(x, y+1, count+1)


mazerunner(0, 0, 1)