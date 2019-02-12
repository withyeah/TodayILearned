import sys
sys.stdin = open("반복문자 지우기_input.txt", "r")

T = int(input())
for tc in range(T):
    data = list(input())

    i = 1
    while i != len(data):
        if data[i] == data[i-1]:
            del data[i-1], data[i-1]
            i = 0

        i += 1

    print(f'#{tc+1} {len(data)}')