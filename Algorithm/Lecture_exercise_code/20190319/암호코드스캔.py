import sys
sys.stdin = open('암호코드스캔_input.txt')

asc = {"0": "0000",
       "1": "0001",
       "2": "0010",
       "3": "0011",
       "4": "0100",
       "5": "0101",
       "6": "0110",
       "7": "0111",
       "8": "1000",
       "9": "1001",
       "A": "1010",
       "B": "1011",
       "C": "1100",
       "D": "1101",
       "E": "1110",
       "F": "1111",}

# for tc in range(int(input())):
T = int(input())
for tc in range(2):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]
    rightcorner = []
    for i in range(N):
        for j in range(M-2, -1, -1):
            if data[i][j] != '0' and data[i][j+1] == '0' and data[i-1][j] == '0':
                rightcorner.append([i, j])
    password = []
    for [a, b] in rightcorner:
        for j in range(b, -1, -1):
            if data[a][j] == '0':
                bend = j + 1
                break
        for j in range(a, N+1):
            if data[j][b] == '0':
                aend = j -1
                break
        print(aend, bend)
        print(a, b)
        password.append(data[a][bend:b+1])
    print(password)
    pwtobinary = []

    for i in password:
        temppwtobinary = ''.join([asc[j] for j in i])
        multiple = len(temppwtobinary)//56
        sliced = []
        for j in range(8):
            # sliced += ''.join(temppwtobinary[j*7*multiple:(j+1)*7*multiple])
            temp = temppwtobinary[j*7*multiple:(j+1)*7*multiple]

        pwtobinary.append(temppwtobinary)
        # print(sliced)
