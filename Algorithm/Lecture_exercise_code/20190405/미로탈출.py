import sys
sys.stdin = open('미로탈출_input.txt')

def BFS():
    dr = (1, -1, 0, 0)
    dc = (0, 0, 1, -1)

    que = [(sr, sc, 3, 0)]
    chk[3][sr][sc] = 1

    while que:
        r, c, bomb, cnt = que.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if map[nr][nc] == 4:
                return cnt + 1
            if map[nr][nc] == 1: continue
            if map[nr][nc] == 2 and not chk[bomb][nr][nc]:
                if not bomb: continue
                else:
                    que.append((nr, nc, bomb-1, cnt+1))
                    chk[bomb][nr][nc] = 1
            if (not map[nr][nc] or map[nr][nc] == 4) and not chk[bomb][nr][nc]:
                que.append((nr, nc, bomb, cnt+1))
                chk[bomb][nr][nc] = 1
    else: return -1

# main ------------------------
R, C = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(R)]
chk = [[[0]*C for _ in range(R)] for _ in range(4)]
for i in range(R):
    for j in range(C):
        if map[i][j] == 3:
            sr, sc = i, j
        if map[i][j] == 4:
            er, ec = i, j
print(BFS())
