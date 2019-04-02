# Floyd 알고리즘

import sys

T = int(input())
for tc in range(T):
    temp = list(map(int, input().split()))

    N = temp.pop(0)
    adj = [[0]*N for _ in range(N)]
    idx = 0
    for i in range(0, N):
        for j in range(0, N):
            adj[i][j] = temp[idx]
            if i != j and adj[i][j] == 0:
                adj[i][j] = sys.maxsize
            idx += 1

    for k in range(N):
        for i in range(N):
            if i == k : continue
            for j in range(i+1, N):
                if j == k or j == i : continue
                if adj[i][j] > adj[i][k] + adj[k][j]:
                    adj[j][i] = adj[i][j] = adj[i][k] + adj[k][j]

    minV = sys.maxsize
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += adj[i][j]
        if sum < minV : minV = sum

    print('#{} {}'.format(tc+1, minV))
