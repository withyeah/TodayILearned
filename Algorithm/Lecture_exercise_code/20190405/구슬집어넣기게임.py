import sys
sys.stdin = open('구슬집어넣기게임_input.txt')

def BFS():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, 1, -1)

    que = [(Rr, Rc, Br, Bc, 0)]
    chk[Rk][Rc][Br][Bc] = 1
    while que:
        Rr, Rc, Br, Bc, cnt = que.pop(0) # 현 구슬 위치
        #기울임 횟수가 10회가 넘어가면 게임 실패
        for i in range(4):
            Rnr, Rnc = Rr+dr[i], Rc+dc[i] # 빨간 구슬의 다음 가볼 위치
            Bnr, Bnc = Br+dr[i], Bc+dc[i] # 파란 구슬의 다음 가볼 위치
            # 이동방향에 벽이 있는 구슬은 움직일 수 없다.
            if arr[Rnr][Rnc] == '#': # 빨간 구슬의 가볼 위치가 벽이면 현재 위치로
                Rnr, Rnc = Rr, Rc
            if arr[Bnr][Bnc] == '#': # 파란 구슬의 가볼 위치가 벽이면 현재 위치로
                Bnr, Bnc = Br, Bc
            # 빨간 구슬과 파란 구슬이 같은 위치이면 스킵
            # 파란 구슬이 목표 구멍이면 스킵
            # 빨간 구슬이 목표 구멍이면 성공 리턴
            # 가볼 위치의 빨간 구슬, 파란 구슬의 위치를 이미 방문했으면 스킵
            # 여기까지 내려오면 큐에 저장하고 방문 표시


# main ------------------------
T = int(input())
R, C = map(int, input())
chk = [[[[0]*C for _ in range(R)] for _ in range(C)] for _ in range(R)]
arr = [list(input()) for _ in range(R)]
Rr, Rc, Br, Bc, Hr, Hc = 0, 0, 0, 0, 0, 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'R':
            Rr, Rc = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            Br, Bc = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'H':
            Hr, Hc = i, j
            arr[i][j] = '.'

print(BFS())