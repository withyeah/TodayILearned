import sys
sys.stdin = open('사칙연산_input.txt')

for tc in range(1):
    n = int(input())
    op = [0]*(n+1)
    fc = [0]*(n+1)
    sc = [0]*(n+1)
    num = [0]*(n+1)
    opstack = []
    for i in range(n):
        temp = input().split()
        addr = int(temp[0])
        if temp[1].isdigit():
           num[addr] = int(temp[1])
        else:
            op[addr] = temp[1]
            if addr * 2 <= n:
                fc[addr] = int(temp[2])
                if addr * 2 + 1 <= n:
                    sc[addr] = int(temp[3])
    # print(op)
    # print(fc)
    # print(sc)
    # print(num)
    for i in range(n, 0, -1):
        if op[i] != 0:
            opstack.append(op[i])
            if op[i] == '+':
                num[i] = num[fc[i]] + num[sc[i]]
            elif op[i] == '*':
                num[i] = num[fc[i]] * num[sc[i]]
            elif op[i] == '-':
                num[i] = num[fc[i]] - num[sc[i]]
            elif op[i] == '/':
                num[i] = num[fc[i]] / num[sc[i]]
    print(num)
            
