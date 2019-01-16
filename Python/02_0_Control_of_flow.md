# 02_Control of flow

#### 1. enumerate()

```python
lunch = ['짜장면', '초밥']
for idx, menu in enumerate(lunch, start=3): #idx start값 줄 수 있음
    print(idx, menu)
# 3 짜장면
# 4 초밥
```



#### 2. dictionary에서 `for` 활용

```python
# 0. dictionary (key 반복)
for key in dict:
    print(key)

# 1. key 반복
for key in dict.keys():
    print(key)
    
# 2. value 반복    
for val in dict.values():
    print(val)

# 3. key와 value 반복
for key, val in dict.items():
    print(key, val)
```



#### 3. `break` `continue` `else` : 반복문 제어

```python
while test:
    statements
    if test:
        break            # 바로 루프를 빠져나감. else 문 생략.
        continue         # 바로 루프 상단에 있는 test 로 이동.
else:
    statements           # break 를 만나지 않고 루프를 종료할 경우 실행.
```

##### 	<u>`continue` : 코드실행 건너뛰기</u>

- `continue`문은 continue 이후의 코드를 수행하지 않고 다음 요소를 선택해 반복을 계속 수행

- `break` 와 약간 다른점은 continue 는 제어흐름(반복)을 유지한 상태에서 코드의 실행만 건너뛴다.

- ```python
  for i in range(6):
      if i % 2 == 0:
          continue
      print(f'{i}는 홀수다.')
  ```

  ```python
  1는 홀수다.
  3는 홀수다.
  5는 홀수다.
  ```