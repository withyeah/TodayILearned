import sys
sys.stdin = open('최대상금_input.txt')

def dfs(d):
    global change, maxarr
    if d == 0:
        if maxarr <= int(''.join(arr)):
            maxarr = int(''.join(arr))
            return maxarr
    else:
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]
                dfs(d-1)
                arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for tc in range(2):
    data, change = input().split()
    change = int(change)
    depth, maxarr = 0, 0
    arr = [i for i in data]
    memo = [[] for _ in range(change+1)]
    memo[0].append(int((''.join(arr))))
    dfs(change)
    print(maxarr)


