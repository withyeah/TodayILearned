# 알고리즘 Intro 

### 20190114 월요일 

김한욱 교수님 / hanoogi@naver.com / 



## A. Introduction

### 1. 삼성 SW 시험

- `Expert` : 다 맞아도 2% 정도만 붙여줌
- `Pro`: 함수이름과 매개변수만 알려주고 함수 구현, 문제 (코딩량 어마어마, 코딩 구현 많이 해 본 사람만 가능)
- `AD` : 대부분 완전검색(재귀), 가ㅏㅏㅏ끔 DP(동적계획법)
- `IM` : 배열 + 다중 for문 (2~3중)



### 2. 참고사이트

- swexpertacademy.com

  > A형 - IM~AD
  >
  > B형 - AD~Pro
  >
  > C형 - Pro~Expert



### 3. C언어의 역사 (갑자기?

> `ALGOR` - `B` - `C` (데니스 리치) - `Java` /Oracle - JRE, JVM
>
> ​                      |                        |- `C++` (객체지향) 
>
> ​                      |                        |-`C#` (Java + C++) /MS -CLR
>
> UNIX 운영체제를 만들기 위해 C를 만듬
>
> - `android` : Java 바탕
> - `iOS` : objective-C 바탕



---





## B. 알고리즘

### 1. 알고리즘

> .sort 메소드 쓰면 되는데 알고리즘 왜하냐 >> 그게 어떻게 동작하는지 알기 위해
> 

 `알고리즘` : 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법.

> 	  주로 컴퓨터용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말함.
>
> > `어떠한 문제를 해결하기 위한 절차`
>
> 알고리즘 설계할 때는 일단 종이에 손으로 푸는 게 좋다 > 그 후 코딩



> <u>컴퓨터 분야에서 알고리즘을 표현하는 방법 2가지</u>
>
> - 수도코드
> - 순서도



  **<u>좋은 알고리즘</u>** (p.7)

 - 정확성 : 얼마나 정확하게 동작하는가
 - 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
 - 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
 - 단순성 : 얼마나 단순한가
 - 최적성 : 더 이상 개선할 여지없이 최적화되었는가



 알고리즘 성능 분석 필요

 > ##### **<u>시간 복잡도 (Time Complexity) 표기법</u>** > `빅-오(O) 표기법`
 >
 > - O( 3n + 2 ) = O( n )
 > - O( 2n******2 + 10n + 100 ) = O( n******2 )
 > - O( 4 ) = O ( 1 )
 >
 > > ex) for 문 2중으로 n 번 명령? > O( n**2 )

 > <u>p.11 다양한 시간 복잡도의 비교</u>
 >
 > > **`Polynomial`** 현실적 계산 가능
 > >
 > > O( log n ) - 이진 탐색
 > >
 > > O( n ) - 순차 탐색
 > >
 > > O( n log n ) - Quick, Merge, heap
 > >
 > > O( n**2 ) - 선택 Bubble, 삽입
 > >
 > > O( n**3 ) - 모든쌍 최단 경로 (프로이드)
 > >
 > > ---
 > >
 > > **`Nondeterministic Polynomial`** 현실적 계산 어려움 (n이 커지면)
 > >
 > > O( 2**n ) - 부분집합
 > >
 > > O( n! ) - TSP
 >
 > 보통 1초에 10억개 연산 O( n )



### 2. 배열

 **`배열`** : <u>일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조</u>

 > 배열을 사용하면 하나의 선언을 통해 둘 이상의 변수 선언 가능
 >
 > > 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있음



 **<u>1차원 배열</u>**

> 별도의 선언 방법이 없으면 변수에 처음 값을 할당할 때 생성
>
> > 우리는 C 스타일로 배열 쓸 것임



 - <u>연습문제 1</u> `Gravity` ( p. 16 ) > IM레벨

 > 2중 for문 + 리스트
 >
 > ```python
 > # gravity.py
 > data = [7,4,2,0,0,6,0,7,0]
 > result = 0
 > maxHeight = 0
 > for i in range(len(data)):
 >     #i의 최대 낙차 값은 len(data) - (i+1)
 >     #i이후의 모든 행을 검사한다.
 >     maxHeight = len(data) - (i + 1)
 >     for j in range(i+1, len(data), 1):
 >         if data[i] <= data[j] : #아래 행이 i행보다 상자가 많을 때, 최대낙차값을 1감소시킴
 >             maxHeight -= 1
 >     if result < maxHeight:
 >         result = maxHeight
 > print(result)
 > ```

 - <u>연습문제 2</u> `Baby-gin Game` ( p.19 )

 > greedy하게 푸는 방법은 다양함 > 위험 (될 수도 안 될 수도)
 >
 > 완전검색하면 정답은 무조건 맞추게 돼있다.
 >
 > 완전검색 - 6! 가지수를 전부 검증
 >
 > > 밑에 `순열`에 코드 있음



 **`완전검색`** : <u>해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법</u>

 > Brute-force / generate_and_test 기법이라고도 함
 >
 > 모든 경우의 수를 테스트한 후, 최종 해법을 도출
 >
 > 일반적으로 경우의 수가 상대적으로 작을 때 유용
 >
 > > 수행 속도는 느리지만, 해답을 찾지 못할 확률 낮음
 > >
 > > 우선 완전 검색으로 접근하여 해답 도출 후 다른 알고리즘으로 성능개선하는 것이 좋음



**`순열 (Permutation)`** 

> 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열
>
> 서로 다른 n개 중 r개를 택하는 순열 == nPr
>
> - nPr = n * (n-1) * (n-2) **...* * (n-r+1)
> - nPn = n! (Factorial)
>
> ex) {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수 p.25

> `Baby-gin Game`
>
> ```python
> def babygin(data):
>     for i1 in range(6):
>         for i2 in range(6):
>             if i2 != i1:
>                 for i3 in range(6):
>                     if i3 != i1 and i3 != i2:
>                         for i4 in range(6):
>                             if i4 != i1 and i4 != i2 and i4 != i3:
>                                 for i5 in range(6):
>                                     if i5 != i1 and i5 != i2 and i5 != i3 and i5 != i4:
>                                         for i6 in range(6):
>                                             if i6 != i1 and i6 != i2 and i6 != i3 and i6 != i4 and i6 != i5:
>                                                 chk = 0
>                                                 if data[i1] == data[i2] and data[i2] == data[i3]:
>                                                     chk += 1
>                                                 if data[i4] == data[i5] and data[i5] == data[i6]:
>                                                     chk += 1
>                                                 if data[i1] + 1 == data[i2] and data[i2] + 1 == data[i3]:
>                                                     chk += 1
>                                                 if data[i4] + 1 == data[i5] and data[i5] + 1 == data[i6]:
>                                                     chk += 1
>                                                 if chk == 2:
>                                                     print("Baby-gin")
>                                                     return
>                                                 else:
>                                                     print("NOT Baby-gin")
> 
> data = [6, 6, 7, 7, 6, 7]
> babygin(data)
> ```



**`탐욕(Greedy) 알고리즘`**

>최적해를 구하는 데 사용되는 근시안적인 방법
>
>여러 경우 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달한다.
>
>각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적, `BUT` 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 해서 <u>그것이 최적이라는 보장은 없음</u>
>
>일반적으로 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면  Greedy 접근

1. `해 선택` : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합(Solution Set)에 추가
2. `실행 가능성 검사` : 새로운 부분해 집합이 실행 가능한지를 확인, 문제의 제약 조건을 위반하지 않는지 검사
3. `해 검사` : 새로운 부분해 집합이 문제의 해가 되는지를 확인. 아직 전체 문제의 해가 완성되지 않았다면 1.의 해 선택부터 다시 시작한다.



> Baby-gin game - Greedy로 풀기 / Counting 방법
>
> #continue 쓰는 이유 : TripletX2 또는 RunX2 경우 다시 while로 올려주기 위해서
>
> ```python
> num = 123123
> c = [0] * 12  #밑에 i+2 > 9 들어갔을 때 11되기 때문에 12자리 생성
> for i in range(6):
>     c[num % 10] += 1  #숫자 카운트
>     num //= 10        #1의 자리 날림
> 
> i=0
> tri=0
> run=0
> while i < 10:
>     if c[i] >= 3:    #같은 숫자 3개 이상일 때
>         c[i] -= 3    #3개를 지운다!
>         tri += 1     #트리플렛 += 1
>         continue     #continue 무조건 넣어야 함
>     if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:   #3자리 연속일 때
>         c[i] -= 1      
>         c[i+1] -= 1    #i, i+1, i+2 한 개씩 카운트에서 빼줌
>         c[i+2] -= 1
>         run += 1      
>         continue     #continue 무조건 넣어야 함
>     i += 1
> if tri + run == 2: print("Baby-gin")
> else: print("NOT Baby-gin")
> ```



### 3. 정렬

**`정렬`** : <u>2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값(오름차순 : ascending), 혹은 그 반대의 순서대로(내림차순 : descending) 재배열하는 것</u>

**`키`** : 자료를 정렬하는 기준이 되는 특정 값

> ex) 서류를 번호대로 정렬, 카드를 번호대로 정렬

> <u>대표적인 정렬 방식의 종류</u>
>
> - 버블 정렬
> - 카운팅 정렬
> - 선택 정렬 : 제일 작은거 찾아서 제일 앞으로 
> - 퀵 정렬
> - 삽입 정렬 : 책 정리
> - 병합 정렬

#### <u>1) 버블 정렬 (Bubble Sort)</u>

> - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
>
> - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬
>
> - 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같아서 버블정렬
>
> - 한 패스 지날 때마다 비교횟수가 1씩 줄어듦
>
> - 원소가 N개면 N-1번의 패스가 필요
>
> - > <u>시간 복잡도 : O( n**2 )</u>
>
> ```python
> def bubbleSort(data):
>     for i in range(len(data)-1, 0 ,-1):
>         for j in range(0, i):
>             if data[j] > data[j+1]:  # 부등호 반대로 하면 내림차순 정렬
>                 data[j], data[j+1] = data[j+1], data[j]
> 
> data = [55, 78, 7, 12, 42]
> bubbleSort(data)
> print(data)
> 
> # > [7, 12, 42, 55, 78]
> ```

#### <u>2) 카운팅 정렬 (Counting Sort)</u>

> - 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
>
> - 제한사항
>
>   - 정수 or 정수로 표현할 수 있는 자료(캐릭터/파이썬에는 없음)에 대해서만 적용 가능 - 각 항목의 발생 회수를 기록하기 위해 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문.
>   - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 함.
>
> - > <u>시간 복잡도 : O( n+k )</u>    #n은 리스트 길이, k는 정수의 최대값
>
> - 과정
>   - 1단계 : Data에서 각 항목들의 발생 회수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 counts에 저장
>   - 2단계 : 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 counts의 원소를 조정
>     - [1, 3, 1, 1, 2] > [1, 4, 5, 6, 8]
>     - 원소가 정렬될 때 리스트의 몇 번째 위치에 들어가야 하는지 보여주기 위함
>   - 3단계 : 데이터의 마지막 항목부터 정렬
>     - data[-1]이 1이므로 counts[1]의 숫자를 1감소시킴(4 > 3), temp[3]에 1삽입
>     - data[-2] == 4, counts[4] -= 1, temp[counts[4]-1] 에 4 삽입
>     - 반복
>
> ```python
> def CountingSort(A, B, C):
>  for i in range(len(A)):
>      C[A[i]] += 1
> 
>  for i in range(1, len(C)):
>      C[i] += C[i-1]
> 
>  for i in range(len(B)-1, -1, -1):
>      B[C[A[i]]-1] = A[i]
>      C[A[i]] -= 1
> 
> A = [1, 4, 5, 1, 2, 4, 5, 7, 9, 3]
> B = [0] * len(A)
> C = [0] * 10
> CountingSort(A, B, C)
> print(B)
> 
> ```





##  C. 문풀 (review - 20190115)

- [1206. view](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWhKdvi6ECkDFAS6&contestProbId=AV134DPqAA8CFAYh&probBoxId=AWhKdvi6ECoDFAS6&type=PROBLEM&problemBoxTitle=1%EC%9B%94+14%EC%9D%BC&problemBoxCnt=1)

```python
# 내 답

import sys
sys.stdin = open("view_input.txt")
T = 10
for tc in range(10):
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))
    #
    peak = []
    for i in range(2, len(data)):
        if data[i-1] < data[i] and data[i] > data[i+1] and data[i-2] < data[i] and data[i+2] < data[i]:
            peak.append(i)
    for p in peak:
        ans += min(data[p]-data[p-2], data[p]-data[p-1], data[p]-data[p+1], data[p]-data[p+2],)

    print("#{} {}".format(tc+1, ans))
```

```python
# 강사님 답 (C 스타일)

import sys
sys.stdin = open("(1206)View_input.txt")
T = 10
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans = 0

    for i in range(2, N-2):
        min = 987654321            #min 함수 안 쓰고 엄청 큰 값 줘서 비교
        for j in range(5):         #j(==2)기준으로 양쪽 2개씩
            if j != 2:
                if data[i]-data[i-2+j] < min:
                    min = data[i] - data[i-2+j]
        if min > 0:
            ans += min

    print("#{} {}".format(tc+1, ans)) 
```







