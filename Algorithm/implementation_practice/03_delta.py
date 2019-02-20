arr = [[1, 1, 1, 1, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 1, 1, 1, 1]]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def isWall(x, y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True
    return False

def calAbs(y, x):
    if y-x > 0:
        return y-x
    else:
        return x-y
sum = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if not isWall(testX, testY):
                sum += calAbs(arr[y][x], arr[testY][testX])
print(sum)