# 04_Recursive function

20190117



## A. 재귀함수

`반복(루프)를 위해 직접 또는 간접적으로 자기 자신을 호출하는 함수`

```python
# 리스트 sum()
def my_sum(n):
    print(n)
    if not n:
        return 0
    else:
        return n[0] + my_sum(n[1:])
```

```python
# factorial()
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return n
```

> 파이썬의 최대 재귀 깊이는 1,000번



```python
# 피보나치 수열 (재귀)
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```

```python
# 피보나치 수열 (반복문)
def fib_loop_2(n):
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
```

> 재귀함수를 작성시에는 반드시 `base case`가 존재해야 한다

> for문은 대부분의 상황에서 재귀를 대신할 수 있으며 메모리 사용량과 실행 시간에서 더 효율적