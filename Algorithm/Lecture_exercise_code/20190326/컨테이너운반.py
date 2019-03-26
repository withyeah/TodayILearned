import sys
sys.stdin = open('컨테이너운반_input.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())
    w = list(reversed(sorted(list(map(int, input().split())))))
    t = list(reversed(sorted(list(map(int, input().split())))))
    neww = [container for container in w if container <= max(t)]
    cnt = 0
    while True:
        for i in t:
            flag = False
            for j in neww:
                if j <= i:
                    cnt += j
                    neww.remove(j)
                    t.remove(i)
                    flag = True
                    break
            if flag:
                break
        else:
            ans = 0
            break
    print('#{} {}'.format(tc+1, cnt))