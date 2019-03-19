m, n = map(int, input().split())

count_list = [[0 for j in range(n)] for i in range(m)]
map_list = []

for i in range(m):
    map_list.append(input().split())
