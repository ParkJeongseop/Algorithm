n = int(input())
answer = [0,0,0,0,0]
for i in range(n):
    x, y = map(int, input().split())
    if x*y == 0:
        answer[4] += 1
    elif x>0 and y>0:
        answer[0] += 1
    elif x<0 and y>0:
        answer[1] += 1
    elif x<0 and y<0:
        answer[2] += 1
    elif x>0 and y<0:
        answer[3] += 1

for i in range(4):
    print("Q{}: {}".format(i+1, answer[i]))
print("AXIS:", answer[4])