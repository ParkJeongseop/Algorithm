n = int(input())

answer = 0
for i in range(n):
    word = input()
    count = [0 for k in range(26)]
    answer += 1
    for j in range(len(word)):
        id = ord(word[j])-ord('a')
        count[id] += 1
        if j > 1:
            if count[id] > 1 and word[j] != word[j-1]:
                answer -= 1
                break

print(answer)