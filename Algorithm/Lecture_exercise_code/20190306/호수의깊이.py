import sys
sys.stdin = open('호수의깊이_input.txt')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data2 = data
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
temp, depth = [], 0

def search(i, j, num):
    for d in range(4):
        if data[i+dx[d]][j+dy[d]] != num: return False
    return True

for k in range(1, n//2):
    for i in range(1, n):
        for j in range(1, n):
            if data[i][j] == k:
                if search(i, j, k):
                    temp.append([i, j])
    for line in temp:
        [x, y] = line
        data2[x][y] = k
for i in data2: depth += sum(i)
print(depth)

