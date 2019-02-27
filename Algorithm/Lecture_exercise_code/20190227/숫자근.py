import sys
sys.stdin = open('숫자근_input.txt')

data = sorted([int(input()) for _ in range(int(input()))])
def digitroot(x):
    while True:
        tempsum = 0
        while x:
            tempsum += x % 10
            x //= 10
        if tempsum < 10: return tempsum
        x = tempsum

maxval = maxidx = 0
for idx, val in enumerate(list(map(digitroot, data))):
    if val > maxval:
        maxval, maxidx = val, idx
print(data[maxidx])

