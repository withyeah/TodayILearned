# Queue_lecture_note

20190225



## Queue

### A. 큐

- 선입선출구조 (FIFO : First In First Out)

  - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소는 가장 먼저 삭제된다
  - 예시: 서비스 대기행렬

- 머리(front) <<<<< 꼬리(Rear)

- 큐의 기본 연산

  - 삽입 : enQueue
  - 삭제 : deQueue

- 큐의 주요 연산

  |     연산      | 기능                                                         |
  | :-----------: | ------------------------------------------------------------ |
  | enQueue(item) | 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산                  |
  |   deQueue()   | 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산           |
  | createQueue() | 공백 상태의 큐를 생성하는 연산                               |
  |   isEmpty()   | 큐가 공백상태인지를 확인하는 연산 (front == end 일 때 empty) |
  |   isFull()    | 큐가 포화상태인지를 확인하는 연산                            |
  |    Qpeek()    | 큐의 앞쪽(front)에서 원소를 삭제 없이 반환하는 연산          |



### B. 선형 큐

- 선형큐

  - 1차원 배열을 이용한 큐
    - 큐의 크기 == 배열의 크기
    - front : 저장된 첫 번째 원소의 인덱스
    - rear : 저장된 마지막 원소의 인덱스
  - 상태표현
    - 초기 상태 : front = rear = -1
    - 공백 상태 : front = rear
    - 포화 상태 : rear = n-1 (n: 배열의 크기, n-1: 배열의 마지막 인덱스)

- 초기 공백 큐 생성

  - 크기 n인 1차원 배열 생성
  - front와 rear를 -1로 초기화

  

> C스타일
>
> ```python
> SIZE = 100
> Q = [0]*SIZE
> front, rear = -1, -1
> 
> def isFull():
>     global rear
>     return rear == len(Q)-1
> 
> def isEmpty():
>     global front, rear
>     return front == rear
> 
> def enQueue(item):
>     global rear
>     if isFull(): print('Queue_Full')
>     else:
>         rear += 1
>         Q[rear] = item
> 
> def deQueue():
>     global front
>     if isEmpty(): print('Queue_Empty')
>     else:
>         front += 1
>         return Q[front]
> 
> def Qpeek():
>     global front
>     if isEmpty(): print('Queue_Empty')
>     else: return Q[front+1]
> 
> enQueue(1)
> enQueue(2)
> enQueue(3)
> print(Qpeek())
> print(deQueue())
> print(deQueue())
> print(deQueue())
> ```



> python 스타일
>
> ```python
> Q = []
> 
> Q.append(1)
> Q.append(2)
> Q.append(3)
> 
> print(Q.pop(0))
> print(Q.pop(0))
> print(Q.pop(0))
> ```

> 참고 : 큐 라이브러리 있음
>
> ```python
> import sys
> import queue
> 
> q = queue.Queue()
> q.put(1)
> q.put(2)
> q.put(3)
> print(q.get())
> print(q.get())
> print(q.get())
> ```

- 선형 큐의 문제점



### C. 원형 큐

- 초기 공백 상태
  - front = rear = 0
- Index의 순환
  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함
  - 이를 이해 나머지 연산자 mod를 사용함
- front 변수
  - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
- 삽입 위치 및 삭제 위치
  - 표
- 원형 큐의 구현

```python
SIZE = 4
Q = [0]*SIZE
front, rear = 0, 0

def isFull():
    global front, rear
    return (rear+1) % len(Q) == front

def isEmpty():
    global front, rear
    return front == rear

def enQueue(item):
    global rear
    if isFull(): print('Queue_Full')
    else:
        rear = (rear+1) % len(Q)
        Q[rear] = item

def deQueue():
    global front
    if isEmpty(): print('Queue_Empty')
    else:
        front = (front+1)%len(Q)
        return Q[front]

def Qpeek():
    global front
    if isEmpty(): print('Queue_Empty')
    else: return Q[front+1]

enQueue(1)
enQueue(2)
enQueue(3)
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(4)
print(deQueue())
```



### D. 연결 큐



### E. 우선순위 큐

