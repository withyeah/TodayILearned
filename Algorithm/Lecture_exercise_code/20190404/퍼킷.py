import sys
sys.stdin = open('퍼킷_input.txt')

def DFS(no, Ssum, Bsum):
    global nmin
    if no >= N:
        if not Bsum: return
        temp = abs(Ssum - Bsum)
        if temp < nmin: nmin = temp
        return

    DFS(no + 1, Ssum, Bsum)
    DFS(no + 1, Ssum*data[no][0], Bsum + data[no][1])



N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
nmin = 0x7fffffff
DFS(0, 1, 0)
print(nmin)