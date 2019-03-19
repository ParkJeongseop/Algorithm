n = input()
n = "0" + n
count = [0 for i in range(10)]
digit_num = len(n)-1
for number in range(10): # 0 1 2 3 ...9
    for digit in range(digit_num): # 0 1 2  세자리
        element = int(n[-1-digit])

        if number == 0:
            if not digit == digit_num-1:
                if element == 0:
                    count[number] += (int(n[0:-1 - digit])-1) * pow(10, digit)
                    if digit > 0:
                        count[number] += int(n[0 - digit:]) + 1
                    else:
                        count[number] += 1
                else:
                    count[number] += (int(n[0:-1 - digit])) * pow(10, digit)
        elif number > element:
            count[number] += (int(n[0:-1 - digit])) * pow(10, digit)
        elif number < element:
            count[number] += (int(n[0:-1 - digit]) + 1) * pow(10, digit)
        else: #같을 때
            count[number] += (int(n[0:-1-digit]))*pow(10, digit)
            if digit > 0:
                count[number] += int(n[0-digit:])+1

if int(n[-1]) != 0:
    count[int(n[-1])] += 1
print(*count)


#
#
# count = [0 for i in range(10)]
#
#
# for i in range(int(n)):
#     number = str(i+1)
#     for j in range(len(number)):
#         count[int(number[j])] += 1
#
# print(*count)





# import time
#
# n = "1"
# while True:
#     n = "0" + n
#     count = [0 for i in range(10)]
#
#     digit_num = len(n) - 1
#     for number in range(10):  # 0 1 2 3 ...9
#         for digit in range(digit_num):  # 0 1 2  세자리
#             element = int(n[-1 - digit])
#
#             if number == 0:
#                 if not digit == digit_num - 1:
#                     if element == 0:
#                         count[number] += (int(n[0:-1 - digit]) - 1) * pow(10, digit)
#                         if digit > 0:
#                             count[number] += int(n[0 - digit:]) + 1
#                         else:
#                             count[number] += 1
#                     else:
#                         count[number] += (int(n[0:-1 - digit])) * pow(10, digit)
#             elif number > element:
#                 count[number] += (int(n[0:-1 - digit])) * pow(10, digit)
#             elif number < element:
#                 count[number] += (int(n[0:-1 - digit]) + 1) * pow(10, digit)
#             else:  # 같을 때
#                 count[number] += (int(n[0:-1 - digit])) * pow(10, digit)
#                 if digit > 0:
#                     count[number] += int(n[0 - digit:]) + 1
#
#     if int(n[-1]) != 0:
#         count[int(n[-1])] += 1
#     temp = ' '.join(map(str, count))
#
#
#     count = [0 for i in range(10)]
#
#
#     for i in range(int(n)):
#         number = str(i+1)
#         for j in range(len(number)):
#             count[int(number[j])] += 1
#
#     print(n)
#
#     if temp !=  ' '.join(map(str, count)):
#         print("Error")
#         time.sleep(1)
#
#     n = str(int(n)+1)