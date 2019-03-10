import sys
sys.stdin = open('미로의거리_input.txt')

for tc in range(int(input())):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    queue = []
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    for i in range(n):
        for j in range(n):
            if data[i][j] == 2:
                si, sj = i, j
    queue.append((si, sj))
    while queue:
        ans = 0
        x, y = queue.pop(0)
        if not visited[x][y]:
            visited[x][y] += 1
        for i in range(4):
            if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n and not data[x+dx[i][y+dy[i]] and not visited[x+dx[i]][y+dy[i]]:
                queue.append(((x+dx[i]),(y+dy[i])))
                visited[x+dx[i]][y+dy[i]] = visited[x][y] + 1
            if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n and data[x+dx[i]][y+dy[i]] == 3:
                flag = 1
                ans = visited[x][y]
        if flag:
            break
    print(f'#{tc+1} {(ans-1) if flag else 0}')
    