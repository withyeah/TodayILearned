
def upperSearch(s, e, data):
    # data 이하 중에서 가장 큰 값의 위치를 리턴
    sol = -1
    while s <= e:
        m = (s+e)//2
        if arr[m] < data: # data 이하이면 오른쪽 영역(더 큰 값) 재탐색
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
        low = upperSearch(j, N-1, start)
        up = upperSearch(j, N-1, end + 1)
        cnt += up - low
print(cnt)