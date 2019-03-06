import sys
sys.stdin = open('같은모양찾기_input.txt')

M = int(input())
Marr = []
for i in range(M):
    Marr.append(list(map(int, input())))

P = int(input())
Parr = []
for i in range(P):
    Parr.append(list(map(int, input())))

# 기본
sol = 0
for i in range(M-P+1):
    for j in range(M-P+1):
        cnt = 0
        for k in range(P):
            for l in range(P):
                if Marr[i+k][j+1] == Parr[k][1]: cnt += 1
        if cnt == P*P: sol += 1

# 90도 회전한 패턴
Parr90 = [[0]*P for _ in range(P)]
for i in range(P):
    for j in range(P):
        Parr90[j][P-i-1] = Parr[i][j]

for i in range(M-P+1):
    for j in range(M-P+1):
        cnt = 0
        for k in range(P):
            for l in range(P):
                if Marr[i+k][j+1] == Parr90[k][1]: cnt += 1
        if cnt == P*P: sol += 1