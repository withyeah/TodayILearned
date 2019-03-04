import sys
sys.stdin = open('공통조상_input.txt')

def pre(node):
    global cnt
    if node != 0:
        cnt += 1
        pre(tree[node-1][1])
        pre(tree[node-1][2])
for tc in range(int(input())):
    v, e ,num1, num2 = map(int, input().split())
    data = input().split()
    tree = [[0 for _ in range(4)] for _ in range(v)]
    for i in range(v):
        tree[i][0] = i+1
    for i in range(0, len(data), 2):
        p, c = int(data[i]), int(data[i+1])
        tree[c-1][3] = p
        if tree[p-1][1]: tree[p-1][2] = c
        else: tree[p-1][1] = c
    plist, cnt = [], 0
    while num1 != 1:
        plist.append(tree[num1-1][3])
        num1 = tree[num1-1][3]
    while num2 != 1:
        num2 = tree[num2-1][3]
        if num2 in plist:
            grand = num2
            break
    pre(grand)
    print('#{} {} {}'.format(tc+1, grand, cnt))



