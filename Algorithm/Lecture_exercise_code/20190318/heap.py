import sys
import heapq
sys.stdin = open("이진힙_input.txt", "r")
T = int(input())

for test_case in range(T):
    N = int(input())
    last = 0
    heap = []
    temp = list(map(int, input().split()))

    for i in range(N):
        heapq.heappush(heap, temp[i])

    for i in range(N):
        print(heapq.heappop(heap), end=" ")
    print()