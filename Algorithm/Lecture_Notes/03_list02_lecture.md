# 20190121_알고리즘03 _배열2



## 배열: 2차 배열

### A. 2차원 배열의 선언

- 1차원 list를 묶어놓은 list
- 2차원 이상의 다차원 list는 차원에 따라 Index를 선언
- 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

```python
arr = [[0, 1, 2, 3], [4, 5, 6, 7]] #2행 4열의 2차원 List
```



### B. 2차원 배열의 접근

- 배열 순회 : n X m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법

- for문이 2개 필요하다!

- 행 우선 순회

  - ```python
    # i행의 좌표
    # j열의 좌표
    for i in range(len(Array)):
        for j in range(len(Array[i])):
            Array[i][j] #필요한 연산 수행
    ```

- 열 우선 순회

  - ```python
    # i행의 좌표
    # j열의 좌표
    for j in range(len(Array[0])):
        for i in range(len(Array)):
            Array[i][j] #필요한 연산 수행
    ```

- 지그재그 순회(그냥 넘어가자,,)

  - ```python
    # i행의 좌표
    # j열의 좌표
    for i in range(len(Array)):
        for j in range(len(Array[0])):
            Array[i][j + (m-1-2*j)*(i%2)] #필요한 연산 수행
    ```

- <u>델타를 이용한 2차 배열 탐색</u>

  - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
    - 델타 값은 한 좌표에서 네 방향의 좌표와 x, y 의 차이를 저장한 list로 구현
    - 델타 값을 이용하여 특정 원소의 상하좌우에 위치한 원소에 접근할 수 있음
    - 이 때, 2차원 list의 가장자리 원소들은 상하좌우 네 방향에 원소가 존재하지 않을 경우가 있으므로 index를 체크하거나 index의 범위를 제한해야 함
  - 연습문제1

  ```python
  arr = [[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1]]
  
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  
  
  def isWall(x, y):
      if x < 0 or x >= 5:
          return True
      if y < 0 or y >= 5: 
          return True
      return False
  
  def calAbs(y, x):
      if y-x > 0:
          return y-x
      else:
          return x-y
  
  for x in range(len(arr)):
      for y in range(len(arr[x])):
          for i in range(4):
              testX = x + dx[i]
              testY = y + dy[i]
              if not isWall(testX, testY):
                  sum += calAbs(arr[y][x], arr[testY][testX])
  print(f'sum = {sum}')
  ```

  

### C. 2차원 배열의 활용

- 전치 행렬

  - 행과 열의 값이 반대인 행렬을 의미

  ```python
  # i : 행의 좌표, len(arr)
  # j : 열의 좌표, len(arr[0])
  # 3*3 행렬
  arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
  
  for i in range(3):
      for j in range(3):
          if i < j:
              arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
  ```

  - 이 때, 모든 좌표에 대해 행과 열의 값을 바꾸게 되면 본래의 모습으로 돌아오기 때문에 이를 주의해야 함

- 부분집합 구하기
  - 비트 개수대로 for문 돌리기 
  ```python
  bit = [0, 0, 0]
  for i in range(2):
      bit[0] = i
      for j in range(2):
          bit[1] = j
          for k in range(2):
              bit[2] = k
              print(bit)
  ```

  - 비트 연산자

    - 0과 1로 이루어진 이진수에 대한 연산을 수행하는 연산자
    - 종류
      - `&` : 비트 단위로 AND 연산을 함
      - `|` : 비트 단위로 OR 연산을 함
      - `<<` : 피연산자의 비트 열을 왼쪽으로 이동시킴
      - `>>` : 피연산자의 비트 열을 오른쪽으로 이동시킴
    - `<<` 연산자
      - 1<<n = 2**n  즉, 원소가 n개일 경우의 모든 부분집합 갯수
    - `&` 연산자
      - i & (1<<j) : 1 | i에서 j번째 비트가 1인지 아닌지를 리턴
    - 비트연산자를 이용해 부분집합 생성하는 방법

    ```python
    arr = [1, 2, 3]
    n = len(arr)
    
    for i in range(1 << n): # 1<<n: 부분 집합의 개수
        for j in range(n): # 원소의 수만큼 비트를 비교함
            if i & (1 << j): # i의 j번째 비트가 1이면 j번째 원소 출력
                print(arr[j], end=",")
        print()
    ```

- 부분집합 합 구하기 (연습문제2)

```python
# n개의 정수를 입력받아 부분집합의 합이 0이 되는 경우 구하기

arr = [-7, -3, -2, 5, 8]
n = len(arr)

cnt = 0
for i in range(1, 1 << n): 
    sum = 0
    for j in range(n):
        if i & (1 << j):
            sum += arr[j]

    if sum == 0:
        cnt += 1 # 부분집합의 합이 0인경우 카운트 += 1
        for j in range(len(arr)): # 부분집합의 합이 0인 경우 i (여기서는 i == 14) 번째 부분집합을 표시
            if i & (1 << j):
                print(arr[j], end=" ") # -3 -2 5

        print() # 한 줄 띄우기
print(f'개수 : {cnt}') # 개수 : 1
```



##  검색(search)

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것
  - 탐색 키(search key) : 자료를 구별하여 인식할 수 있는 키
- 검색의 종류
  - 순차 검색
  - 이진 검색
  - 인덱싱

### A. 순차 검색(sequential search)

- 일렬로 되어 있는 자료를 순서대로 검색하는 방법

  - 가장 간단하고 직관적
  - 순차구조로 구현된 자료구조의 경우 유용
  - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행 시간이 급격히 증가하여 비효율적임

- 2가지 경우

  - <u>정렬되어 있지 않은 경우</u>

    - 검색과정
      - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 검색
      - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 리턴
      - 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패
    - 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
    - 평균 비교 회수 = (n+1)/2 >> <u>시간 복잡도 : O(n)</u>

    ```python
    def sequentialSearch(a, n, key):
        i = 0
        while i < n and a[i] != key:
            i = i + 1
    
        if i < n:
            return i
        else:
            return -1
    
    data = [4, 9, 11, 23, 2, 19, 7]
    key = 19
    print(sequentialSearch(data,len(data), key))
    # >> 19의 인덱스값인 5를 리턴
    ```

  - <u>정렬되어 있는 경우</u>

    - 검색과정
      - (오름차순 가정) 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료
    - 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
      - 정렬이 되어있으므로, 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어든다
    - <u>시간 복잡도 : O(n)</u>

    ```python
    def sequentialSearch2(a, n, key):
        i = 0
        while i < n and a[i] < key:
            i = i + 1
            
        if i < n and a[i]==key:
            return i
        else:
            return -1
    ```

    



### B. 이진 검색 (Binary Search)

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행
- 이진 검색을 하기 위해서는 <u>자료가 정렬된 상태여야 함</u>
- 시간복잡도 : O(logN)
- 검색과정
  - 자료의 중앙에 있는 원소를 고른다
  - 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다
  - 목표 값이 중앙 원소의 값보다 **작으면** 자료의 **왼쪽 반**에 대해서 새로 검색을 수행, **크다면** 자료의 **오른쪽 반**에 대해서 새로 검색을 수행
  - 찾고자 하는 값을 찾을 때까지 위 과정을 반복
- 구현
  - 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행
  - 이진 검색의 경우, 자료에 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬 상태로 유지하는 추가 작업이 필요함

```python
def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = (start + end)//2
        if key == a[middle]:
            return middle
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1

key = 23
data = [2, 4, 7, 9, 11, 19, 23]
print(binarySearch(data, key)) # 6
```

- 재귀 함수를 이용한 이진 검색 구현

```python
def binarySearch2(a, low, high, key):
    if low > high: # 검색실패
        return False
    else:
        middle = (low + high)//2
        if key == a[middle]: # 검색성공
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle+1, high, key)
```



### C. 인덱스 (대충 넘어가자,,)

- DB에서 유래, 테이블에 대한 동작 속도를 높임
- DB 외에서는 룩 업 테이블(Look up Table) 등의 용어로 사용함
- 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블 저장에 필요한 디스크 공간보다 작음
  - 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목은 갖고 있지 않기 때문
- List를 사용한 인덱스
  - 대량의 데이터를 매번 정렬하면, 프로그램의 반응은 느려질 수 밖에 없음. 이러한 대량 데이터의 성능 저하 문제를 해결하기 위해 List인덱스를 사용할 수 있음
- 원본 데이터에 데이터가 삽입될 경우 상대적으로 크기가 작은 인덱스 list를 정렬하기 때문에 속도가 빠름



## 정렬

### A. 셀렉션 알고리즘 (Selection Algorithm)

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
  - 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다.
- 선택과정
  - 셀렉션은 아래와 같은 과정을 통해 이루어진다.
    - 정렬 알고리즘을 이용하여 자료 정렬하기
    - 원하는 순서에 있는 원소 가져오기



### B. 선택 정렬

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

  - A. 셀렉션 알고리즘을 전체 자료에 적용한 것

- 정렬 과정
  - 주어진 리스트 중에서 최소값을 찾는다.
  - 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복
  - 미정렬원소가 하나 남은 상황에서는 마지막 원소가 가장 큰 값을 갖게 되므로 실행을 종료

- 시간 복잡도 : O(n**2)

- 구현

  ```python
  def selectionSort(a):
      for i in range(0, len(a)-1):
          min = i
          for j in range(i + 1, len(a)):
              if a[min] > a[j]:
                  min = j
          a[i], a[min] = a[min], a[i]
  ```

  