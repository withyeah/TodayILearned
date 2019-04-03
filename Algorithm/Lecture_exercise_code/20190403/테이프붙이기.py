import sys
sys.stdin = open('테이프붙이기_input.txt')

def DFS(no, cnt, hap):
    # 현재 no번 테이프를 붙이거나 붙이지 않는 경우의 시도
    # N/2 개를 고른 경우만 길이의 차 비교
    global sol
    if cnt + (N-no) < N/2: return
    if cnt == N // 2:
        temp = abs(hap - (tot - hap))  # 이등분한 테이프의 차이
        if temp < sol: sol = temp
        return
    if no >= N:
        return


    rec[cnt] = arr[no]
    DFS(no + 1, cnt + 1, hap+arr[no])
    rec[cnt] = 0
    DFS(no + 1, cnt, hap)


# main ------------------------
N = int(input())
arr = list(map(int, input().split()))
rec = [0]*N # 디버깅용 기록
sol = 500*20
tot = sum(arr)
DFS(0, 0, 0) # 0 번째 테이프부터 시작, 고른 개수 0개, 테이프 길이 합
print(sol)