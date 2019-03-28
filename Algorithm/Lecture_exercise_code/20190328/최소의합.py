import sys

def DFS1(no, sum):
    # 첫 번째 방법 : 열의 중복을 허용한 중복순열
    global nmin
    if sum > nmin : return
    if no >= N:
        if sum < nmin: nmin = sum
        return
    for i in range(N):
        rec[no] = data[no][i]
        DFS1(no + 1, sum + data[no][i])

def DFS2(no, sum):
    # 두 번째 방법 : 열의 중복을 배제한 순열
    global nmin
    if sum > nmin: return
    if no >= N:
        if sum < nmin: nmin = sum
        return
    for i in range(N):
        if chk[i]: continue
        chk[i] = 1
        rec[no] = data[no][i]
        DFS2(no + 1, sum + data[no][i])
        chk[i] = 0


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
rec = [0] * N # 고른 값을 기록배열(디버깅용)
chk = [0] * N # 열 체크배열

nmin = sys.maxsize
DFS1(0, 0)
print(nmin)

nmin = sys.maxsize
DFS2(0, 0)
print(nmin)