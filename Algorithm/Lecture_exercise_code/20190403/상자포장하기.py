import sys
sys.stdin = open('상자포장하기_input.txt')

def DFS(no, Abox, Bbox, hap):
    global sol
    if no >= N: return
	for i in range(N-1):
		if box[i] < Abox and box[i+1] > Bbox:
			DFS(no + 1, box[i], Bbox)
			DFS()



# main --------------------------
T = int(input())
for tc in range(T):
    N = int(input())
    box = list(map(int, input().split()))
    sol = 0
    DFS(0, 1000, 0, 0)
    print(sol)