# 알고리즘D08_20190212

Stack01 문제풀이



1. 종이붙이기

> 어린이 알고리즘 교실의 선생님은 경우의 수 놀이를 위해, 그림처럼 가로x세로 길이가 10x20, 20x20인 직사각형 종이를 잔뜩 준비했다.
>
> 그리고 교실 바닥에 20xN 크기의 직사각형을 테이프로 표시하고, 이 안에 준비한 종이를 빈틈없이 붙이는 방법을 찾아보려고 한다.
>
> 10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산하는 프로그램을 만드시오. 직사각형 종이가 모자라는 경우는 없다.

```python
import sys
sys.stdin = open('종이붙이기_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())//10
    def paper(N):
        if N == 1:
            return 1
        elif N == 2:
            return 3
        else:
            return paper(N-1) + paper(N-2)*2

    print(f'#{tc+1} {paper(N)}')
```



2. 괄호검사

> 주어진 입력에서 괄호 {}, ()가 제대로 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
>
> 예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
>
> 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
>
> print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.

```python
import sys
sys.stdin = open("괄호검사_input.txt")

T = int(input())
for tc in range(T):
    data = input()
    def check(data):
        stack = []
        for i in data:
            if i == '(' or i == '{':
                stack.append(i)
            elif i == ')' or i == '}':
                if not stack:
                    return 0
                else:
                    popvalue = stack.pop()
                    if (i == ')' and popvalue != '(') or \
                        (i == '}' and popvalue != '{'):
                        return 0
        if stack:
            return 0
        else:
            return 1
    print(f'#{tc+1} {check(data)}')
```



3. 그래프경로

> V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
>
> 두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
>
> 노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
>
> [입력]
>
> 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
>
> 다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
>
> 테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
>
> E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

```python
def dfs(v):
    global S, G, table, visited, V, flag
    visited[v] = 1
    if v == G:
        flag = 1
        return
    for i in range(V):
        if table[v][i] == 1 and visited[i] == 0:
            dfs(i)


import sys
sys.stdin = open('그래프 경로_input.txt')

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    V += 1
    flag = 0
    table = [[0 for _ in range(V)] for _ in range(V)]
    visited = [0 for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().split())
        table[a][b] = 1
    S, G = map(int, input().split())

        # if table[S][i] == 1:

    dfs(S)
    print(f'#{tc+1} {flag}')

```



4. 반복문자 지우기

> 문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.
>
> 반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
>  
>
> 다음은 AAABBA에서 반복문자를 지우는 경우의 예이다.
>
> C**AA**ABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
>
> CA**BB**A 연속 문자 BB를 지우고 A와 A를 잇는다.
>
> C**AA** 연속 문자 AA를 지운다.
>
> C 1글자가 남았으므로 1을 리턴한다.

```python
import sys
sys.stdin = open("반복문자 지우기_input.txt", "r")

T = int(input())
for tc in range(T):
    data = list(input())

    i = 1
    while i != len(data):
        if data[i] == data[i-1]:
            del data[i-1], data[i-1]
            i = 0

        i += 1

    print(f'#{tc+1} {len(data)}')
```

