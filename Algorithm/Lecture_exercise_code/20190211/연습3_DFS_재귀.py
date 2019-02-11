import sys
sys.stdin = open('연습3_DFS_재귀_input.txt')

n, e = map(int, input().split())
n += 1
temp = list(map(int, input().split()))

G = [[0 for i in range(n)] for j in range(n)] # 2차원 초기화
visited = [0 for i in range(n)]

for i in range(0, len(temp), 2):  # 입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(n):
    print(i, G[i])



def dfs(G, v):
    visited[v] = 1
    print(v, end=' ')
    if visited[v] == 1:
        for w in range(n):
            if G[v][w] == 1 and visited[w] == 0:
                visited[w] = 1
                dfs(G, w)


dfs(G, 1)


def dfs(v):
    global G, visited, n
    visited[v] = 1
    print(v, end=' ')
    for w in range(n):
        if G[v][w] and not visited[w]:
            dfs(w)