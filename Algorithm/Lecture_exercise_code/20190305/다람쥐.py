import sys
sys.stdin = open('다람쥐_input.txt')

n = int(input())
data = list(map(int, input().split()))
stupid, clever = 0, 0
for i in data:
    if i > 0:
        clever += i 
for i in range(n-1):
    acorn = [0 for _ in range(n)]
    for j in range(i, n):
        if j == i:
            acorn[0] = data[j]
        elif acorn[j] < 0:
            break
        else:
            acorn[j] = acorn[j-1] + data[j]
    if max(acorn) > stupid:
        stupid = max(acorn)
print(stupid, clever)