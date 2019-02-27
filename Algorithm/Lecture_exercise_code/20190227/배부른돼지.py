import sys
sys.stdin = open('배부른돼지_input.txt')

data = sorted([input().split() for feed in range(int(input()))])
happy = 0
maxfeed = 0
minfeed = 100
for datum in data:
    if datum[1] == 'N':
        if int(datum[0]) >= maxfeed:
            maxfeed = int(datum[0])
    else:
        if minfeed >= int(datum[0]):
            minfeed = int(datum[0])
if maxfeed >= minfeed or minfeed == 100:
    print('F')
else:
    print(minfeed)