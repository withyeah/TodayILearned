import sys
sys.stdin = open('원안의사각형_input.txt')

r = int(input())
cnt = 0
for i in range(r):
    for j in range(r):
        if (r-i)**2+(r-j)**2 <= r**2:
            cnt += 1
print(cnt*4)