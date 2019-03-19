import sys
sys.stdin = open('정식이의은행업무_input.txt')

def generator(list, n, data, anslist):
    for i in range(len(list)):
        for j in range(n):
            if list[i] == j: continue
            else:
                temp = data[:i] + str(j) + data[i+1:]
                anslist.append(temp)

for tc in range(int(input())):
    binary = input()
    ternary = input()
    binarylist, ternarylist = [], []
    bintolist = [int(i) for i in binary]
    tertolist = [int(i) for i in ternary]
    generator(bintolist, 2, binary, binarylist)
    generator(tertolist, 3, ternary, ternarylist)
    for i in binarylist:
        for j in ternarylist:
            if int(i, 2) == int(j, 3):
                print('#{} {}'.format(tc+1, int(i, 2)))
