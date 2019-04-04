import sys
sys.stdin = open('로봇_input.txt')


def BFS():
    dr = (0, 0, 0, 1, -1) # 동서남북 1234
    dc = (0, 1, -1, 0, 0)
    # 방향 정보 테이블
    turn = [(0, 0), (4, 3), (3, 4), (1, 2), (2, 1)]

    #1] 시작점을 큐에 저장 (방문표시)
    que = ((sr, sc, 방향, 명령횟수))


    while que:
        #2] 큐에서 데이터 읽기
        r, c = que.pop(0)

        for i in range(1, 4): # Go 1, 2, 3

        for i in range(2): # Turn Left, Right












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