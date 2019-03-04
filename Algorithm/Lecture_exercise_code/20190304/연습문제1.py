def preorder(node):
    if node != 0:
        print('{}'.format(node), end=' ')
        preorder(tree[node-1][1])
        preorder(tree[node-1][2])

def inorder(node):
    if node != 0:
        inorder(tree[node-1][1])
        print('{}'.format(node), end=' ')
        inorder(tree[node-1][2])

def postorder(node):
    if node != 0:
        postorder(tree[node-1][1])
        postorder(tree[node-1][2])
        print('{}'.format(node), end=' ')

import sys
sys.stdin = open('연습문제_input.txt')

v, k = map(int, input().split())
data = list(map(int, input().split()))
tree = [[0 for _ in range(4)] for _ in range(v)]
for i in range(v):
    tree[i][0] = i+1
for i in range(0, len(data), 2):
    p, c = data[i], data[i+1]
    tree[c-1][3] = p
    if tree[p-1][1]:
        tree[p-1][2] = c
    else:
        tree[p-1][1] = c



for line in tree:
    print(*line)

print('전위순회 : ', end='')
preorder(1)
print()

print('중위순회 : ', end='')
inorder(1)
print()

print('후위순회 : ', end='')
postorder(1)
print()
