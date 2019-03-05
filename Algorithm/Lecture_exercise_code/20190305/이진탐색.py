import sys
sys.stdin = open('이진탐색_input.txt')

def inorder(node):
    global idx
    if node <= n:
        inorder(node*2)
        tree[node] = idx
        idx += 1
        inorder(node*2 + 1)

for tc in range(int(input())):
    n = int(input())
    tree = [0 for _ in range(n+1)]
    idx = 1
    inorder(1)
    print('#{} {} {}'.format(tc+1, tree[1], tree[n//2]))