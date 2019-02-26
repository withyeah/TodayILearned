import sys
sys.stdin = open('회전_input.txt')

for tc in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    for i in range(m):
        data.append(data[0])
        data.pop(0)
    print(f'#{tc+1} {data[0]}')