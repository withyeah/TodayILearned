import sys
sys.stdin = open('다람쥐_input.txt')

n = int(input())
data = list(map(int, input().split()))
stupid, clever = 0, 0
for i in range(n):
    if data[i] > 0:
        clever += i
    acorn = [0*n]
    if i == n-1:
        continue
    else:
        for j in range(i, n):
            if j == i:
                acorn[0] = data[j]
            else:
                acorn[j] = acorn[j-1] + data[j]
        if max(acorn) > stupid:
            stupid = max(acorn)
print(stupid, clever)