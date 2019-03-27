
def lowerSearch(s, e, data):
    # data 이상 중에서 가장 작은 값의 위치를 리턴
    sol = -1
    while s <= e:
        m = (s+e)//2
        if arr[m] >= data: # data 이상이면 왼쪽 영역(더 작은 값) 재탐색
            sol = m
            e = m - 1
        else: s = m + 1 # 오른쪽 탐색
    return sol

def upperSearch(s, e, data):
    # data 이하 중에서 가장 큰 값의 위치를 리턴
    sol = -1
    while s <= e:
        m = (s+e)//2
        if arr[m] <= data: # data 이하이면 오른쪽 영역(더 큰 값) 재탐색
            sol = m
            s = m + 1
        else: e = m - 1 # 왼쪽 탐색
    return sol


N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        start = arr[j] + (arr[j] - arr[i])
        end = arr[j] + (arr[j] - arr[i])*2
        low = lowerSearch(j+1, N-1, start)
        # 예외 경우 : 못찾았거나 2배이상 초과시 스킵
        if low == -1 or arr[low] > end: continue
        up = upperSearch(j+1, N-1, end)
        cnt += (up - low + 1)
print(cnt)