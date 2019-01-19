# 05_02_Dictionary_data_structure



## A. 딕셔너리 메소드 활용

### 추가 및 삭제

- `pop(key[, default])` : key가 딕셔너리에 있으면 리턴하고 제거, 없으면 default를 반환. default가 없는 상태에서 key가 없으면 키에러
- `update({key, value})` : key, value 페어를 추가. key가 이미 존재한다면 value를 덮어씀
- `get(key[, default])` : key를 통해 value를 가져옴. default는 기본적으로 None > key error발생하지 않음



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
```



## B. map(), zip(), filter()

### map(function, iterable)

- iterable의 요소를 지정된 함수로 처리해주는 함수
  - iterable : list, dict, set, str, bytes, tuple, range
- return은 map_object형태
- map은 원본을 변경하지 않고 새 값을 생성함
- ex) list(map( 함수, 리스트 ))
- for문으로 반복하면서 요소를 변환하기 어려울 때 map을 사용하면 편리
- 