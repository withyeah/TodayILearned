import sys
sys.stdin = open('inputoutputtest_input.txt')

first = int(input())
second = list(map(int, input().split()))
third = [list(input()) for _ in range(5)]
print(first)
print(*second)
for line in third: print(''.join(line))

