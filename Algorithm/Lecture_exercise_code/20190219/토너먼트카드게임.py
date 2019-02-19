import sys
sys.stdin = open('토너먼트카드게임_input.txt')


def rps(a, b):
    if data[a] == data[b]:
        return a
    elif data[a] == 1:
        if data[b] == 2: return b
        else: return a
    elif data[a] == 2:
        if data[b] == 1: return a
        else: return b
    elif data[a] == 3:
        if data[b] == 1: return b
        else: return a

def mergeSort(data):
    if len(data) <= 1:
        return data
    left = mergeSort(data[:(1+len(data))//2])
    right = mergeSort(data[(1+len(data))//2:])

    # l1, r1 = 0, 0
    # while l1 < len(left) and r1 < len(right):










T = int(input())
for tc in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    data = [[idx, val] for idx, val in enumerate(data)]


    # left, right = [], []
    # while len(left)!=1 or len(right)!=1:
    #     left = data[:(1+len(data)//2)]
    #     right = data[(1+len(data)//2):]
    # print(left)