import sys
sys.stdin = open('로봇_input.txt')


def BFS():
    dr = (0, 0, 0, 1, -1) # 동서남북 1234
    dc = (0, 1, -1, 0, 0)
    # 방향 정보 테이블 / 왼쪽 턴 0열, 오른쪽 턴 1열
    turn = [(0, 0), (4, 3), (3, 4), (1, 2), (2, 1)]

    #1] 시작점을 큐에 저장 (방문표시)
    que = [(sr, sc, sdir, 0)] # 행, 열, 방향, 명령횟수
    chk[sdir][sr][sc] = 1 # visit체크

    while que:
        #2] 큐에서 데이터 읽기
        r, c, dir, cnt = que.pop(0)
        if r == er and c == ec and dir == edir: return cnt

        for i in range(1, 4): # Go 1, 2, 3
            nr = r + dr[dir]*i
            nc = c + dc[dir]*i
            if nr < 0 or nr >= R or nc < 0 or nc >= C: break # 맵 범위 벗어나면 break
            if arr[nr][nc] == 1: break # 벽 만나면 break
            # 여기까지 내려왔다는 것은 궤도라는 뜻
            if chk[dir][nr][nc]: continue # 궤도지만 방문했다면 스킵
            que.append((nr, nc, dir, cnt + 1))
            chk[dir][nr][nc] = 1

        for i in range(2): # Turn Left, Right
            ndir = turn[dir][i]
            if chk[ndir][r][c]: continue
            que.append((r, c, ndir, cnt + 1))
            chk[ndir][r][c] = 1

# main --------------------

R, C = map(int, input().split())
chk = [[[0]*C for _ in range(R)] for _ in range(5)] # 열, 행, 면
arr = [list(map(int, input().split())) for _ in range(R)]
rec = []
sr, sc, sdir = map(int, input().split())
sr -= 1; sc -= 1
er, ec, edir = map(int, input().split())
er -= 1; ec -= 1
sol = BFS()
print(sol)