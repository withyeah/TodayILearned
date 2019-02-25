
n = 8
temp = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]


G = [[0 for i in range(n)] for j in range(n)] # 2차원 초기화
visited = [0 for i in range(n)]

for i in range(0, len(temp), 2):  # 입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(n):
    print(i, G[i])



def bfs(G, v):
    queue = []
    ans = []
    v_count = 0
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] += 1
            ans.append(t)
        for i in range(n):
            if G[t][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    return max(visited) - 1


print(bfs(G, 1))


# def dfs(v):
#     global G, visited, n
#     visited[v] = 1
#     print(v, end=' ')
#     for w in range(n):
#         if G[v][w] and not visited[w]:
#             dfs(w)