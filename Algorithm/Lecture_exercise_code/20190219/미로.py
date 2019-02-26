def maze(x, y):
    global flag, n
    if data[x][y] == 3:
        flag = 1
        return
    else:
        data[x][y] = 9
        for i in range(4):
            if data[x][y] == 3:
                flag = 1
                return
            elif x+dx[i] >= 0 and x+dx[i] < n and y+dy[i] >= 0 and y+dy[i] < n and (data[x+dx[i]][y+dy[i]] == 0 or data[x+dx[i]][y+dy[i]] == 3):
                h = x+dx[i]
                v = y+dy[i]
                maze(h, v)

T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    flag = 0
    for h in range(n):
        for v in range(n):
            if data[h][v] == 2:
                x, y = h, v
                maze(x, y)
                print(f'#{tc+1} {flag}')