count = 0
total = 0
N = 10
A = [0 for _ in range(N)]    # 원소의 포함여부 (0, 1)
data = list(range(1, 11))

def printSet(n):
    global count
    sum = 0
    for i in range(n):
        if A[i] == 1:
            sum += data[i]

    if sum == 10:
        count += 1
        print('{} :'.format(count), end='')          # 생성되는 부분 배열의 갯수 출력
        for i in range(n):                           # 각 부분 배열의 원소 출력
            if A[i] == 1:                            # A[i]가 1이면 포함된 것이므로 출력
                print('{} '.format(data[i]), end='')
        print()


def powerset(n, k):
    global total
    total += 1
    if n == k: printSet(n)
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

powerset(N, 0)
print('호출회수 : {}'.format(total))
