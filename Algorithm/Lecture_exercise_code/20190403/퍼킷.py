import sys
sys.stdin = open('퍼킷_input.txt')

def DFS(no, Ssum, Bsum):
    global nmin
    if no >= N and Bsum:
        temp = abs(Ssum - Bsum)
        if temp < nmin: nmin = temp
        return
    for i in range(N):
        if chk[i]: continue
        chk[i] = 1
        DFS(no + 1, Ssum*data[i][0], Bsum + data[i][1])
        DFS(no + 1, Ssum, Bsum)
        chk[i] = 0

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
chk = [0]*N
nmin = sys.maxsize
DFS(0, 1, 0)
print(nmin)