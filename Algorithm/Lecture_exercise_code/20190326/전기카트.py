import sys
sys.stdin = open('전기카트_input.txt')

def perm(n, k):
    global minbattery
    if n == k :
        if battery(arr) < minbattery:
            minbattery = battery(arr)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]

def battery(arr):
    battery = data[0][arr[0]]
    for i in range(len(arr) - 1):
        battery += data[arr[i]][arr[i + 1]]
    battery += data[arr[-1]][0]
    return battery


# for tc in range(int(input())):
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(1, N))
    minbattery = sys.maxsize
    perm(N - 1, 0)
    print('#{} {}'.format(tc+1, minbattery))