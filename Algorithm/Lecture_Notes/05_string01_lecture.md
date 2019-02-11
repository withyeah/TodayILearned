# 알고리즘 D05_20190128

> 문자열 / 패턴매칭 / 문자열 암호화 / 문자열 압축 / 실습1,2

20190129 



## 문자열(string)

### A. <u>문자의 표현</u>

- 코드체계 ㅣ ex)영어는 대소문자 합쳐서 52이므로 6비트(64가지)면 모두 표현할 수 있음
- ASCII (American Standard Code for Information Interchange) : 문자 인코딩 표준
  - 7bit 인코딩 -128문자를 표현, 95개의 출력 가능한 문자 + 33개의 출력 불가능한 제어문자
    - bit (0/1) : 정보의 최소 단위
    - Byte (8bit) : 영문자 하나의 단위 / 7bit + 1 Panity bit
- 확장아스키 : panity bit 안써서 추가로 128개 > 지금은 안씀
- 유니코드 : 다국어 처리를 위한 표준
  - python 인코딩 | 유니코드 UTF-8
- endian (?)
  - big-endian, little-endian

> 참고) 정수의 표현 (보수 : NOT) (20190129)
>
> - 부호와 절대치 - 0, -0 0이 두개
> - 1의 보수 - 0, -0 0이 두개
> - 2의 보수 - 한 자리 더 표현할 수 있음 + 연산 가능 의 이점이 있기 때문에 2의 보수를 쓴다.



### B. <u>문자열 뒤집기</u> -> 팰린드롬에 활용 가능

- 자기 문자열에서 뒤집는 방법
- 새로운 빈 문자열을 만들어 소스의 뒤에서부터 읽어서 타겟에 쓰는 방법

```python
# C스타일로 reverse
def my_strrev(ary):
    str = list(ary)
    for i in range(len(str)//2):
        t = ary[i]
        str[i] = str[len(str)-1-i]
        str[len(str)-1-i] = t
    ary = "".join(str)
    return ary

ary = "abcde"
ary = my_strrev(ary)
print(ary)

# 파이썬스타일로 reverse
s = "Reverse this strings"
s = s[::-1]
print(s)
```



### C. <u>문자열 비교</u>(p.124)

- c - strcmp() 함수 / Java - equals() 메소드 / python - ==, is연산자
- 문자열 비교에서 == 연산은 메모리 참조가 같은지를 묻는 것
- == 연산자는 내부적으로 특수 메서드 `__eq__()` 를 호출

```python
# python으로 string compare 함수 구현하기
def strcmp(str1, str2):
    i = 0
    # str 길이 다르면 일단 False!
    if len(str1) != len(str2):
        return False
    else:
        while i < len(str1) and i < len(str2):
            if str1[i] != str2[i]:
                return False
            i += 1
    return True

a = 'abc'
b = 'abc'
print(strcmp(a, b))   # True
print(a == b)         # True
```



### D. <u>문자열 숫자를 정수로 변환하기</u> (atoi = array to integer)

- c - atoi(), itoa() / java - parse메소드 / python - int() float() str() repr()

```python
# python으로 atoi() 구현하기
def atoi(string):
    value = 0
    i = 0
    while (i < len(string)):
        c = string[i]
        # 문자끼리 비교 : python-유니코드넘버 / c-ascii
        if c >= '0' and c <= '9':
            # ord : ascii로 변환 / ord('0') == 48
            # c = 2 일때 ord(c) == 50 > 50-48 = 2
            digit = ord(c) - ord('0')
        else:
            break
        # * 10 해서 1의 자리에 계속 추가
        value = (value * 10) + digit
        i += 1
    return value

a = '123'
print(type(a))   # str
b = atoi(a)
print(type(b))   # int
c = int(a)
print(type(c))   # int
```



### E. <u>문자열 교체하기</u>

- 원래는 교체부분 뒷자리를 잘라서 다른 곳에 보관하고 교체한 후 다시 붙여야 함

```python
# python 
str1 = 'abc 1, 2 ABC'
print(str1)
str1 = str1.replace('1, 2', 'one, two')
print(str1)  # abc one, two ABC
```



### F. <u>integer to array</u>

```python
# 내 코드 : 망함!
def itoa(value):
    list = []
    while value > 0:
        list.append(value % 10)
        value //= 10
    return ''.join(list[::-1])

print(itoa(123))
```

```python
# 강사님 코드
def itoa(x):
    str = list()
    y = 0
    while True:
        y = x % 10
        str.append(chr(y + ord('0')))
        x //= 10
        if x == 0:
            break

    str.reverse()
    str = ''.join(str)
    return str

x = 123
print(x, type(x))        # 123 <class 'int'>
str1 = itoa(x)
print(str1, type(str1))  # 123 <class 'str'>
```

---



## 패턴 매칭 find()

패턴매칭 : 본문에서 특정한 문자열을 찾는 것

### A. 고지식한 패턴 검색 알고리즘 (Brute Force)

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식
- 시간복잡도 : 최악의 경우 텍스트의 모든 위치에서 패턴을 비교해야 하므로 O(MN)이 됨

```python
# 슬라이드에 있는 방식
p = 'is'
t = 'This is a book~!'
M = len(p)
N = len(t)

def BruteForce(p, t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M
    else:
        return -1

print(BruteForce(p, t))
```

```python
# 추가 for문 활용
파일에서 보고 추가
```

```python
# 추가 while 문 활용
```



### B. KMP알고리즘(p.136)

- 불일치가 발생한 텍스트 문자열의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행

  1. <u>패턴을 전처리</u>하여 배열 next[M]을 구해서 잘못된 시작을 최소화함 | next[M] : 불일치가 발생했을 경우 이동할 다음 위치
  2. 시간 복잡도 : O(M+N)

- 전처리 : 패턴의 각 위치에 대해 매칭에 실패했을 때 돌아갈 곳을 준비 해 둠

  ```
  [a, b, c, d, a, b, c, e, f]
  > 전처리
  [-1, 0, 0, 0, 0, 1, 2, 3, 0]
  >> e에서 매칭 실패하면 3번 인덱스로 돌아가야 한다는 뜻
  ```



### C. 보이어-무어 알고리즘(p.139)

- 오른쪽에서 왼쪽으로 비교

- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘

- 패턴의 오른쪽 끝에 있는 문자가 불일치하고, 이 문자가 패턴 내에 존재하지 않는 경우, 이동거리는 패턴의 길이만큼이 됨

- 패턴 string의 skip배열을 미리 준비할 수 있음

  ```
  찾을 패턴이 'water'인 경우의 skip 배열
  w, a, t, e, r, 다른 모든 문자
  0, 1, 2, 3, 4, 5
  ```

- 시간복잡도 : 일반적으로 O(n) 보다 작다

  - 최악의 경우 : O(mn)



> note* 20190210
>
> 여기부터는 교재에 없는 내용 ( 찾아서 복습 해야함 )

### D. 카프-라빈 알고리즘 

##### `(교재 A반_SW문제해결응용_2 p.31 참고)`

- 해쉬값을 찾아서 비교
- 찾고자하는 문자열에서 한 글자씩 이동하며 패턴 길이만큼 읽어서 해쉬값을 계산하는 게 아니라
- 새로 추가되는 문자와 그전에 읽었던 값을 이용하여 해쉬값을 구함
- ex) 6843 > 8432 : 6 버림 ~ 843*10 ~ + 2추가
- 패턴이 문자열이며 길어지면 길이를 일정 자리수로 맞추기 위해 mod연산을 취해 준다
- 따라서 해쉬 값이 일치하더라도 실제 패턴이 일치하지 않을 수 있기 때문에 해쉬 값이 일치하면 문자열 일치를 검사해야 한다. (이를 해쉬 충돌이라고 함)



- bit 열의 암호화
  - 배타적 논리합 (exclusive-or) 연산 사용

  ```python
  def Bbit_print(a): 
    for i in range(7, -1, -1):
        if a & (1<<i):
            print(1, end='')
        else:
            print(0, end='')
        print()
    

  a = 0x86
  key = 0xAA
  print("a      ==>", end=' ')
  Bbit_print(a)

  print("a^=key ==>", end=' ')
  a ^= key
  Bbit_print(a)
     
  print("a^=key ==>", end=' ')
  a ^= key
  Bbit_print(a)
  ```



- 문자열 압축
  - Run-length encoding 알고리즘


