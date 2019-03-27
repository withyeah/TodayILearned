def lowerSearch(s, e, target):
    sol = -1
    while s <= e:
        m = (s + e) // 2
        # data == mid : 왼쪽 영역 재탐색
        if target == data[m]:
            sol = m
            e = m - 1
            m = (s + e) // 2
        # data > mid : 오른쪽 영역 재탐색
        elif target > data[m]:
            s = m + 1
            m = (s + e)//2
        # data < mid : 왼쪽 영역 재탐색
        else:
            e = m - 1
            m = (s + e)//2
    return sol

def upperSearch(s, e, target):
    sol = -1
    while s <= e:
        m = (s + e) // 2
        # data == mid : 오른쪽 영역 재탐색
        if target == data[m]:
            sol = m
            s = m + 1
            m = (s + e) // 2
        # data > mid : 오른쪽 영역 재탐색
        elif target > data[m]:
            s = m + 1
            m = (s + e)//2
        # data < mid : 왼쪽 영역 재탐색
        else:
            e = m - 1
            m = (s + e)//2
    return sol

N = int(input())
data = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
for target in targets:
    low = lowerSearch(0, N-1, target)
    if low == -1: print(0, end=' ')
    else:
        up = upperSearch(0, N-1, target)
        print(up-low+1, end=' ')

