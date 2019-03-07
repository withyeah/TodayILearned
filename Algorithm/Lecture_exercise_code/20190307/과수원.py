import sys
sys.stdin = open('과수원_input.txt')

N = int(input())
data = [list(map(int, input())) for _ in range(N)]

cnt = 0
for x in range(1, N):
    for y in range(1, N):
        apple1, apple2, apple3, apple4= 0, 0, 0, 0
        for i in range(x):
            for j in range(y):
                apple1 += data[i][j]
        for i in range(x):
            for j in range(y, N):
                apple2 += data[i][j]
        for i in range(x, N):
            for j in range(y):
                apple3 += data[i][j]
        for i in range(x, N):
            for j in range(y, N):
                apple4 += data[i][j]
        if apple1 == apple2 == apple3 == apple4:
            cnt += 1
print(cnt if cnt else -1)