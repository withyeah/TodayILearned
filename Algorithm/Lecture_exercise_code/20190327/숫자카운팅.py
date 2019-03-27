def binsearch(s, e, target):
    global cnt
    m = (s + e)//2
    while s <= e:
        # data == mid :
        if target == data[m]:
            for i in range(s, e + 1):
                if data[i] == target:
                    cnt += 1
            return cnt
        # data > mid : 오른쪽 영역 재탐색
        elif target > data[m]:
            s = m + 1
            m = (s + e)//2
        # data < mid : 왼쪽 영역 재탐색
        else:
            e = m - 1
            m = (s + e)//2
    return 0 # 못 찾은 경우 0 리턴

N = int(input())
data = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
for target in targets:
    cnt = 0
    binsearch(0, len(data)-1, target)
    print(cnt, end=' ')

