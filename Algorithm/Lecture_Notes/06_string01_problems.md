# 알고리즘 D06_20190129

문제 풀이

**문자열비교**

```python
import sys
sys.stdin = open("문자열비교_input.txt")

T = int(input())
for tc in range(T):
    target = input()
    data = input()
    i, j, ans = 0, 0, 0
    while j < len(target) and i < len(data):
        if data[i] != target[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == len(target):
        ans = 1
    else:
        ans = 0
    print(f'#{tc+1} {ans}')
```



**회문**

```python
import sys
sys.stdin = open("회문_input.txt")

T = int(input())

def hm(x):
    for i in range(len(x)//2):
        if x[i] != x[-i-1]:
            return False
    return True

for tc in range(T):
    N, M = map(int, input().split())
    data = [input() for i in range(N)]
    x = ''
    for j in range(N):
        y = ''
        for i in range(N):
            y += data[i][j]
        for z in range(N - M + 1):
            if hm(y[z:M + z]):
                ans = y[z:M + z]
            x = data[j][z:M + z]
            if hm(x):
                ans = x

    print(f'#{tc+1} {ans}')

```



**글자수**

```python
import sys
sys.stdin = open("글자수_input.txt")

T = int(input())

for tc in range(T):
    a = input()
    b = input()
    data = {i:b.count(i) for i in a}
    maxnum = 0
    for value in data.values():
        if value > maxnum:
            maxnum = value
    print(f'#{tc+1} {maxnum}')
```



**회문2**

```python
import sys
sys.stdin = open("회문2_input.txt")

def hm(x):
    for i in range(len(x)//2):
        if x[i] != x[-i-1]:
            return False
    return True

for tc in range(10):
    N = int(input())
    data = [input() for i in range(100)]
    maxlen = 3
    for M in range(100, 2, -1):
        x = ''
        for j in range(100):
            y = ''
            for i in range(100):
                y += data[i][j]
            for z in range(100 - M + 1):
                if hm(y[z:M + z]):
                    if len(y[z:M + z]) > maxlen:
                        maxlen = len(y[z:M + z])
                x = data[j][z:M + z]
                if hm(x):
                    if len(x) > maxlen:
                        maxlen = len(x)
    print(f'#{N} {maxlen}')
```