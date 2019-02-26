import sys
sys.stdin = open('Contact_input.txt')

for tc in range(1):
    l, s = map(int, input().split())
    data = list(map(int, input().split()))
    node = max(data)
    G = [[0 for _ in range(node+1)] for _ in range(node+1)]
    for i in range(0, len(data)-1, 2):
        G[data[i]][data[i+1]] = 1
    visited = [0 for _ in range(node+1)]
    queue = []
    ans = []
    queue.append(s)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] += 1
            ans.append(t)
        for i in range(s):
            if G[t][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    print(G)