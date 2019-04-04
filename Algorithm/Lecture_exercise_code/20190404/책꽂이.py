import sys
sys.stdin = open('책꽂이_input.txt')

def DFS(no, hsum):
    global hmin
    if hsum > hmin: return
    if no >= N:
        if hsum >= B:
            if hsum < hmin: hmin = hsum
        return

    DFS(no + 1, hsum + H[no])
    DFS(no + 1, hsum)

T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    chk = [0]*N
    hmin = 0x7fffffff
    DFS(0, 0)
    print(hmin-B)