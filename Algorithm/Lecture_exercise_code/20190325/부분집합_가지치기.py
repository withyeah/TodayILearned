count = 0
total = 0
N = 10
A = [0 for _ in range(N)]
data = list(range(1, 11))

def printSet(n):
    global count
    sum = 0
    for i in range(n):
        if A[i] == 1:
            sum += data[i]

    if sum == 10:
        count += 1
        print('{} :'.format(count), end='')
        for i in range(n):
            if A[i] == 1:
                print('{} '.format(data[i]), end='')
        print()


def powerset(n, k, sum):
    global total
    if sum > 10: return
    total += 1
    if n == k: printSet(n)
    else:
        A[k] = 1
        powerset(n, k+1, sum + data[k])
        A[k] = 0
        powerset(n, k+1, sum)

powerset(N, 0, 0)
print('호출회수 : {}'.format(total))
