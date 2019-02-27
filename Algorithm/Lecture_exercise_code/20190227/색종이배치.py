import sys
sys.stdin = open('색종이배치_input.txt')

n = 120
i1, j1, x1, y1 = map(int, input().split())
i2, j2, x2, y2 = map(int, input().split())
paper = [[0 for _ in range(n)] for _ in range(n)]


for i in range(i1-1, i1+x1+1):
    for j in range(j1-1, j1+y1+1):
        if i == i1-1 or i== i1+x1 or j == j1-1 or j == j1+y1:
            paper[i+1][j+1] = 2
        else:
            paper[i+1][j+1] = 1

cnt = 0
flag = 0
for i in range(i2, i2+x2):
    for j in range(j2, j2+y2):
        if paper[i+1][j+1] == 1:
            flag = 1
        elif paper[i+1][j+1] == 2:
            cnt += 1
if flag == 1:
    print(3)
else:
    if cnt == 1:
        print(1)
    elif cnt >= 2:
        print(2)
    else:
        print(4)

# for i in range(i2, i2+x2):
#     for j in range(j2, j2+y2):
#         paper[i+1][j+1] += 2
#
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if paper[i][j]:
#             if paper[i][j] == 3:
#                 print(3)
#             else:
#                 for f in range(4):
#                     if paper[i+dx[f]][j+dy[f]] == 0:
#                         cnt += 1
# radius = 2*(x1+x2+y1+y2)
# if cnt < radius:
#     print(2)
# elif (i1+x1 == i2 and j1+y1 == j2) or (i2+x2 == i1 and j2+y2 == j1):
#     print(1)
# else:
#     print(4)




# elif paper[i1+x1+1][j1+y1+1]:
#     print(1)