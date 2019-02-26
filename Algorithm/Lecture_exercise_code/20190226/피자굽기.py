import sys
sys.stdin = open('피자굽기_input.txt')

for tc in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    cheese = [[idx+1, val] for idx, val in enumerate(data)]
    queue = []
    for i in range(n):
        queue.append(cheese.pop(0))
    cnt = 0
    while queue:
        [a, b] = queue.pop(0)
        if b//2 == 0:
            if cheese:
                queue.append(cheese.pop(0))
        else:
            queue.append([a, b//2])
            cnt += 1
        if len(queue) == 1:
            break
    print(f'#{tc+1} {queue[0][0]}')
