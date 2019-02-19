import sys
sys.stdin = open('배열최소합_input.txt')

def least(row, n):
    global now
    row += 1
    sum_now = sum(arr[key][val] for key, val in enumerate(data[0:row]))
    if sum_now > now:
        return
    if row == n:
        sum_now = sum(arr[key][val] for key, val in enumerate(data))
        if sum_now < now:
            now = sum_now
            return
    for column in range(n):
        if column not in data[0:row]:
            data[row] = column
            least(row, n)

for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    data = [-1]*n
    row = -1
    now = 1000
    least(row, n)
    print(f'#{tc+1} {now}')
