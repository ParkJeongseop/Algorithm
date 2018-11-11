n_num = int(input())
n = list(map(int, input().split()))
n.sort()
m_num = int(input())
m = list(map(int, input().split()))

def bin_search(list, target, low, high):
    if low > high:
        return 0
    mid = (low+high)//2
    if list[mid] == target:
        return 1
    elif list[mid] > target:
        return bin_search(list, target, low, mid-1)
    else:
        return bin_search(list, target, mid+1, high)

for i in range(m_num):
    print(bin_search(n, m[i], 0, n_num-1),end='')
    if i+1 != m_num:
        print()