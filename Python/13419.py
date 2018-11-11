n = int(input())

for j in range(n):
    word = input()
    myturn = ""
    yourturn = ""
    i=0
    while True:
        if i%2 == 0:
            myturn += word[i%len(word)]
            if i >0:
                if yourturn[0] == word[(i+1) % len(word)]:
                    break
        else:
            yourturn += word[i%len(word)]
            if i >0:
                if myturn[0] == word[(i+1) % len(word)]:
                    break
        i += 1

    print(myturn)
    if j+1 == n:
        print(yourturn, end='')
    else:
        print(yourturn)
