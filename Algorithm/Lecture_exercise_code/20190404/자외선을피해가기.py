import sys
sys.stdin = open('자외선을피해가기_input.txt')

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def BFS():
    que = []
    #1] 시작점 큐에 저장(기록)
    que.append((0, 0))
    rec[0][0] = arr[0][0]

    while que:
        #2] 큐에서 데이터 읽기
        r, c = que.pop(0)

        #3] 연결점 찾아 큐에 저장(기록)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue # 범위를 벗어나면 스킵
            # 가볼 위치의 이전의 해 > 현재진행경로의 해 비교하여 최소이면
            if rec[nr][nc] > rec[r][c] + arr[nr][nc]:
                rec[nr][nc] = rec[r][c] + arr[nr][nc]
                que.append((nr, nc))

    #4] 큐가 빈상태
    return rec[N-1][N-1]

# main -------------------------------------
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
rec = [[100000]*N for _ in range(N)] # 자외선합 기록
sol = BFS()
print(sol)