import sys
sys.stdin = open('구슬굴리기_input.txt')

garo, sero = map(int, input().split())
arr = [[1]*(garo+2) for _ in range(sero+2)]
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
for i in range(1, sero+1):
    arr[i] = [1] + list(map(int, input())) + [1]
N = int(input())
dir = list(map(int, input().split()))
for i in range(garo+2):
    for j in range(sero+2):
        if arr[i][j] == 2:
            x, y = i, j
for i in dir:
    while arr[x][y] != 1:
        arr[x][y] = 9
        x += dx[i]
        y += dy[i]
    else:
        x -= dx[i]
        y -= dy[i]
print(sum([line.count(9) for line in arr]))