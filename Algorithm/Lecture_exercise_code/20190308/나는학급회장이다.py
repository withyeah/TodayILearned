import sys
sys.stdin = open('나는학급회장이다_input.txt')

N = int(input())
arr = [[0]*5 for _ in range(4)] #행을 후보자로 열을 1, 2, 3점수대로 4열은 합계
for i in range(N):
    score = list(map(int, input().split()))
    for j in range(1, 4):
        arr[j][score[j-1]] += 1
for i in range(1, 4): #후보자별 합계
    for j in range(1, 4):
        arr[i][4] += arr[i][j]*j

for i in range(1, 4):
    for j in range(1, 5):
        print(arr[i][j], end=' ')
    print()

maxi = 1
flag = 0
for i in range(2, 4):
    if arr[maxi][4] < arr[i][4]: # 더 큰 합계를 비교
        maxi = i
        flag = 1
    elif arr[maxi][4] == arr[i][4]: # 합계가 동일하면
        for j in range(3, 1, -1): # 3점부터 비교
            # 두후보 간 더 큰 점수의 후보 탐색
            if arr[maxi][j] == arr[i][j]: continue
            if arr[maxi][j] < arr[i][j]: maxi = i
            flag = 1 # 후보찾았으면 탈출
            break
    if flag == 1: break
print(maxi, arr[maxi][4])