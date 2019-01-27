# 05_02_Dictionary_data_structure



## A. 딕셔너리 메소드 활용

### 추가 및 삭제

- `pop(key, default)` : key가 딕셔너리에 있으면 리턴하고 제거, 없으면 default를 반환. default가 없는 상태에서 key가 없으면 키에러

- `update({key: value})` : key, value 페어를 추가. key가 이미 존재한다면 value를 덮어씀

  - return None

  - ```python
    특이한거 발견
    >>> dust
    {'서울': 72, '경기': 82, '대전': 29, '중국': 200}
    >>> dust.update({'부산', '제주'})
    >>> dust
    {'서울': 72, '경기': 82, '대전': 29, '중국': 200, '부': '산', '제': '주'}
    ```

- `get(key, default)` : key를 통해 value를 가져옴. default는 기본적으로 None > key error발생하지 않음



### Dictionary comprehension

```python
# 다음의 딕셔너리에서 미세먼지 농도가 80초과는 나쁨 80이하는 보통으로 하는 value를 가지도록 바꿔봅시다.
# 예) {'서울': '나쁨', '경기': '보통', '대전': '나쁨', '부산': '보통'}
dust = {'서울': 72, '경기': 82, '대전': 29, '중국': 200}
dust_air = {key: '나쁨' if value > 80 else '보통' for key, value in dust.items()}
print(dust_air)

#{'서울': '보통', '경기': '나쁨', '대전': '보통', '중국': '나쁨'}
```

```python
{key: '매우나쁨' if value > 150 else '나쁨'
                if value > 80 else '보통'
                if value > 30 else '좋음' for key, value in dust.items()}
# if 위에서부터 돌음!
```



## B. map(), zip(), filter()

### map(function, iterable)

- iterable의 요소를 지정된 함수로 처리해주는 함수

  - iterable : list, dict, set, str, bytes, tuple, range

- return은 map_object형태

- map은 원본을 변경하지 않고 새 값을 생성함

- ex) list(map( 함수, 리스트 ))

- for문으로 반복하면서 요소를 변환하기 어려울 때 map을 사용하면 편리

- function에는 사용자 정의 함수도 들어갈 수 있음

  - ```python
    def cube(n):
        return n**3
    a = [1, 2, 3]
    list(map(cube, a))
    #[1, 8, 27]
    ```



### zip(*iterables)

- 복수의 iterable한 것들을 모아줌

- 튜플의 모음으로 구성된 zip object를 리턴

  ```python
  girls = ['jane', 'iu', 'mary']
  boys = ['justin', 'david', 'kim']
  list(zip(girls, boys))
  #[('jane', 'justin'), ('iu', 'david'), ('mary', 'kim')]
  ```

  ```python
  #dict comprehension
  {girl: boy for girl in girls for boy in boys}
  # dictionary에서 key는 유일한 값
  #{'jane': 'kim', 'iu': 'kim', 'mary': 'kim'}
  ```

  ```python
  {girl: boy for girl, boy in zip(girls, boys)}
  #{'jane': 'justin', 'iu': 'david', 'mary': 'kim'}
  ```

- zip은 길이가 같을 때 사용해야 함. 길이가 짧은 것으르 기준으로 구성

- 패킹/언패킹

  - ```python
    letters = ['a', 'b', 'c']
    nums = [1, 2, 3]
    zip_list = list(zip(letters, nums))
    print(zip_list)
    #[('a', 1), ('b', 2), ('c', 3)]
    ```

    ```python
    new_letters, new_nums = zip(*zip_list)
    print(new_letters) #('a', 'b', 'c')
    print(new_nums) #(1, 2, 3)
    ```

    

### filter( function, iterable )

- iterable에서 function의 리턴값이 참인 것들만 구성하여 반환

  - ```python
    def even(n):
        return not n % 2
    a = [1, 2, 3, 4]
    list(filter(even, a))
    # false는 버리고 true인 애들만 반환
    ```



## C. 세트 메소드 활용

### 추가 및 삭제 pop 제외 return None

- `add(elem)` : elem을 세트에 추가/ 여러번 해도 한 번만 추가됨

- `update(*others)` : 여러가지 값(iterable)을 순차적으로 추가

  - ```python
    a = {1, 2, 3}
    a.update((5, 5, 5, 2), {7, 9}, [14, 5, 532])
    # iterable한 값만 들어간다 *정수 넣으면 안됨
    print(a)
    #>{1, 2, 3, 532, 5, 7, 9, 14}
    ```

- `remove(elem)` : elem을 삭제, 없으면 키에러

- `discard(elem)` : elem을 삭제, 없어도 키에러X

- `pop()` : 임의의 원소를 리턴하고 삭제

  - 세트기 때문에 pop(i)처럼 인덱스 값을 줄 수 없음 무조건 랜덤 원소 리턴