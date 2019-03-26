import sys
sys.stdin = open('화물도크_input.txt')

def checkmax(data):
    global maxcount
    clock = [0 for _ in range(24)]
    cnt = 0
    for datum in data:
        s, e = datum
        if clock[s:e] == [0 for _ in range(e-s)]:
            clock[s:e] = [1 for _ in range(e-s)]
            cnt += 1
    if maxcount < cnt:
        maxcount = cnt

T = int(input())
for tc in range(T):
    N = int(input())
    maxcount = 0
    data = sorted([list(map(int, input().split())) for _ in range(N)])
    checkmax(data)
    data = list(reversed(data))
    checkmax(data)
    clock = [0 for _ in range(24)]
    cnt = 0
    shortest = []
    for datum in data:
        s, e = datum
        shortest.append([e-s, s, e])
    data = sorted(shortest)
    for datum in data:
        l, s, e = datum
        if clock[s:e] == [0 for _ in range(e - s)]:
            clock[s:e] = [1 for _ in range(e - s)]
            cnt += 1
    if maxcount < cnt:
        maxcount = cnt

    print('#{} {}'.format(tc+1, maxcount))