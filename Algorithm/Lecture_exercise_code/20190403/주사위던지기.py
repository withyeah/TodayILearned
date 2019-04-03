import sys
sys.stdin = open('주사위던지기_input.txt')

def DFS1(no): # 중복순열
    if no > N:
        for i in range(1, N+1): print(rec[i], end=' ')
        print()
        return
    for i in range(1, 7): # 눈
        rec[no] = i # 눈 기록
        DFS1(no + 1)

def DFS3(no): # 순열
    if no > N:
        for i in range(1, N+1): print(rec[i], end=' ')
        print()
        return
    for i in range(1, 7): # 눈
        if chk[i]: continue
        chk[i] = 1
        rec[no] = i # 눈 기록
        DFS3(no + 1)
        chk[1] = 0

def DFS2(no, start): # 중복조합
    if no > N:
        for i in range(start, N+1): print(rec[i], end=' ')
        print()
        return
    for i in range(start, 7): # 눈
        rec[no] = i # 눈 기록
        DFS2(no + 1, i)

def DFS4(no, start): # 조합
    if no > N:
        for i in range(1, N+1): print(rec[i], end=' ')
        print()
        return
    for i in range(start, 7): # 눈
        rec[no] = i # 눈 기록
        DFS4(no + 1, i+1)



# main ------------------------
N, M = map(int, input().split())
rec = [0]*(N+1)
chk = [0]*7 # 체크
if M == 1: DFS1(1) # 눈의 중복순열 1번 주사위부터 시작
elif M == 3: DFS3(1) # 눈의 중복을 배제한 순열
elif M == 2: DFS2(1, 1) # 눈 중복 조합 : 1번 주사위부터 시작, 1눈 부터 시작
elif M == 4: DFS4(1, 1) # 눈의 중복을 배제한 조합