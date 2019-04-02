import sys
sys.stdin = open('그룹나누기_input.txt')

def findset(x):
    if x != p[x]:
        p[x] = findset(p[x])
    return p[x]

def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]: rank[y] += 1

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    p = list(range(N+1))
    rank = [0]*(N+1)
    for i in range(0, len(data)-1, 2):
        x, y = data[i], data[i+1]
        p1, p2 = findset(x), findset(y)
        link(p1, p2)
    sol = 0
    for i in range(1, len(p)):
        if p[i] == i: sol += 1
    print('#{} {}'.format(tc+1, sol))

