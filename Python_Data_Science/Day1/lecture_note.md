# **Python 자료구조 및 스크랩핑, Numpy**

2019.09.24.화



## 1. 자료구조

### 1) List 

- 인덱싱

- 슬라이싱

- 덧셈 연산 : 덧셈 연산을 하더라도 따로 어딘가 변수에 할당해 주지 않으면 기존 변수는 변화가 없다.

- 곱셈 연산 : 기준 리스트에 n을 곱했을 때, 같은 리스트를 n배만큼 늘려준다.

- in 연산 : 포함 여부를 확인하는 연산

- 리스트 추가 삭제 함수

- 패킹 && 언패킹

  - 패킹 : 한 변수에 여러 개의 데이터를 할당하는 것.

  - 언패킹 : 한 변수의 데이터를 각각의 변수로 반환하는 것

    ```python
    t = [1, 2, 3]
    a, b, c = t
    print(t)
    print(a, b, c)
    ```

    > 길이 3인 리스트를 4개의 변수로 언패킹하면?



### 2) Stack

- LIFO (Last In Firtst Out)
- 푸시 Push
- 팝 Pop

  ```python
  a = [1, 2, 3, 4, 5]
  a.append(10)
  print(a)
  a.append(20)
  print(a.pop())
  print(a)
  print(a.pop())
  ```

> 입력한 텍스트를 역순으로 추출하기
>
> ```python
> word = input()
> word_list = list(word)
> print(word_list)
> 
> result = []
> for _ in range(len(word_list)):
>     result.append(word_list.pop())
> 
> print(result)
> print(word[::-1])
> ```



### 3) Queue

- FIFO (First In First Out)



### 4) Tuple && Set 



### 5) Dictionary

- 딕셔너리 변수 = {키1: 값1, 키2: 값2, 키3: 값3}



## 2. 함수

### 1) Lambda

- 함수형 프로그래밍

  ```python
  def func1(x, y):
      return x + y

  print(func1(1, 4))

  f = lambda x, y: x+ y
  print(f(1, 4))
  ```

- 익명함수

  ```python
  # gugudan
  for x in range(1, 10):
      for y in range(1, 10):
          print(str(x) + " * " + str(y) + " = " + str(x*y))
  
  # lambda로
  result = lambda x, y : f'{x} * {y} = {x*y}'
  for x in range(2, 10):
      for y in range(1, 10):
          print(result(x, y))
  ```

  



### 2) map()

- 일반적으로 시퀀스 자료형에 사용

- 연속 데이터를 저장하는 시퀀스형에서 요소마다 같은 기능을 적용할 때 사용

  ```python
  ex = [1, 2, 3, 4, 5]
  f = lambda x : x ** 2
  result = map(f, ex)            # ex의 모든 요소에 f를 적용하겠다
  print("Map result1 =", result) # map object 리턴 
  print("Map result2 =", list(result))
  ```

  

### 3) list comprehension

- [<expression> for <element> in <iterable>]

  ```python
  ex = [1, 2, 3, 4, 5]
  multiples = [n**2 for n in ex]
  print("Map result3 =", multiples)
  ```

  

### 4) filtering

- else

  ```python
  ex = [1, 2, 3, 4, 5]
  print("Map result4 =", list(map(lambda x : x** 2 if x % 2 == 0 else x, ex)))
  result2 = [x ** 2 if x % 2 == 0 else x for x in ex]
  print("Map result5 =", result2)
  ```



### 5) reduce

- 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수

  ![image](https://user-images.githubusercontent.com/45819975/65483926-df2bc280-ded8-11e9-874c-cf223a9b3055.png)
  
```python
  from functools import reduce
  
  ex = [1, 2, 3, 4, 5]
result3 = reduce(lambda x, y : x + y, ex)
  print("Reduce result1 =", result3)
  
  x = 0
for y in ex:
      x += y
  
  print("Reduce result2 =", x) 
  ```



## 3. 웹 스크래핑

