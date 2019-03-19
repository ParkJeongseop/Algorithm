answer = 0
layer = 0
arrangement = input()
for i in range(len(arrangement)-1):
    if arrangement[i] == '(' and arrangement[i+1] != ')':#stack
        layer += 1
    elif arrangement[i] == '(' and arrangement[i+1] == ')':#cutting
        answer += layer
    elif arrangement[i] != '(' and arrangement[i+1] == ')':#pop
        layer -= 1
        answer += 1
print(answer)