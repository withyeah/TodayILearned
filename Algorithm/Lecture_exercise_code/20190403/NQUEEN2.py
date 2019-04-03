
def DFS(no): # 현재 행에서 모든 열에 퀸을 놓아보는 경우
    global sol
    if no >= N:
        sol += 1
        return
    for i in range(N):
        if chk1[i]: continue   # 세로 위 방향 체크
        if chk2[no + i]: continue   # 오른쪽 대각선 방향 체크
        if chk3[(N-1)-(no-i)]: continue   # 왼쪽 대각선방향 체크
        chk1[i] = chk2[no + i] = chk3[(N-1)-(no-i)] = 1
        DFS(no + 1)
        chk1[i] = chk2[no + i] = chk3[(N-1) - (no-i)] = 0

# main ------------------------
N = int(input())
arr = [[0]*N for _ in range(N)]
chk1 = [0] * (N + 1)
chk2 = [0] * (N*2 + 1)
chk3 = [0] * (N*2 + 1)
sol = 0
DFS(0) # 0행부터 시작
print(sol)