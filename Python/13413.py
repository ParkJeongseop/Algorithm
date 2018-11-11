n = int(input())
for i in range(n):
    input()
    before = input()
    target = input()
    num_b = 0
    num_w = 0
    for j in range(len(before)):
        if before[j] != target[j]:
            if before[j] == "B":
                num_b += 1
            else:
                num_w += 1
    answer = num_b if num_b >= num_w else num_w
    print(int(answer),end='')
    if i+1 != n:
        print()