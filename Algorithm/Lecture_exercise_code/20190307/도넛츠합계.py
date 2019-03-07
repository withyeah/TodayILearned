import sys
sys.stdin = open('도넛츠합계_input.txt')

N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

maxdonutsum = 0
for donuti in range(N-K+1):
    for donutj in range(N-K+1):
        donutsum = 0
        for i in range(K):
            for j in range(K):
                donutsum += data[donuti+i][donutj+j]
        for i in range(1, K-1):
            for j in range(1, K-1):
                donutsum -= data[donuti+i][donutj+j]
        if maxdonutsum < donutsum: maxdonutsum = donutsum
print(maxdonutsum)