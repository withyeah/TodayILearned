import sys
sys.stdin = open('magnetic_input.txt')

for tc in range(10):
    n = int(input())
    data = [list(input().split()) for _ in range(n)]
    ans = 0
    for y in range(n):
        line = []
        for x in range(n):
            if data[x][y] != '0':
                line.append(data[x][y])
        for i in range(len(line)-1):
            if line[i] == '1' and line[i+1] == '2':
                ans += 1
    print(f'#{tc+1} {ans})
