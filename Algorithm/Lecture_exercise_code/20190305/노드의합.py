import sys
sys.stdin = open('노드의합_input.txt')

for tc in range(int(input())):
    n, m, l = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(m)]
    tree = [0 for _ in range(n+1)]
    for i in range(len(data)):
        tree[data[i][0]] = data[i][1]
    for i in range(n-m, 0, -1):
        if i*2+1 <= n:
            tree[i] = tree[i*2] + tree[i*2+1]
        else: tree[i] = tree[i*2]
    print('#{} {}'.format(tc+1, tree[l]))