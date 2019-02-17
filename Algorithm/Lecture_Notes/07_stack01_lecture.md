# Stack_01

예습필기_20190210

#### 알고리즘 D07_20190211



## Stack 자료구조의 개념

### A. Stack의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 스택에 저장되니 자료는 선형구조를 가짐
  - 선형구조 : 자료 간의 관계가 1대 1 (ex.리스트)
  - 비선형구조 : 자료 간의 관계가 1대 N (ex.트리) / N대 N (ex.그래프)
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있음
- 마지막에 삽입한 자료를 가장 먼저 꺼냄
- 후입선출(LIFO, Last-In-First-Out)이라고 부름
  - 스택에 1, 2, 3순으로 자료를 삽입한 후 꺼내면 역순으로, 즉 3, 2, 1순으로 꺼낼 수 있음



### B. Stack의 구현

> ADT : 자료구조 + 연산

- <u>자료구조</u>
  - 자료를 선형으로 저장할 저장소가 필요함
  - 파이썬에서는 리스트를 사용할 수 있음
  - 저장소 자체를 스택이라 부르기도 한다
  - 스택에서 마지막으로 삽입된 원소의 위치를 top이라고 부름
- <u>연산</u>
  - 삽입 (push) : 저장소에 자료를 저장
  - 삭제 (pop) : 저장소에서 자료를 꺼냄 (삽입한 자료의 역순으로)
  - isEmpty : 스택이 공백인지 아닌지 확인하는 연산
  - peek : 스택의 top에 있는 item을 반환하는 연산 ( pop : 리턴 후 꺼냄 / peek : 리턴만 함 )



### C. Stack의 연산

- 빈 스택에 원소 A, B, C를 차례로 삽입 후 한 번 삭제하는 연산 과정

  ```
  공백스택 ( top : -1 )
  push A > top : A
  push B > top : B
  push C > top : C
  pop > C 리턴, top : B
  ```

- push 알고리즘

  > top 을 한 칸 위로 올리고, top이 가리키는 위치에 item을 삽입

  ```python
  # python 스타일 : 리스트의 크기는 무한
  s = []
  def push(item):
      s.append(item)
  ```

  ```python
  # 교수님 강의 > C스타일 : 배열의 사이즈 한정되어 있음
  SIZE = 100
  stack = [0] * SIZE
  top = -1
  def push(item):
      global top
      if top > SIZE - 1:
          return
      else:
          top += 1
          stack[top] = item
  ```

- pop 알고리즘

  > top에 있는 item을 꺼냄 + 리턴 후 top을 한 칸 아래로 이동

  ```python
  # python 스타일
  def pop():
      if len(s) == 0: # 공백스택
          # underflow 처리
          return
      else:
          return s.pop(-1) # -1은 생략해도 됨
  ```

  ```python
  # 교수님 강의 > C스타일 : pop해도 stack에 데이터 남아있음 (pop 후 같은 자리에 덮어쓰기 가능)
  def pop():
      global top
      if top == -1:
          print("Stack is Empty!")
          return 0
      else:
          result = stack[top]
          top -= 1
          return result
  ```

- 구현하기 < 연습문제 1 >

  1. 스택을 구현하기
  2. 구현한 스택을 이용하여 3개의 데이터를 스택에 저장하고 다시 3번 꺼내서 출력하기

  ```python
  # python 스타일
  def push(item):
      s.sppend(item)
      
  def pop():
      if len(s) == 0:
          print('Stack is Empty!!') # underflow
          return
      else:
          return s.pop(-1)
      
  s=[]
  push(1)
  push(2)
  push(3)
  print('pop item =>', pop())
  print('pop item =>', pop())
  print('pop item =>', pop())
  ```

  ```python
  # c 스타일
  SIZE = 100
  stack = [0] * SIZE
  top = -1
  def push(item):
      global top
      if top > SIZE - 1:
          return
      else:
          top += 1
          stack[top] = item
  
  def pop():
      global top
      if top == -1:
          print("Stack is Empty!")
          return 0
      else:
          result = stack[top]
          top -= 1
          return result
  
  push(1)
  push(2)
  push(3)
  print('pop item =>', pop())
  print('pop item =>', pop())
  print('pop item =>', pop())
  ```

- 스택 구현 고려사항

  - 리스트를 사용하여 스택을 구현하는 경우
    - 장점 : 구현이 용이함
    - 단점 : 리스트의 크기를 변경하는 작업은 내부적으로 큰 overhead 발생 작업으로 많은 시간이 소요됨 | 스택의 크기를 변경하기가 어렵다

  > 해결방법

  1. 리스트의 크기가 변동되지 않도록 배열처럼 크기를 미리 정해놓고 사용하는 방법
  2. 동적 연결리스트를 이용하여 저장소를 동적으로 할당하여 스택을 구현하는 방법
     - 장점 : 구현이 용이함
     - 단점 : 리스트로 구현하는 것보다 구현이 복잡함



## Stack의 응용

### A. 괄호검사

- 괄호의 종류 : 대괄호[], 중괄호{}, 소괄호()

- 조건
  1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 함
  2. 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 함
  3. 괄호 사이에는 포함관계만 존재함

- 잘못된 괄호 사용의 예

  - (a(b) | a(b)c) | a{b(c[d]e}f)

- 스택을 이용한 괄호 검사
  - 좌 괄호 나오면 스택에 push
  - 우 괄호 나오면 스택에서 top 괄호를 pop & 우 괄호와 짝이 맞는지 확인 > 짝이 맞으면 버림 / 짝이 맞지 않으면 오류!
  - 괄호 수식이 끝났는데 스택에 괄호가 남아있으면 오류!

- 괄호검사 프로그램 구현 < 연습문제 2 >

  ```python
  # 내 코드
  s = []
  
  def push(item):
      s.append(item)
  
  def pop():
      if len(s) == 0:
          print('Stack is Empty!')
          return
      else:
          return s.pop(-1)
  
  def parencheck(a):
      for i in a:
          if i == '(':
              push('(')
          elif i == ')':
              ret = pop()
              if ret != '(':
                  return False
      return not s
  
  print(parencheck('()()((()))')) # True
  ```

  ```python
  # 강사님 코드
  s = list()
  def push(item):
      s.append(item)
  
  def pop():
      if len(s) == 0:
          print("stack is empty")
          return
      else:
  
          return s.pop(-1)
  
  
  def isEmpty():
      if lens(s) == 0: return True
      else: Return False
  
  def check_matching(data):
      for i in range(len(data)):
          if data[i] == "(":
              push(data[i])
          elif data[i] == ")":
              if isEmpty(): return False
              pop()
      #         오른쪽 만나면 pop 왼쪽 만나면 push 해주면 됨
      if not isEmpty(): return False
      else: return True
  
  data = input()
  print(check_matching(data))
  ```




### B. Function Call

- 함수 호출 관리 | 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
  - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조이므로, 후입선출 구조의 스택을 이용하여 수행순서 관리
  - 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임에 저장하여 시스템 스택에 삽입
  - 함수의 실행이 끝나면 시스템 스택의 top원소(스택 프레임)를 삭제(pop)하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀
  - 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 됨
- 함수 호출 수행 순서

  ![image](https://user-images.githubusercontent.com/45819975/52543966-1e494f80-2df1-11e9-8c8c-3049b528bbd2.png)
- 재귀 호출
  - 자기 자신을 호출하여 순환 수행되는 것

  - 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀 호출 방식을 사용하여 함수를 들면 프로그램의 크기를 줄이고 간단하게 작성할 수 있음

  - 디버깅이 어렵고 잘못 작성하게 되면 수행 시간이 많이 소요됨

  - 예시) factorial
    - n에 대한 factorial : 1부터 n까지의 모든 자연수를 곱하여 구하는 연산
    - 마지막에 구한 하위 값을 이용하여 상위 값을 구하는 작업을 반복
    - 스택 프레임으로 스택에 저장되는 값이 입력값이 틀린 같은 함수의 스택 프레임을 저장한다는 차이점이 있음 ????

    ![image](https://user-images.githubusercontent.com/45819975/52544031-69fbf900-2df1-11e9-8ccc-eea0d33eb081.png)

    ```python
    def fact(n):
        if n == 1:
            return 1
        else:
            return n * fact(n-1)
    # 디버깅 해보면 frames에 스택 쌓이고 사라지는 과정 나타남
    ```


## Memoization

### A. 피보나치 수열

- 재귀 호출을 작성할 수 있는 함수 - 피보나치 수열을 구하는 함수

  - 0과 1로 시작하고 이전이 두 수 합을 다음 항으로 하는 수열

  - 피보나치 수열의 i 번째 값을 계산하는 함수 F를 정의하면 다음과 같음

    ```
    F0 = 0, F1 = 1                  # basis
    Fi = Fi-1 + Fi-2 for i >= 2     # inductive
    ```

  - 위의 정의로부터 피보나치 수열의 i번째 항을 반환하는 함수를 재귀함수로 구현할 수 있음

- 피보나치 수열을 구하는 함수의 알고리즘

  ```python
  def fibo(n)
  	if n < 2:
          return n
      else:
          return fibo(n-1) + fibo(n-2)
  ```

  > 문제점 : 엄청난 중복 호출이 존재함 ( ex. Call Tree로 그려보면 fibo(2)는 엄청 여러번 호출됨 p.171 )



### B. Memoization(메모이제이션)

- 메모이제이션의 의미

  - 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
  - DP(동적 계획법)의 핵심이 되는 기술

- Memoization 단어의 의미

  - 글자 그대로 해석하면 '메모리에 넣기(to put in memory)'라는 의미
  - '기억되어야 할 것'이라는 뜻의 라틴어 Memorandum에서 파생
  - Memorization과 다른 단어!

- Memoization 방법을 적용한 알고리즘

  - 피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면 실행시간을 줄일 수 있음
  - 만약 기존에 계산하여 저장된 값이 있을 경우에는 다시 계산하지 않겠다는 알고리즘

  ```python
  # memo를 위한 리스트를 생성하고, 
  # memo[0] 을 0으로, memo[1]는 1로 초기화 한다
  
  def fibo1(n):
      global memo  # 안써도됨
      if n >= 2 and len(memo) <= n:
          memo.append(fibo1(n-1) + fibo1(n-2))
      return memo[n]
  
  memo = [0, 1]
  # 앞에서부터 순서대로 구해진다
  ```

  - 시간복잡도 : O(n)



## DP(동적 계획법)

### A. DP(동적 계획법) 알고리즘

- Dynamic Programming의 약자
- 그리디 알고리즘과 같이 <u>최적화 문제</u>( 여러가지 답 중에 최선의 답 찾는 것 )를 해결하는 알고리즘
- 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결
- 최종적으로 원래 주어진 입력의 문제를 해결하는 설계 기법



### B. DP(동적 계획법)를 적용한 피보나치 수

> 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있는 최적 부분 구조로 이루어져 있어 DP를 적용할 수 있음

1. 문제를 부분 문제로 분할

   - Fibo(n) 함수는 Fibo(n-1)과 Fibo(n-2)의 합
   - Fibo(n-1)은 Fino(n-2)와 Fibo(n-3)의 합
   - Fibo(2)는 Fibo(1)과 Fibo(0)의 합
   - Fibo(n)은 Fibo(n-1), Fibo(n-2), ... Fibo(2), Fibo(1), Fibo(0)의 부분집합으로 나뉨

2. 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구함

3. 그 결과를 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구함

   | 테이블 인덱스    | [0]  | [1]  | [2]  | [3]  | [4]  | ...  | [n]     |
   | ---------------- | ---- | ---- | ---- | ---- | ---- | ---- | ------- |
   | 저장되어 있는 값 | 0    | 1    | 1    | 2    | 3    | ...  | fibo(n) |

- 피보나치 수를 DP에 적용한 알고리즘

  - 위에 애들은 재귀사용하기 때문에 1000번째 수 구하려고 하면 에러나지만
  - 이 방법으로는 구할 수 있음

  ```python
  def fibo2(n):
      f = [0, 1]
      
      for i in range(2, n+1):
          f.append(f[i-1] + f[i-2])
      
      return f[n]
  ```

  ```python
  # DP 팩토리얼 
  
  def fact_2(n):
      f = [1]
  
      for i in range(1, n + 1):
          f.append(i * f[i-1])
  
      return f[n]
  ```

- DP의 구현 방식

  - recursive 방식 : fibo1()
    - 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 overhead가 발생할 수 있음
  - iterative 방식 : fibo2()
    - Memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적



## DFS(깊이 우선 탐색)

### A. DFS란?

- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요

  - 깊이 우선 탐색 (Depth First Search, DFS)
  - 너비 우선 탐색 (Breadth First Search, BFS)

- DFS 방법 | vertex(정점), edge(간선)

  - 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳 까지 깊이 탐색
  - 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아옴
  - 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정을 방문하여 순회
  - 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택을 사용
  - cf) 피보나치 수열의 call tree


### B. DFS 알고리즘

- DFS 알고리즘
    - 시작 정점 v를 결정하여 방문

    - 정점 v에 인접한 정점 중에서

      1. 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문 > w를 v로 하여 다시 위 판단을 반복

      2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 위 판단을 반복

    - 스택이 공백이 될 때까지 위 과정 반복

- DFS 알고리즘 구현 (수도 코드)

  ```c
  // 스택 
  visited[], stack[] 초기화
  DFS(v)
  	v 방문;
      visited[v] = true;
      do {
          if (v의 인접 정점 중 방문하지 않은 w 찾기)
          	push(v);
          while(w) {
              w 방문;
              visited[w] = true;
              push(w);
              v = w;
              v의 인접 정점 중 방문하지 않은 w 찾기
          }
          v = pop(stack);
      } while(v)
  end DFS()
  ```

  ```c
  // 재귀
  DFS_Recursive(G, v)
      
      visited[ v ] = TRUE // v 방문 설정
      
      FOR each all w in adjacency( G, v ) // v에 인접한 모든 w에 대하여
      	IF visited[w] != TRUE
      		DFS_Recursive(G, w)
  ```





1. 인접행렬
2. 인접정점의 리스트
3. 간선의 배열

### C. <연습문제3>

![image](https://user-images.githubusercontent.com/45819975/52549583-3d5ad800-2e17-11e9-84b8-a0d3da598e93.png)

```python
# 준비과정
import sys
sys.stdin = open('연습3_DFS_재귀_input.txt')

n, e = map(int, input().split())
n += 1
temp = list(map(int, input().split()))

G = [[0 for i in range(n)] for j in range(n)] # 2차원 초기화
visited = [0 for i in range(n)]

for i in range(0, len(temp), 2):  # 입력 받기
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1
```



```python
# 내 답
def dfs(G, v):
    visited[v] = 1
    print(v, end=' ')
    if visited[v] == 1:
        for w in range(n):
            if G[v][w] == 1 and visited[w] == 0:
                visited[w] = 1     #안해줘도 된다
                dfs(G, w)

dfs(G, 1)
```

```python
# 강사님 답( 비슷 )
def dfs(v):
    global G, visited, n
    visited[v] = 1
    print(v, end=' ')
    for w in range(n):
        if G[v][w] and not visited[w]:
            dfs(w)
```



#### 추가 슬라이드 _ dfs 반복 ( 재귀X - overflow 가 나지 않는다 )

```python
STACK s
visited[]
DFS(v)
	push(s, v)
    WHILE NOT isEmpty(s)
    	v = pop(s)
        IF NOT visited[v]
        	visit(v)
            FOR each w in adjacency(v)
            	IF NOT visited[w]
                	push(s, w)
```

> 1-3-7-6-5-2-4 

```python
def dfs(v):
    global G, visited, n
    s = []
    
    s.append(v) # push
    while len(s) != 0
    	v = s.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            # range(n-1, 0, -1)로 주면 1-3-7-6-5-2-4로 돌고
            # range(1, n)으로 주면 1-2-4-6-5-7-3
            for w in range(1, n):
                if G[v][w] == 1 and visited[w] == 0:
                    s.append(W)
```





## workshop

[ladder1](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWhKdvi6ECkDFAS6&contestProbId=AV14ABYKADACFAYh&probBoxId=AWjbeWOaGo0DFAQn&type=PROBLEM&problemBoxTitle=2%EC%9B%94+11%EC%9D%BC&problemBoxCnt=1)

```python
# 문제
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.

김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.

사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고(이 예에서는 2개가 추가됨) 이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.

X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.

방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라 (‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다. 도착 지점은 '2'로 표현된다).
```

```
[제약 사항]

한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.

[입력]

입력 파일의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도착하게 되는 출발점의 x좌표를 출력한다.
```



내 답

```python
import sys
sys.stdin = open('ladder1_input.txt')

for tc in range(10):
    n = int(input())
    # 입력받기
    data = [list(map(int, input().split())) for _ in range(100)]
    # 끝나는 지점 (2) 찾기
    for i in range(100): 
        if data[99][i] == 2:
            end = i
    # 밑에서부터 올라갈 것이기 때문에 출발점 x, y 지정
    x, y = 99, end
    # 맨 윗줄에 도달하기 직전까지
    while x > 0:
        # 방문한 지점은 다시 돌아가지 못하도록 9로 표시
        data[x][y] = 9
        # 왼쪽에 1이 있으면 이동
        if y-1 >= 0 and data[x][y-1] == 1:
            y -= 1
        # 오른쪽에 1이 있으면 이동
        elif y+1 <= 99 and data[x][y+1] == 1:
            y += 1
        # 왼 오 둘 다 1없으면 한 칸 위로 이동
        elif data[x-1][y] == 1:
            x -= 1
	
    # x가 0일 때 y값 출력 (사다리의 시작점)
    print(f'#{tc+1} {y}')

```

