st = input()
answer = st[0]
vowel = ['a','e','i','o','u']

stack = 0
for i in range(1,len(st)-1):
    if stack == 0:
        for j in vowel:
            if st[i] == j:
                stack = 1
        answer += st[i]
    elif stack == 1:
        if st[i] == 'p':
            stack = 2
        else:
            stack = 0
            answer += st[i]
    elif stack == 2:
        isVowel = False
        for j in vowel:
            if st[i] == j:
                isVowel = True

        if isVowel:
            stack = 0
        else:
            answer += st[i]
            stack = 0
    else:
        stack = 0

print(answer)