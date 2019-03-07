import sys
sys.stdin = open('다람쥐_input.txt')

n = int(input())
data = list(map(int, input().split()))

stupid = [0]*n
stupid[0] = data[0]
for i in range(1, n):
    if stupid[i-1] + data[i] > data[i]:
        stupid[i] = stupid[i-1] + data[i]
    else: stupid[i] = data[i]

smart = []
for i in range(n):
    if data[i] > 0:
        smart.append(data[i])
if not smart: smart.append(max(data))

print(max(stupid), sum(smart))