# n = int(input())
# m = int(input())
# btn_list = input().split()
# btn_list = [int(i) for i in btn_list]
# print(btn_list)


def solution(n, m, btn_list):
    answer = 0
    num = 0
    for i in range(len(str(n))):#각자리수
        exist = True
        for j in btn_list:#리모컨 버튼 돌기
            if str(n)[i] == j:
                exist = False
        if exist:
            num += 1
        else:#버튼이 없을때
            if str(n)[i+1] > 5: #반올림
                answer = len(str(n)) + 10**len(str(n)[i+1:-1]) - str(n)[i+1:-1]
            else:#반내림
                answer = len(str(n)) + str(n)[i+1:-1]
            break


    return answer

print(solution(int(input()), int(input()), input().split()))