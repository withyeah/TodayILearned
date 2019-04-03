import sys
sys.stdin = open('상자포장하기_input.txt')

def DFS(no, Asum, Bsum):
    global sol
    if no >= N:
        if



# main --------------------------
T = int(input())
for tc in range(T):
    N = int(input())
    box = list(map(int, input().split()))
    sol = 0
    for i in range(N):
        DFS(0, box[i], 0)
    print(sol)