import sys
sys.stdin = open('원안의마을_input.txt')

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
villages = []
maxd = 0
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            x, y = i, j
        elif data[i][j] == 1:
            villages.append([i, j])

for village in villages:
    [i, j] = village
    d = ((i-x)**2 + (j-y)**2)**0.5
    if maxd < d:
        maxd = d

print(int(maxd) + (maxd%int(maxd) > 0))
