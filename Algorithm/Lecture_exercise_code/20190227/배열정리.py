import sys
sys.stdin = open('배열정리_input.txt')

y, x = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(y)]
G = [[0 for _ in range(x)] for _ in range(y)]
for line in range(len(data)):
    cnt = 0
    for i in range(len(data[line])):
        if data[line][i] == 0:
            cnt = 0
        if data[line][i] == 1:
            cnt += 1
        G[line][i] = cnt
for i in range(len(G)):
    print(*G[i])
