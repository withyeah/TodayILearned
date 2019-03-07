import sys
sys.stdin = open('자리배정_input.txt')

def seat(K):
    global C, R
    x, y, i, cnt = 1, 1, 0, 0
    if K > C*R: return 0
    else:
        # for s in range(C*R):
        while True:
            room[x][y] = 9
            cnt += 1
            if cnt == K:
                return x, y
            if room[x+dx[i]][y+dy[i]]:
                i = (i+1)%4
                x += dx[i]
                y += dy[i]
            else:
                x += dx[i]
                y += dy[i]

C, R = map(int, input().split())
K = int(input())
room = [[1]*(R+2) for _ in range(C+2)]
for i in range(1, C+1):
    room[i] = [1] + [0 for _ in range(R)] + [1]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = seat(K)
if answer:
    print(*answer)
else:
    print(0)
