count = 0
N = 3
A = [0 for _ in range(N)]
data = [1, 2, 3]

def printSet(n):
    global count
    count += 1
    print('{} :'.format(count), end='')
    for i in range(n):
        if A[i] == 1:
            print('{} '.format(data[i]), end='')
    print()

def powerset(n, k):  # n: 원소의 갯수, k:  현재 depth
    if n == k: printSet(n)  # Basis Part
    else:                   # Inductive Part
        A[k] = 1            # k번 요소 O
        powerset(n, k+1)    # 다음 요소 포함 여부 결정
        A[k] = 0            # k번 요소 X
        powerset(n, k+1)    # 다음 요소 포함 여부 결정

powerset(N, 0)