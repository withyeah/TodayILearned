import sys
sys.stdin = open('오셀로_input.txt')

def find(x, y, s):
    if s == 1: color = 2
    else: color = 1
    for i in range(8):
        if board[x+dx[i]][y+dy[i]] == color:
            dir.append(i)

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    board = [[9]*(N+2) for _ in range(N+2)]
    for i in range(1, N+1):
        board[i] = [9] + [0 for _ in range(N)] + [9]
    board[N//2][N//2], board[N//2+1][N//2+1], board[N//2][N//2+1], board[N//2+1][N//2] = 2, 2, 1, 1
    dx = [-1, -1, 0, 1, 1, 0, -1, 1]
    dy = [0, 1, 1, 0, -1, -1, -1, 1]

    for i in range(M):
        x, y, s = map(int, input().split())
        dir = []
        board[x][y] = s
        find(x, y, s)
        for d in dir:
            depth, flag = 1, 0
            temp = []
            while board[x][y] != 9 and board[x][y] != 0:
                x += dx[d] * depth
                y += dy[d] * depth
                temp.append((x, y))
                if board[x][y] == s:
                    flag = 1
                    break
                # depth += 1
            # else:
            if flag == 1:
                for j in temp:
                    k, l = j
                    board[k][l] = s
    print(board)