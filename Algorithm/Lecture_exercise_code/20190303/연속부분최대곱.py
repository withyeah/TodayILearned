import sys
sys.stdin = open('연속부분최대곱_input.txt')

n = int(input())
data = [float(input()) for _ in range(n)]
maxx = 0
for i in range(n-1):
    x = 1
    for j in range(i, n):
        if data[j] == 0:
            break
        x *= data[j]
        if x > maxx:
            maxx = x
print(f'{maxx:.3f}')