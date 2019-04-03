import sys
sys.stdin = open('책꽂이_input.txt')

def DFS(no, hsum):
    global hmin
    if hsum > hmin: return
    if no >= N:
        if hsum > B:
            if hsum < hmin: hmin = hsum
        return
    for i in range(N):
        if chk[i]: continue
        chk[i] = 1
        DFS(no + 1, hsum + H[i])
        DFS(no + 1, hsum)
        chk[i] = 0

T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    chk = [0]*N
    hmin = sys.maxsize
    DFS(0, 0)
    print(hmin-B)