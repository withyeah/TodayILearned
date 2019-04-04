import sys
sys.stdin = open('해밀턴순환회로_input.txt')

def DFS(city, cnt, cost):
    global sol
    if cost > sol: return # 가지치기
    # 마지막 도시에서 집으로 가는 최소비용 비교
    if cnt == N:
        if fair[city][0]: # (단 집으로가는 비용이 있는 경우)
            if cost + fair[city][0] < sol:
                sol = cost + fair[city][0]
        return

    # 현재 도시에서 비용이 있고, 방문하지 않은 도시를 모두 시도하는 경우의 수
    for i in range(1, N):
        if fair[city][i] and not chk[i]:
            chk[i] = 1
            DFS(i, cnt + 1, cost + fair[city][i])
            chk[i] = 0


# main -------------------------------------
N = int(input())
fair = [list(map(int, input().split())) for _ in range(N)]
chk = [0]*N
sol = 0x7fffffff
DFS(0, 1, 0) # 첫 번째 도시부터 시작, 순회회수 1(집에서 출발하는 것도 세기), 비용 0원
print(sol)