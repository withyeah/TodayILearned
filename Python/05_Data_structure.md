# 05_Data_structure

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

