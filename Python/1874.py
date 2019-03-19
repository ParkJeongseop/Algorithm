n = int(input())
need = [int(input()) for i in range(n)]
numbers = [i+1 for i in range(n)]
stacklist = []
answer = ""

while len(need) > 0:
    if len(stacklist) == 0:
        answer += "+\n"
        stacklist.append(numbers[0])
        del numbers[0]
    if stacklist[-1]>need[0]:
        answer = "NO"
        break
    elif stacklist[-1]<need[0]:
        answer += "+\n"
        stacklist.append(numbers[0])
        del numbers[0]
    elif need[0] == stacklist[-1]:
        del stacklist[-1]
        del need[0]
        answer += "-\n"

print(answer)