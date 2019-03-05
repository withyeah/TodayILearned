import sys
sys.stdin = open('숫자맞추기_input.txt')

n = int(input())
score = [0 for _ in range(n)]
data = [[] for _ in range(n)]
for i in range(n):
    a, b, c = map(int, input().split())
    data[0].append(a)
    data[1].append(b)
    data[2].append(c)
for datum in data:
    for i in range(len(datum)):
        if datum.count(datum[i]) == 1:
            score[i] += datum[i]
for i in score:
    print(i)