import sys
sys.stdin = open('소수의개수와최대최소구하기_input.txt')

def prime(a, b):
    cnt = 0
    sieve = [0]*2 + [1]*(b-2)
    m = int(b ** 0.5)
    for i in range(2, m+1):
        if sieve[i]:
            for j in range(i+i, b, i):
                sieve[j] = 0
    for i in range(a, b):
        if sieve[i]: cnt += 1
    for i in range(a, b):
        if sieve[i]:
            minprime = i
            break
    for i in range(b-1, a-1, -1):
        if sieve[i]:
            maxprime = i
            break
    return cnt, minprime, maxprime

for tc in range(3):
    a, b = map(int, input().split())
    cnt, minprime, maxprime = prime(a, b)
    print(cnt)
    print(minprime+maxprime)