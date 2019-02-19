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

def mergeSort(i, j):
    if i == j:
        return i
    a = mergeSort(i, (i+j)//2)
    b = mergeSort((i+j)//2+1, j)
    return rps(a, b)

T = int(input())
for tc in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    print(f'#{tc+1} {mergeSort(0, len(data)-1)+1}')
