import sys
sys.stdin = open('이진수2_input.txt')

for tc in range(int(input())):
    N = float(input())
    answer = ''
    for i in range(12):
        answer += str(int(N*2//1))
        N = (N*2)%1
        if N == 0: break
    if N != 0: answer = 'overflow'
    print('#{} {}'.format(tc+1, answer))