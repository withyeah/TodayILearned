import sys
sys.stdin = open('도약_input.txt')

N = int(input())
arr = sorted([int(input()) for _ in range(N)])

cnt = 0
for i in range(N-2): # 시작위치
    for j in range(i+1, N-1): # 첫번째 점프
        jump1 = arr[j]-arr[i]
        for k in range(j+1, N): # 두번째 점프
            jump2 = arr[k]-arr[j]
            if jump1 <= jump2 <= jump1*2:
                cnt += 1
            if jump2 > jump1*2:
                break
print(cnt)