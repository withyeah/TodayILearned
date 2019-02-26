import sys
sys.stdin = open('미로의거리_input.txt')

for tc in range(int(input())):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    queue = []
    # ans = []
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    for i in range(n):
        for j in range(n):
            if data[i][j] == 2:
                si, sj = i, j
    queue.append((si, sj))
    while queue:
        ans = 0
        t, u = queue.pop(0)
        if not visited[t][u]:
            visited[t][u] += 1
            # ans.append([t, u])
        for i in range(4):
            if t+dx[i] < n and 0 <= t+dx[i] and u+dy[i] < n and 0 <= u+dy[i] and not data[t+dx[i]][u+dy[i]] and not visited[t+dx[i]][u+dy[i]]:
                queue.append(((t+dx[i]), (u+dy[i])))
                visited[t+dx[i]][u+dy[i]] = visited[t][u] + 1
            if t+dx[i] < n and 0 <= t+dx[i] and u+dy[i] < n and 0 <= u+dy[i] and data[t+dx[i]][u+dy[i]] == 3:
                flag = 1
                ans = visited[t][u]
        if flag:
            break

    print(f'#{tc+1} {(ans-1) if flag else 0}')