import sys
sys.stdin = open('노드의거리_input.txt')

def bfs(G, s):
    global g
    queue.append(s)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] += 1
            ans.append(t)
        for i in range(v):
            if G[t][i+1] and not visited[i+1]:
                queue.append(i+1)
                visited[i+1] = visited[t] + 1
    return (visited[g] - visited[s]) if visited[g] else 0

for tc in range(int(input())):
    v, e = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())
    G = [[0 for _ in range(v+1)] for _ in range(v+1)]
    visited = [0 for i in range(v+1)]
    for [a, b] in data:
        G[a][b] = 1
        G[b][a] = 1
    queue = []
    ans = []
    print(f'#{tc+1} {bfs(G, s)}')