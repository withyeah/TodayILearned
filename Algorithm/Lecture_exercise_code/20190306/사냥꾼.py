import sys
sys.stdin = open('사냥꾼_input.txt')

def hunt(x, y):
    cnt = 0
    for i in range(8):
        for j in range(1, n+2):
            if arr[x+dx[i]*j][y+dy[i]*j] == 1 or arr[x+dx[i]*j][y+dy[i]*j] == 0:
                break
            else: arr[x+dx[i]*j][y+dy[i]*j] = 9
    # return sum[arr.count(9) for line in arr]


n = int(input())
arr = [[0]*(n+2) for _ in range(n+2)]
for i in range(1, n+1):
    arr[i] = [0] + list(map(int, input())) + [0]
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
# rabbit = 0
for x in range(n+2):
    for y in range(n+2):
        if arr[x][y] == 1:
            hunt(x, y)
print(sum([line.count(9) for line in arr]))

