import sys
sys.stdin = open('같은모양찾기simple_input.txt')

m = int(input())
paper = [list(map(int, input())) for i in range(m)]
p = int(input())
pattern = [list(map(int, input())) for i in range(p)]

def search(i, j):
    for k in range(p):
        for l in range(p):
            if paper[i+k][j+l] != pattern[k][l]:
                return 0
    return 1

cnt = 0
for i in range(m-p+1):
    for j in range(m-p+1):
        if search(i, j):
            cnt += 1
print(cnt)