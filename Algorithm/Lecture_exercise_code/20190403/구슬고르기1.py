

a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
N = 3

def DFS(no): # 0개에서 N개까지 고르는 조합
    if no >= N:
        for i in range(N): print(b[i], end=' ')
        print()
        return
    b[no] = a[no] # 담기
    DFS(no + 1)
    b[no] = 0 # 담지 않기
    DFS(no + 1)


def DFS2(no, cnt): # N개 중 M개를 고르는 조합
    if cnt == 2:
        for i in range(N): print(b[i], end=' ')
        print()
        return
    if no >= N:
        return
    b[no] = a[no] # 담기
    # 또는 b[cnt] = a[no] : 순서대로 담기
    DFS2(no + 1, cnt + 1)
    b[no] = 0 # 담지 않기
    DFS2(no + 1, cnt)

# DFS(0)      # a[0] 요소 구슬부터 시작
# DFS2(0, 0)  # 0 요소 부터 시작, 개수는 0개부터




##############################
#20190328 구슬고르기 1에서 추가수업#
##############################


def DFS3(no, start):
    #1] 리턴조건 : N번째이면 리턴
    for i in range(N): print(b[i], end=' ')
    print()
    if no >= N or start >= N:
        return
    for i in range(start, N): # a[i]
        b[no] = a[i]
        DFS3(no + 1, i + 1)
        b[no] = 0

# main ----------------------
DFS3(0, 0) # b[0] 담기 시작, a[0] 구슬부터 시작