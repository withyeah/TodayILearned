import sys
sys.stdin = open('배열최소합_input.txt')


def process_solution(a, k, sum):
    if sumlist:
        if sum >= min(sumlist):
            return
    list = []
    sum = 0
    for i in range(1, k+1):
        list.append(data[a[i]])
    perm = [(idx, val) for idx, val in enumerate(list)]
    for i in range(len(perm)):
        sum += arr[perm[i][0]][perm[i][1]-1]
    sumlist.append(sum)

def make_candidate(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands


def backtrack(a, k, input, sum):
    if sumlist:
        if sum >= min(sumlist):
            return
    global MAXCANDIDATES, cnt
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k, sum)
        cnt += 1

    else:
        k += 1
        ncands = make_candidate(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            #arr[k-1][data[a[k]-1]]
            backtrack(a, k, input, sum)

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    data = list(range(n+1))

    MAXCANDIDATES = n+1
    NMAX = n+1
    cnt = 0
    sumlist = []
    a = [0]*NMAX
    backtrack(a, 0, n, 0)
    print(f'#{tc+1} {min(sumlist)}')