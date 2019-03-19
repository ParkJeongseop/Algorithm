temp = input().split()
while temp[0]!="0" and temp[1]!="0" and temp[2]!="0" and temp[3]!="0":
    print(str(int(temp[2])-int(temp[1])), str(int(temp[3])-int(temp[0])))
    temp = input().split()