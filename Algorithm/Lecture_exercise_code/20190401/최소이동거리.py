

# 20190401 망한 코드임 참고 ㄴㄴ



import sys
sys.stdin = open('최소이동거리_input.txt')

def dijkstra(A, D):
    U = set([0])
    for i in range(N+1):
        D[i] = A[0][i]
    print(D)
    while V:
        minDw = 0
        for w in (V-U):
            if D[w] < D[minDw]:
                minDw = w
        print(minDw)
        U.add(minDw)
        print(V)
        V.remove(D[minDw])
    for i in A[w]:
        D[i] = min(D[i], A[w][i])
    return A[0][N]

T = int(input())
for tc in range(T):
    N, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    A = [[0]*(N+1) for _ in range(N+1)]
    for datum in data:
        s, e, d = datum
        A[s][e] = d
    D = [0]*(N+1)
    V = set(range(N+1))
    print(dijkstra(A, D))