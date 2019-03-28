import sys
sys.stdin = open('input.txt')

def dfs(r, c):
    global cnt
    dr = (1, -1, 0, 0)
    dc = (0, 0, -1, 1)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        if data[nr][nc] == 1:
            data[nr][nc] = 9
            cnt += 1
            dfs(nr, nc)
    return cnt

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
sr, sc = 0, 0
apartment = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            cnt = 1
            apartment.append(dfs(i, j))

print(len(apartment))
for i in sorted(apartment):
    print(i)
