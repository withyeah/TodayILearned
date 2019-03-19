import sys
sys.stdin = open('단순2진암호코드_input.txt')

cypher = [[0, 0, 0, 1, 1, 0, 1],
          [0, 0, 1, 1, 0, 0, 1],
          [0, 0, 1, 0, 0, 1, 1],
          [0, 1, 1, 1, 1, 0, 1],
          [0, 1, 0, 0, 0, 1, 1],
          [0, 1, 1, 0, 0, 0, 1],
          [0, 1, 0, 1, 1, 1, 1],
          [0, 1, 1, 1, 0, 1, 1],
          [0, 1, 1, 0, 1, 1, 1],
          [0, 0, 0, 1, 0, 1, 1]]

T = int(input())
for tc in range(T):
    c, r = map(int, input().split())
    data = [list(map(int, input())) for _ in range(c)]
    # print(data)
    cnt, start = 0, 0
    for line in data:
        for i in line:
            if i == 1:
                cnt += 1
                line2 = line
                break
    # print(cnt)
    password = []
    for i in range(len(line2)-1, -1, -1):
        if line2[i] == 1:
            start = i
            break

    line2 = line2[:start+1]

    for i in range(8):
        password.append(line2[start - 6:start + 1])
        line2 = line2[:start - 6]
        start = len(line2) - 1
    password = list(reversed(password))
    answer = []
    for pw in password:
        for i in range(len(cypher)):
            if pw == cypher[i]:
                answer.append(i)
                break
    if not ((answer[0] + answer[2] + answer[4] + answer[6]) * 3 + answer[1] + answer[3] + answer[5] + answer[7])%10:
        print('#{} {}'.format(tc+1, sum(answer)))
    else: print('#{} {}'.format(tc+1, 0))