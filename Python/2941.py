word = input()
alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alphabets:
    word = word.replace(i, '0')

print(len(word))
