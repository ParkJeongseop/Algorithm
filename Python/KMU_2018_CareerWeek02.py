def solution(grid, K):
    answer = 0

    N = len(grid)

    sum_list = [0 for i in range(N-K+1)] #n-k+1개이중행렬
    for i in range(N-K+1):
        sum_list[i] = [0 for j in range(N-K+1)]

    select_list = [0 for i in range(N-2*K+2)] #n-k-1개이중행렬
    for i in range(N-2*K+2):
        select_list[i] = [0 for j in range(N-2*K+2)]


    for i in range(len(sum_list)):
        for j in range(len(sum_list)):
            for k in range(K):
                for l in range(K):
                    sum_list[i][j] += grid[i+k][j+l]
    # ##
    for i in range(len(select_list)):
        for j in range(len(select_list)):
            max_n = 0
            for ii in range(len(sum_list)):
                for jj in range(len(sum_list)):
                    if not ((i-K<ii and ii<i+K) and (j-K<jj and jj<j+K)):
                        if sum_list[ii][jj] > max_n:
                            max_n = sum_list[ii][jj]
            select_list[i][j] += sum_list[i][j] + max_n
            # print(str(sum_list[i][j]) +"/"+ str(max_n))
    # print(sum_list)
    # print(select_list)

    for i in range(len(select_list)):
        for j in range(len(select_list)):
            if select_list[i][j] > answer:
                answer = select_list[i][j]
    return answer