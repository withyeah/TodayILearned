import sys
sys.stdin = open('양팔저울_input.txt')

def DFS(no, Lsum, Rsum):
    # 현재 추를 사용하거나(왼쪽, 오른쪽 저울에 사용) 사용하지 않기
    # 양쪽 저울 무게가 같으면 성공
    global sol
    if sol: return # 가지치기( flag on이면 리턴 )
    if no >= CN:
        if Lsum == Rsum: sol = 1
        return
    DFS(no + 1, Lsum + chu[no], Rsum) # 현재 추를 왼쪽에 올리기
    DFS(no + 1, Lsum, Rsum + chu[no]) # 현재 추를 오른쪽에 올리기
    DFS(no + 1, Lsum, Rsum)           # 현재 추를 사용하지 않기

# main ----------------------------
CN = int(input())
chu = list(map(int, input().split()))
GN = int(input())
gusul = list(map(int, input().split()))
rec = [0]*CN # 기록배열
for i in range(GN):
    sol = 0  # sol을 flag로 씀
    DFS(0, gusul[i], 0) # 0번 추부터 시작, 왼쪽 저울무게를 구슬로 초기화, 오른쪽 저울 무게 0
    if sol: print('Y')
    else: print('N')