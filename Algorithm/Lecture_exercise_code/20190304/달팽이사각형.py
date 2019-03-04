n = 4
arr = [[0 for _ in range(n)] for _ in range(n)]
x, y, i, j = 0, -1, 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(1,n**2+1):
    x += dx[j]
    y += dy[j]
    arr[x][y] = i
    if i == n or i == 2*n-1 or i == 3*n-2 or arr[x+dx[j]][y+dy[j]] != 0:
        if j == 3:
            j = 0
        else:
            j += 1
for line in arr:
    print(*line)