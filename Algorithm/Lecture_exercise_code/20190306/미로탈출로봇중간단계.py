import sys
sys.stdin = open('미로탈출로봇중간단계_input.txt')

n = int(input())
# data = [list(map(int, input())) for _ in range(n)]
arr = [[1]*(n+2) for _ in range(n+2)]
for i in range(1, n+1):
    arr[i] = [1] + list(map(int, input())) + [1]
turn = list(map(int, input().split()))
dx = [0, 1, 0, -1, 0]
dy = [0, 0, -1, 0, 1]
x, y, i, cnt = 1, 1, 0, 0

while True:
    x += dx[turn[i]]
    y += dy[turn[i]]
    if arr[x][y] == 0:
        arr[x][y] = 9
        cnt += 1
    elif arr[x][y] == 1:
        x -= dx[turn[i]]
        y -= dy[turn[i]]
        i = (i + 1) % 4
    else: break

print(cnt)


# def robot():
#     global x, y, i, cnt
#     while arr[x][y] != 9:
#         arr[x][y] = 9
#         x += dx[turn[i]]
#         y += dy[turn[i]]
#         if arr[x][y] == 1:
#             x -= dx[turn[i]]
#             y -= dy[turn[i]]
#             i += 1
#             if i >= 4:
#                 i -= 4
#             x += dx[turn[i]]
#             y += dy[turn[i]]
#         # else:
#         #     cnt += 1
#         cnt += 1
#
#
# robot()
# print(cnt-1)