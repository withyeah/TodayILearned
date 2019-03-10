
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
            elif 0 <= x+dx[i] <= n and 0 <= y+dy[i] <= n and data[x+dx[i][y+dy[i]] <= 3:
                i = x+dx[i]
                j = y+dy[i]
                maze(i, j)

T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    flag = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == 2:
                x, y = i, j
                maze(x, y)