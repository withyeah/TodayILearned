def hill(r, c):
    min = 1000
    for direction in dxy:
        move = tuple(map(sum, zip((r, c), direction)))
        if move[0] >= 0 and move[1] >= 0 and move[0] < N and move[1] < N:
            value = grid[move[0]][move[1]]
            if value <= min: min = value
    if grid[r][c] == min+1: result =False
    else: result = True
    grid[r][c] = min+1
    return result

N = int(input())
grid = [list(map(int, input())) for _ in range(N)]
dxy = [(1,0), (-1, 0), (0, 1), (0, -1)]
now = 1
while now:
    now = False
    for r in range(1, N-1):
        for c in range(1, N-1):
            if grid[r][c]:
                result = hill(r, c)
                if not now and result:
                    now = result
print(max([item for items in grid for item in items]))