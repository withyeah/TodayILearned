import sys
sys.stdin = open('input.txt')

def bfs():
    global cnt
    que = []
    que.append((R, C, 0))
    dr = (-2, -1, 1, 2, 2, 1, -1, -2)
    dc = (-1, -2, -2, -1, 1, 2, 2, 1)
    while que:
        r, c, cnt = que.pop(0)
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if not arr[nr][nc]: return cnt
            if arr[nr][nc] == 2:
                arr[nr][nc] = 1
                que.append((nr, nc, cnt + 1))

N, M = map(int, input().split())
R, C, S, K = map(int, input().split())
R -= 1; C -= 1; S -= 1; K -= 1
arr = [[2]*M for _ in range(N)]
arr[R][C], arr[S][K], cnt = 1, 0, 0
bfs()
print(cnt+1)