import sys
sys.stdin = open('사칙연산_input.txt')

for tc in range(10):
    n = int(input())
    data = [input().split() for _ in range(n)]
    tree = [0 for _ in range(n+1)]
    operator = []
    for datum in data:
        if datum[1].isdigit():
            tree[int(datum[0])] = int(datum[1])
        else:
            operator.append(datum[1])
    print(tree)
    print(operator)
    for i in range(tree.count(0)-1, 0, -1):
        op = operator.pop()
        if op == '+':
            tree[i] = tree[i*2] + tree[i*2+1]
        elif op == '*':
            tree[i] = tree[i * 2] * tree[i * 2 + 1]
        elif op == '-':
            tree[i] = tree[i * 2] - tree[i * 2 + 1]
        elif op == '/':
            tree[i] = tree[i * 2] / tree[i * 2 + 1]
