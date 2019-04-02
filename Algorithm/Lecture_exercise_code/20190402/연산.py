import sys
sys.stdin = open('연산_input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    