import sys
sys.stdin = open('이진힙_input.txt')

def enq(node):
    global last
    last += 1
    c = last
    p = c//2
    Q[last] = node
    while c > 1 and Q[p] > Q[c]:
        Q[p], Q[c] = Q[c], Q[p]
        c = p
        p = p//2

for tc in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    Q = [0 for _ in range(n+1)]
    last, cnt = 0, 0
    for i in data:
        enq(i)
    while n >= 1:
        cnt += Q[n//2]
        n //= 2
    print('#{} {}'.format(tc+1, cnt))