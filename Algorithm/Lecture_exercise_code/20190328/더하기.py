import sys
sys.stdin = open('input.txt')

def johab(no, nsum):
    global flag
    if nsum > K: return
    if no >= N:
        if nsum == K: flag = 1
        return
    a[no] = data[no]
    johab(no + 1, nsum + data[no])
    if flag: return
    a[no] = 0
    johab(no + 1, nsum)

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    a = [0] * N
    flag = 0
    johab(0, 0)
    if flag: print('YES')
    else: print('NO')