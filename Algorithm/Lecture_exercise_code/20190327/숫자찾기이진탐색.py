def binsearch(s, e, target):
    m = (s + e)//2
    while s <= e:
        # data == mid : mid+1 리턴
        if target == data[m]: return m+1
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
T = int(input())
Tnum = list(map(int, input().split()))

for num in Tnum:
    print(binsearch(0, N-1, num))