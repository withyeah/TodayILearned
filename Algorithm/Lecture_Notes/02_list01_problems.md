# 알고리즘 D02

20190115



## A. 오늘 문제

[4828. min max](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

```
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
```

```python
import sys
sys.stdin = open("minmax_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    min = 999999
    max = 0
    for i in data:
        if i < min:
            min = i
        if i > max:
            max = i
    print(f'#{tc+1} {max-min}')
```



[4831. 전기버스](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

```
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
```

```python
import sys
sys.stdin = open("전기버스_input.txt")


T = int(input())

for tc in range(T):
    ans = 0
    now = 0
    K, N, M = map(int, input().split())  # 한번,종점,충전기갯수
    charge = list(map(int, input().split()))  # 충전기위치
    while now + K < N:
        for i in range(K, 0, -1):
            if now + i in charge:
                now += i
                ans += 1
                break
        else:
            print(f'#{tc+1} 0')
            break
    else:
        print(f'#{tc+1} {ans}')
```



[4834. 숫자 카드](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

```
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
```

```python
import sys
sys.stdin = open("숫자 카드_input.txt")

T = int(input())
for tc in range(T):
    ans = 0
    now = 0
    num = int(input())  #카드 장수
    deck = input()      #카드 덱
    count = [0] * 10
    for i in range(len(deck)):
        count[int(deck[i])] += 1
    maxnum = 0
    maxindex = 0
    for x in range(10):
        if maxnum <= count[x]:
            maxnum = count[x]
            maxindex = x
    print(f'#{tc+1} {maxindex} {maxnum}')
```



[4835. 구간합](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

```
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
```

```python
import sys
sys.stdin = open("구간합_input.txt")

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())  # 정수의 개수, 구간의 개수
    integer = list(map(int, input().split()))  # N개의 정수 리스트
    maxnum = 0
    minnum = 999999

    for x in range(M - 1, N):
        num = 0
        for y in range(M-1, -1, -1):
            num += integer[x-y]
        if maxnum <= num:
            maxnum = num
        if minnum >= num:
            minnum = num
    print(f'#{tc+1} {maxnum-minnum}')
```



---

## B. workshop

[Flatten](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV139KOaABgCFAYh&solveclubId=AWhKdvi6ECkDFAS6&problemBoxTitle=1%EC%9B%94+15%EC%9D%BC&problemBoxCnt=1&probBoxId=AWhQWZRqNcoDFAS6)

```
한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.

가로 길이는 항상 100으로 주어진다.

모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.

덤프 횟수는 1이상 1000이하로 주어진다.

주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다
```

```python
import sys
sys.stdin = open("Flatten_input.txt")

for tc in range(10):
    ans = 0
    N = int(input()) #덤프횟수
    data = list(map(int, input().split())) #상자높이리스트
    for i in range(N):
        minnum = 999999
        maxnum = -999999990
        for x in range(100):
            if data[x] < minnum:
                minnum = data[x]
                minindex = x
            if data[x] > maxnum:
                maxnum = data[x]
                maxindex = x
        data[minindex] += 1
        data[maxindex] -= 1
    minnum = 999999
    maxnum = 0
    for i in data:
        if i < minnum:
            minnum = i
        if i > maxnum:
            maxnum = i
    print(f'#{tc+1} {maxnum - minnum}')
```

