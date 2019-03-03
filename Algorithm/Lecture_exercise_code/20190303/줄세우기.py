import sys
sys.stdin = open('줄세우기_input.txt')

n = int(input())
data = list(map(int, input().split()))
line = []
for i in range(n):
    line.insert(len(line)-data[i], i+1)
print(*line)