import sys
sys.stdin = open('최소합_input.txt')

def dfs(r, c):
    global flag, cnt, mincnt
    cnt += data[r][c]
    if cnt > mincnt: return
    if r == c == (N-1):
        flag = 1
        if cnt < mincnt:
            mincnt = cnt
        return
    for i in range(2):
        if 0 <= r+dr[i] < N and 0 <= c+dc[i] < N:
            x = r+dr[i]
            y = c+dc[i]
            dfs(x, y)
            cnt -= data[x][y]


T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    flag, cnt, mincnt = 0, 0, sys.maxsize
    dr = [0, 1]
    dc = [1, 0]
    dfs(0, 0)
    if flag == 1:
        print('#{} {}'.format(tc+1, mincnt))
