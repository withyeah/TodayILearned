import sys
sys.stdin = open('input.txt')

def bfs():
    global radior, radioc
    que = []
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    data[radior][radioc] = 3
    que.append((radior, radioc, 3))
    while que:
        radior, radioc, order = que.pop(0)
        for i in range(4):
            nr = radior + dr[i]
            nc = radioc + dc[i]
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if data[nr][nc] == 1:
                data[nr][nc] = order + 1
                que.append((nr, nc, order + 1))
    else:
        return order

C, R = map(int, input().split())
data = [list(map(int, input())) for _ in range(R)]
radioc, radior = map(int, input().split())
radioc-=1
radior-=1
print(bfs())
cnt = 0
for i in range(R):
    for j in range(C):
        if data[i][j] == 1:
            cnt += 1
print(cnt)