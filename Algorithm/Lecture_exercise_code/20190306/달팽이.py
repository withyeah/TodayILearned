import sys
sys.stdin = open('달팽이_input.txt')


r, c = 0, -1 # 한 칸 이전위치에서 시작
num - 0 #카운팅할 숫자
cnt = N #루프 회전수
while num < N*N:
    # 오른쪽 방향
    for i in range(cnt):
        c += 1 # 열좌표만 증가하면서 오른방향으로
        num += 1
        arr[r][c] = enumerate
    cnt -= 1 # 회전 수 1개 줄임
    # 아래 방향

    # 왼쪽 방향

    # 위쪽 방향

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()