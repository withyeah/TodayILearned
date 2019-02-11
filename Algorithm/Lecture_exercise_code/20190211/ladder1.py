import sys
sys.stdin = open('ladder1_input.txt')

for tc in range(10):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if data[99][i] == 2:
            end = i
    x, y = 99, end
    while x > 0:
        data[x][y] = 9
        if y-1 >= 0 and data[x][y-1] == 1:
            y -= 1
        elif y+1 <= 99 and data[x][y+1] == 1:
            y += 1
        elif data[x-1][y] == 1:
            x -= 1

    print(f'#{tc+1} {y}')
