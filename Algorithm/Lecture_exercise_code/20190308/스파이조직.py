import sys
sys.stdin = open('스파이조직_input.txt')

for tc in range(2):
    N, data = input().split()
    N = int(N)
    spy = [[] for _ in range(len(data))]
    idx = 0
    for i in data:
        if i == '<': data = data.replace('<',' < ')
        elif i == '>': data = data.replace('>', ' > ')
    data = data.split()
    for i in data:
        if i.isdigit():
            spy[idx].append(i)
        elif i == '<':
            idx += 1
        else: idx -= 1
    print(' '.join(spy[N]))