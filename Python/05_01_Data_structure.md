# 05_01_Data_structure

20190118

##### 

## 문자열 메소드 활용하기

### A. 변형

- `capitalize()` : 맨 앞 대문자, 나머지 소문자로 반환

- `title()` : `'` 나 공백 이후를 대문자

- `upper()` : 모두 대문자

- `lower()` : 모두 소문자

- `swapcase()` :  대 소문자 swap

- `join(iterable)` 

  - ```python
    '!'.join('배불러')
    ```

  - ```python
    a = ['hi', 'bye']
    '_'.join(a)
    ```

- `replace( old, new, count )` :  count 지정하면 앞에서부터 해당 갯수만큼만 시행

- `strip()` `lstrip()` `rstrip()` : 괄호 안 strip할 chars, 지정X > 공백 제거



### B. 탐색 및 검증

- `find(x)` : x의  첫 번째 위치를 리턴. 없으면 -1 
- `index(x)` : x의 첫 번째 위치를 리턴. 없으면 오류
- 참/거짓 반환
  - `isalpha()` : 문자열이 오직 알파벳으로만 구성 (공백 포함 시 F)
  - `isdecimal()` : only decimal #
  - `isdigit()`
  - `isnumeric()`
  - `isspace()` : 모두 공백이면 T
  - `isupper()` : 모두 대문자
  - `istitle()` : 모든 문자열이 title스타일
  - `islower()` : 모두 소문자
- `split()` : 괄호 안 문자를 단위로 나누어 **리스트로 리턴** 
  - 공백있으면 공백 기준
  - input이 공백 없는 스트링이면 글자 단위로 나눔



## 리스트 메소드 활용하기

### A. 값 추가 및 삭제

- `append(x)`

- `extend(iterable)` : 리스트에 iterable한 값을 붙일 수 있음

  - ```python
    cafe.extend(['angel','bbaek'])
    #리스트 안 내용만 어펜드 됨
    ```

  - ```python
    cafe.append(['caffebenne'])
    #리스트 자체가 어펜드 됨
    ```

  - ```python
    cafe.extend('twosome')
    # t w o s o m e이 각각 어펜드
    ```

- `insert(i, x)` : i의 위치에 x를 추가, 길이를 넘어서는 인덱스는 무조건 마지막에 하나만 붙는다.

- `remove(x)` : 값이 x인 것을 삭제. 리스트에 값 없으면 오류 발생

- `pop(i)` : i 위치에 있는 값을 리턴하고 삭제, i 미지정 > 마지막 항목



### B. 탐색 및 정렬

- `index(x)` : x값을 찾아 그 index를 반환, x없을 시 오류 발생 
- `count(x)` : x의 갯수 리턴
- `sort()` : 원본 리스트를 변형시키고 none을 리턴 (sorted는 원본 변형 X)
  - .sort(reverse=True)
- `reverse()` : 반대로 뒤집기 (정렬 아님)



### C. 복사

- a = b 하고 b를 수정했을 때 a가 바뀔까?

  - a가 mutable (리스트, 딕셔너리 등) 이면 바뀜, immutable (int) 면 X

- 얕은 복사

  - ```python
    a = [1, 2, 3]
    b = a[:] # or b = list(a)
    b[0] = 5
    print(a)
    # [1, 2, 3]
    ```

  - ```python
    a = [1, 2, [1, 2]]
    b = a[:]
    b[2][0] = 3
    print(a)
    # [1, 2, [3, 2]]
    # > 중첩된 상황에는 a에 영향을 줌
    ```

- 깊은 복사 (내부에 있는 모든 객체까지 새롭게 값이 변경)

  - ```python
    import copy
    a = [1, 2, [1, 2]]
    b = copy.deepcopy(a)
    b[2][0] = 3
    print(a)
    # [1, 2, [1, 2]]
    ```



### D. 삭제

- `clear()` : 리스트의 모든 항목을 삭제



# List Comprehension

> [ 식 for 변수 in 리스트 ]

```python
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
for name in names:
    spl = name.split()
    first_name = spl.pop(0)
    print(first_name.lower())

# list comprehension
first_name = [name.split()[0].lower() for name in names]
print(first_name)
```

 

## A. 활용법

- 여러개의 for 혹은 if 문을 중첩적으로 사용 가능

- 리스트 표현식에 for 여러 개일 때 뒤에서 앞 순서로 처리됨

  - [식 for 변수1 in 리스트1 if 조건식1 for 변수2 in 리스트2 if 조건식2]
  - [식 for 변수 in 리스트 if 조건식]
  - [식 if 조건식 else 조건식 for 변수 in 리스트 ]