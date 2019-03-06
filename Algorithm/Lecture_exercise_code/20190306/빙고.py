# 빙고

import sys
sys.stdin = open('빙고_input.txt')


def find(x):
    for i in range(5):
        for j in range(5):
            if Barr[i][j] == x:
                Barr[i][j] = 0
                return

def Bingo():
    Crosnum1, Crosnum2 = 0, 0
    cnt = 0
    for i in range(5):
        Rsum, Csum = 0, 0
        for j in range(5):
            Rsum += Barr[i][j]
            Csum += Barr[j][i]
        if Rsum == 0: cnt += 1
        if Csum == 0: cnt += 1
        Crosnum1 += Barr[i][i]
        Crosnum2 += Barr[i][5 - i - 1]
    if Crosnum1 == 0: cnt += 1
    if Crosnum2 == 0: cnt += 1
    if cnt >= 3: return True
    else: return False

# 입력받기
Barr = [] # 빙고배열
for i in range(5):
    Barr.append(list(map(int, input().split())))

Carr = [] # 사회자배열
for i in range(5):
    Carr.append(list(map(int, input().split())))


flag = 0
for i in range(5):
    for j in range(5):
        find(Carr[i][j]) # 해당 숫자를 찾아 지우기
        if Bingo():
            flag = 1
            break # 3줄의 빙고를 찾으면 탈출
    if flag == 1 : break
print(i * 5 + j + 1) # 사회자가 부른 횟수
