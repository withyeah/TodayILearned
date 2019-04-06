def DFS1(no): # 중복순열
    if no > N:
        print(*rec[1:])
        return
    for i in range(1, 7):
        rec[no] = i
        DFS1(no + 1)

def DFS3(no):
    if no > N:
        print(*rec[1:])
        return
    for i in range(1, 7):
        if chk[i]: continue
        chk[i] = 1
        rec[no] = i
        DFS3(no + 1)
        chk[i] = 0

def DFS2(no, start):
    if no > N:
        print(*rec[1:])
        return
    for i in range(start, 7):
        rec[no] = i
        DFS2(no + 1, i)

def DFS4(no, start):
    if no > N:
        print(*rec[1:])
        return
    for i in range(start, 7):
        rec[no] = i
        DFS4(no + 1, i + 1)
        
N = 3
rec = [0]*(N+1)
chk = [0]*7

DFS4(1, 1)