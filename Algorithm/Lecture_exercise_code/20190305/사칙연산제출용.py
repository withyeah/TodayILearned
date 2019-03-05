def cal(a, b, c):
    if b == '+':
        return a+c
    if b == '-':
        return a-c
    if b == '*':
        return a*c
    if b =='/':
        return a/c

def inorder(node):
    if tree[node][1].isdigit():
        return tree[node][1]
    else:
        a = inorder(tree[node][2])
        b = inorder(tree[node][3])
        return cal(a, tree[node][1], b)

for tc in range(10):
    n = int(input())
    tree = [[0 for _ in range(4)] for _ in range(n+1)]
    for i in range(1, n+1):
        data = input().split()
        if len(data) == 4:
            tree[i] = [int(data[0]), data[1], int(data[2], int(k[3]))]
        else:
            tree[i][0] = int(data[0])
            tree[i][1] = int(data[1])
    print('#{} {}'.format(tc+1, int(inorder(1))))