import sys
sys.stdin = open('그래프 경로_input.txt')

def dfs(v):
    global S, G, V, flag
    visited[v] = 1
    if v == G:
        flag = 1
        return
    for i in range(V):
        if table[v][i] == 1 and visited[i] == 0:
            dfs(i)

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    V += 1
    flag = 0 
    table = [[0 for _ in range(V)] for _ in range(V)]
    visited = [0 for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().split())
        table[a][b] = 1
    S, G = map(int, input().split())

    dfs(S)
    print(f'#{tc+1} {flag}')