def solution(words):
    answer = 0

    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                word = words[i] + words[j]
                answer += 1
                for k in range(len(word)//2+1):
                    if word[k] != word[len(word)-k-1]:
                        answer -= 1
                        break

    return answer