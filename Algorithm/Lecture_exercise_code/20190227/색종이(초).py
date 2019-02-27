import sys
sys.stdin = open('색종이(초)_input.txt')

n = 100
black = int(input())
data = [list(map(int, input().split())) for _ in range(black)]
paper = [[0 for _ in range(n)] for _ in range(n)]
for [x, y] in data:
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1
cnt = 0
for i in range(n):
    for j in range(n):
        if paper[i][j]:
            cnt += 1

print(cnt)