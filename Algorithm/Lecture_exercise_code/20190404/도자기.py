import sys
sys.stdin = open('도자기_input.txt')

def DFS(start, cnt):
    global sol
    if cnt == M:
        sol += 1
        return
    backup = 0 # 지역변수로 백업 / 또는 밑에 주석 처리한 (기록하면서 가는)방법
    for i in range(start, N): # 흙의 재료
        if backup == arr[i]: continue
        # if rec[cnt] == arr[i]: continue # 같은 재료이면 스킵
        # rec[cnt] = arr[i]
        backup = arr[i]
        DFS(i+1, cnt+1)
    # rec[cnt] = 0 # 잔상 지우기

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    rec = [0]*N
    sol = 0
    DFS(0, 0) # 0번 요소부터 시작, 개수는 0개
    print(sol)