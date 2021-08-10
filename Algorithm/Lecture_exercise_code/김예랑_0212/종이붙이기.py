import sys
sys.stdin = open('종이붙이기_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())//10
    def paper(N):
        if N == 1:
            return 1
        elif N == 2:
            return 3
        else:
            return paper(N-1) + paper(N-2)*2

    print(f'#{tc+1} {paper(N)}')