def get_num(c):
    if c <= 'C':
        return 2
    elif c <= 'F':
        return 3
    elif c <= 'I':
        return 4
    elif c <= 'L':
        return 5
    elif c <= 'O':
        return 6
    elif c <= 'S':
        return 7
    elif c <= 'V':
        return 8
    elif c <= 'Z':
        return 9
    else:
        return 0

word = input()
nums = []
for i in word:
    nums.append(get_num(i)+1)

print(sum(nums))