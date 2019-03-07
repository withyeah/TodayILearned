import sys
sys.stdin = open('반나누기_input.txt')



T = int(input())
for tc in range(T):
    N, Min, Max = map(int, input().split())
    data = sorted(list(map(int, input().split())))
    scoreboard = []
    for i in range(1, 99):
        for j in range(i+1, 100):
            A, B, C = [], [], []
            for k in data:
                if k >= j: A.append(k)
                elif k < i: C.append(k)
                else: B.append(k)
            score = [len(A), len(B), len(C)]
            if max(score) <= Max and min(score) >= Min:
                ans = max(score)-min(score)
                scoreboard.append(ans)
    if scoreboard: print(min(scoreboard))
    else: print(-1)