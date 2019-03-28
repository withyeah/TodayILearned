def bfs():
    global cnt
    que = []
    dr = (-3, -2, 2, 3, 3, 2, -2, -3)
    dc = (-2, -3, -3, -2, 2, 3, 3, 2)
    que.append((r1, c1, 0))
    while que:
        r, c, cnt = que.pop(0)
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= 10 or nc < 0 or nc >= 9: continue
            if not arr[nr][nc]: return cnt + 1
            if arr[nr][nc] == 2:
                arr[nr][nc] = 1
                que.append((nr, nc, cnt + 1))
    else: return -1
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
arr = [[2]*9 for _ in range(10)]
arr[r2][c2], cnt = 0, 0
print(bfs())