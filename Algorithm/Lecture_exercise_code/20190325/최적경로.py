import time
import sys
sys.stdin = open('최적경로_input.txt')

def perm(n, k, distancesum):
    if n == k:
        getmindistance(arr)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1, distancesum + distance())
            arr[i], arr[k] = arr[k], arr[i]

def getmindistance(arr):
    global mindistance
    temp = int(abs(cstmr[arr[0]][0]-work[0]) + abs(cstmr[arr[0]][1]-work[1]))
    temp += int(abs(cstmr[arr[-1]][0] - home[0]) + abs(cstmr[arr[-1]][1] - home[1]))
    for i in range(1, N):
        temp += distance(i, i-1)
        if temp > mindistance:
            return
    if temp < mindistance:
        mindistance = temp
    return mindistance

def distance(a, b):
    return int(abs(cstmr[arr[b]][0]-cstmr[arr[a]][0]) + abs(cstmr[arr[b]][1]-cstmr[arr[a]][1]))

start_time = time.time()
for tc in range(10):
    N = int(input())
    data = list(map(int, input().split()))
    work = (data[0], data[1])
    home = (data[2], data[3])
    cstmr = [(data[i], data[i+1]) for i in range(4, len(data)-1, 2)]
    arr = list(range(N))
    distancesum = 0
    mindistance = sys.maxsize
    perm(N, 0)

    print(mindistance)

print(time.time() - start_time, 'seconds')