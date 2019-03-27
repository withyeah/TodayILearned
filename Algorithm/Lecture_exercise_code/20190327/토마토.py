import sys
sys.stdin = open('input.txt')

def bfs():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    while tomato:
        r, c, day = tomato.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if data[nr][nc] == 0:
                data[nr][nc] = day + 1
                tomato.append((nr, nc, day + 1))
    else: return day

M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
tomato = []
flag = 1
for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            tomato.append((i, j, 0))
        if data[i][j] == 0:
            flag = 0
sol = bfs()
if flag == 1: sol = 0
for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            sol = -1
print(sol)
