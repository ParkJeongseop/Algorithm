count = [0 for i in range(26)]
str = input()

for i in range(len(str)):
    count[ord(str[i])-65 if ord(str[i]) < 91 else ord(str[i])-97] += 1

print(*count)