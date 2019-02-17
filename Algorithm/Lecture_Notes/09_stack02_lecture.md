

# Stack_02

예습필기_20190217

#### 알고리즘 D09_20190218



## 계산기

### A. 계산기에서 Stack의 활용

> 문자열 계산식이 주어질 때 스택을 이용하여 결과값을 계산할 수 있음

- 문자열 수식 계산의 일반적 방법
  1. 중위표기법의 수식을 후위표기법으로 변경
     - 스택 이용
     - 중위표기법(infix notation) : 연산자를 피연산자 가운데 표기하는 방법 예) A+B
  2. 후위표기법의 수식을 스택을 이용하여 계산
     - 후위표기법(postfix notation) : 연산자를 피연산자 위에 표기하는 방법, 컴퓨터의 연산에서 자주 쓰임 예) AB+



### B. 중위표기식을 후위표기식으로 변환하는 방법

1. 기존의 방법

   1.1 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현

   1.2 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동

   1.3 괄호 제거

   ```
   A*B-C/D 변환
   1. ((A*B) - (C/D))
   2. ((A B)* (C D)/)-
   3. AB*CD/-
   ```

   - 문제점 : 사람이 손으로 처리하기는 쉽지만 프로그램으로 작성하기는 어려움
   - Solution : 중위표기식을 후위표기식으로 변환하는 알고리즘 개발

2. 스택을 이용한 방법

   > 토큰 : 수식에서 의미가 있는 최소 단위
   >
   > 피연산자는 후위표기법 수식에 출력되고 연산자는 스택을 거쳐감

   2.1 입력 받은 중위표기식에서 토큰을 읽음

   2.2 토큰이 피연산자이면 토큰을 출력

   2.3 토큰이 연산(괄호포함)일 경우

   ​	![image](https://user-images.githubusercontent.com/45819975/52910149-91156780-32d6-11e9-9a35-83096f81a765.png)

   ​	2.3.1 우선순위가 높으면 > 스택에 push

   ​	2.3.2 우선순위가 높지 않으면 > 연산자의 우선순위가 토큰의 우선순위ㅣ보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push

   ​	2.3.3 만약 top에 연산자가 없으면 > push

   2.4 토큰이 오른쪽 괄호 `)`일 경우

   ​	2.4.1 스택 top에 왼쪽 괄호 `(`가 올 때까지 스택에 pop연산을 수행

   ​	2.4.2 pop한 연산자를 출력

   ​	2.4.3 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않음

   2.5 중위표기식에 더 읽을 것이 없다면 중지, 더 읽을 것이 있다면 1부터 반복

   2.6 스택에 남아있는 연산자를 모두 pop하여 출력

   ​	2.6.1 스택 밖의 왼쪽 괄호느느 우선 순위가 가장 높으며

   ​	2.6.2 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮음



### C. 후위표기법 수식을 스택으로 계산

> 계산 시 주의 사항! 피연산자를 스택에 쌓아 계산한다

1. 피연산자를 만나면 스택에 push
2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산
   - 피연산자 pop할 때 `s[-2] 연산자 s[t-1] ` 순서 주의*
3. 연산결과를 다시 스택에 push
4. 수식이 끝나면 마지막으로 스택을 pop하여 출력



### D. 내장함수 eval()

> 문자열로 된 수식 계산 시 스택을 두 번 사용해서 처리했던 연산을 파이썬에서 제공되는 eval() 내장 함수로 계산할 수 있음

- eval(수식)
  - 문자열로 된 수식을 계산함
  - Evaluation == '값을 구함' 이라는 뜻
  - 올바른 수식이 아닌 경우 SyntaxError가 발생
  - 예 ) eval('6+5*(2-8)/2')와 같은 문자열로 된 수식의 계산결과를 반환





## 백트래킹

### A. 백트래킹 기법

> 해를 찾는 도중에 '막히면', (즉, 해가 아니면) 되돌아가서 다시 해를 찾아가는 기법

- 최적화(Optimization) , 결정(Decision) 문제를 해결할 수 있음
  - 결정문제 : 문제의 조건을 만족하는 해가 존재하는지 여부를 'yes' 또는 'no'로 답하는 문제
    - 미로 찾기, n-Queen, Map coloring, 부분집합의 합(Subset Sum) 등..
- 백트래킹 기법 활용 - 미로 찾기
  - 입구와 출구가 주어진 미로에서 입구부터 출구까지의 경로를 찾는 문제
  - 이동할 수 있는 방향은 4방향으로 제한
  - 2차원 리스트에 미로를 표현할 수 있음 
  - 이동을 스택에 push 하여 저장 (이동방향은 시계방향 또는 반시계방향으로 우선순위를 정할 수 있음)
  - 더 이상 진행할 수 없으면 진행할 수 있는 상태로 되돌아가야 함(스택에서 pop하여 지나온 경로를 역으로 되돌아 감)
  - 스택을 이용하여 다시 경로를 찾음



### B. 백트래킹 알고리즘의 특징

- 백트래킹과 깊이 우선 탐색의 차이

  ![image](https://user-images.githubusercontent.com/45819975/52910522-046da800-32dc-11e9-9ed6-c22c1e689fdb.png)

- 백트래킹 알고리즘의 특징
  - 어떤 노드의 유망성을 점검한 후에 유망(Promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(Backtracking) 다음 자식 노드로 이동
  - 유망성 : 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 함 / 해답의 가능성이 있으면 유망하다고 함 
  - 가지치기(Pruning) : 유망하지 않은 노드가 포함되는 경로는 더 이상 고려하지 않음 > 탐색하는 경우의 수를 줄일 수 있음
- 백트래킹을 이용한 알고리즘의 절차
  1. 상태 공간 Tree의 깊이 우선 검색을 실시
  2. 각 노드가 유망한지를 점검
  3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속



### C. 백트래킹 알고리즘 예시 (n-Queens)

> n*n의 정사각형 안에 n개의 queen을 배치하는 문제로, 모든 queen은 자신의 일직선상 및 대각선상에 아무 것도 놓이지 않아야 함

- 백트래킹 수도코드

  ```python
  def checknode(v) : # node
      if promising(v):
          if there is a solution at v:
              write the solution
          else:
              for u in each child of v:
                  checknode(u)
  ```

- n-Queens 백트래킹 상태 공간 Tree

  ![image](https://user-images.githubusercontent.com/45819975/52910618-7692bc80-32dd-11e9-9fb6-6c54c2cf193e.png)

  > 깊이 우선 검색 : 155개 노드 탐색
  >
  > 백트래킹 : 27개 노드 탐색 ( 깊이 우선 검색의 1/5 수행시간 )



### D. Power Set

> 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합
>
> 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 2**n이 나옴

- 백트래킹 기법으로 Power Set 구하기
  - 일반적인 백트래킹 접근 방법 이용
  - n개의 원소가 들어있는 집합의 2**n개 부분집합을 만들 때 True 또는 False값을 가지는 항목들로 구성된 n개의 리스트를 만드는 방법 이용
  - 리스트의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값

- code

- ```python
  def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0]*MAXCANDIDATES
    
    if k == input:
        process_solution(a, k) # 답이면 원하는 작업을 한다
    else:  # 아니면 재귀 호출
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
  
  
  def construct_candidates(a, k, input, c): # 후보군을 구하는 함수 
      c[0] = True
      c[1] = False
      return 2
  
  def process_solution(a, k):
      print('(', and='')
      for i in range(k+1):
          if a[i]:
              print(i, end='')
      print(')')
  
  MAXCANDIDATES = 100
  NMAX = 100
  a = [0]*NMAX
  backtrack(a, 0, 3)
  ```

- backtrack 함수의 상태 공간 트리
  ![image](https://user-images.githubusercontent.com/45819975/52914197-e7030300-3308-11e9-8a24-a72d703e443d.png)



- 순열을 구하는 백트래킹 알고리즘

  ```python
  # 접근방법은 부분집합 구하기와 유사함
  def backtrack(a, k, input):
      global MAXCANDIDATES
      c = [0]*MAXCANDIDATES
      
      if k == input:
          for i in range(i, k+1):
              print(a[i], end='')
          print()
      else:
          k += 1
          ncandidates = construct_candidates(a, k, input, c)
          for i in range(ncandidates):
              a[k] = c[i]
              backtrack(a, k, input)
  ```

  ```python
  # 후보군을 구하는 함수 부분이 다름
  def construct_candidates(a, k, input, c):
      in_perm = [False]*NMAX
      
      for i in range(1, k):
          in_perm[a[i]] = True
          
      ncandidates = 0
      for i in range(1, input+1):
          if in_perm[i] == False:
              c[ncandidates] = i
              ncandidates += 1
      return ncandidates 
  ```

  ![image](https://user-images.githubusercontent.com/45819975/52914273-bd96a700-3309-11e9-8c0f-d2719923c1dd.png)





## 분할정복

### A. 분할 정복 알고리즘

> 나폴레옹의 설계 전략에서 유래
>
> - 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눔
> - 정복(Conquer) : 나눈 작은 문제를 각각 해결
> - 통합(Combine) : (필요하다면) 해결된 해답을 모음



- 거듭 제곱(Exponentiation) 알고리즘 : O(n)

  ```python
  def Power(Base, Exponent):
      if Base == 0 :
          return 1
      result = 1 # Base^0은 1이므로
      for i in range(Exponent):
          result *= Base
      return result
  ```

  ```
  C2 = C * C
  C3 = C * C * C
  ...
  Cn = C * C * ... * C
  ```

- 분할 정복 기반의 알고리즘 : O(log2n)

  ```python
  def Power(Base, Exponent):
      if Exponent == 0 or Base == 0:
          return 1
     	if Exponent % 2 == 0:
          NewBase = Power(Base, Exponent/2)
          return NewBase*NewBase
      else:
          NewBase = Power(Base, (Exponent-1)/2)
          return (NewBase*NewBase)*Base
  ```

  ```
  C^8 = C * C * C * C * C * C * C * C
  C^8 = C^4 * C^4 = (C^4)^2 = ((C^2)^2)^2
  C^n = C^(n-1/2) * C^(n-1/2) * C = (C^(n-1/2))^2*C
  Cn = n 이 짝수 : C^(n/2)*C^(n/2)
  	 n 이 홀수 : C^((n-1)/2) * C^((n-1)/2) * C
  ```



### B. 퀵 정렬

- 퀵 정렬과 합병 정렬의 비교

  ![image](https://user-images.githubusercontent.com/45819975/52914477-0d766d80-330c-11e9-807d-507823c92a4a.png)

- 퀵 정렬 알고리즘

  ```python
  def quickSort(a, begin, end):
      if begin < end:
          p = partition(a, begin, end)
          quickSort(a, begin, p-1)
          quickSort(a, p+1, end)
  ```

- 주어진 리스트에서 피봇을 구하는 알고리즘

  ```python
  def partition(a, begin, end):
      pivot = (begin + end)//2
      L = begin
      R = end
      while L < R
      while(a[L] < a[pivot] and L < R):
          L += 1
      while(a[R] >= a[pivot] and L < R):
          R -= 1
      if L < R:
          if L == pivot:
              pivot = R
          a[L], a[R] = a[R], a[L]
      a[pivot], a[R] = a[R], a[pivot]
      return R
  ```

- 퀵 정렬은 최악의 경우 시간복잡도가  O(n^2) > 합병정렬에 비해 좋지 못함

  - 그런데 왜 `퀵` 정렬이라고 했을까? > 평균 시간복잡도가 O(nlogn)이기 때문



- 정렬 알고리즘 비교

  ![image](https://user-images.githubusercontent.com/45819975/52914600-b96c8880-330d-11e9-9107-eec243fc679e.png)