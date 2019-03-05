import sys
sys.stdin = open('서브트리_input.txt')

def preorder(node):
    global cnt
    if node != 0:
        cnt += 1
        preorder(table[node-1][1])
        preorder(table[node-1][2])

for tc in range(int(input())):
    cnt = 0
    e, n= map(int, input().split())
    data = list(map(int, input().split()))
    table = [[0 for _ in range(4)] for _ in range(max(data))]
    for i in range(max(data)):
        table[i][0] = i + 1
    for i in range(0, len(data), 2):
        p, c = data[i], data[i+1]
        if table[p-1][1]:
            table[p-1][2] = c
        else: table[p-1][1] = c
        table[c-1][3] = p
    preorder(n)
    print('#{} {}'.format(tc+1, cnt))
