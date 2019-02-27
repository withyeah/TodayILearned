import sys
sys.stdin = open('색종이(중)_input.txt')

n = 102
black = int(input())
data = [list(map(int, input().split())) for _ in range(black)]
paper = [[0 for _ in range(n)] for _ in range(n)]
for [x, y] in data:
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i+1][j+1] = 1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
cnt = 0
for i in range(n):
    for j in range(n):
        if paper[i][j] == 1:
            for f in range(4):
                if paper[i+dx[f]][j+dy[f]] == 0:
                    cnt += 1
print(cnt)