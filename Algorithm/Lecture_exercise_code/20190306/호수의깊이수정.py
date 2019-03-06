import sys
sys.stdin = open('호수의깊이_input.txt')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
temp, depth = [], 0

for i in range(1, n-1):
    for j in range(1, n-1):
        if data[i][j] == 1:
            flag = 0
            for depth in range(1, n):
                for k in range(4):
                    if data[i+dx[k]*depth][j+dy[k]*depth] == 0:
                        flag = 1
                        break
                if flag == 1:
                    break
            data[i][j] = depth
print(sum([sum(i) for i in data]))