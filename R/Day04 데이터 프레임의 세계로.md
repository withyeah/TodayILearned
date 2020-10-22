# Day 04 | 데이터 프레임의 세계로



## 데이터 프레임

### 데이터 프레임이란?

![https://user-images.githubusercontent.com/45819975/96827274-2d125180-1470-11eb-86c5-7b60ca5fbf15.png](https://user-images.githubusercontent.com/45819975/96827274-2d125180-1470-11eb-86c5-7b60ca5fbf15.png)

- 열 : Column, Variable 속성

- 행 : Row 한 사람의 정보

  10 Row까지 있는 데이터 == 10 Case짜리 데이터

  한 명에 대한 데이터는 가로 한 줄에 나열된다

데이터가 크다 == 행이 많다 || 열이 많다

- 행이 많다 → 컴퓨터가 느려짐 → 고사양 장비 구축
- 열이 많다 → 분석 방법의 한계 → 고급 분석 방법



### 데이터 프레임 만들기

(참고 : memory clear 작업)

```r
# memory clear 작업
list=ls()
rm(list=ls())
```

→ 메모리에 있던 변수들이 다 clear 됨! 메모리 관리~~

```r
english <- c(90, 80, 60, 70)  # 영어 점수 변수 생성
english

math <- c(50, 60, 100, 20)    # 수학 점수 변수 생성
math

# english, math로 데이터 프레임 생성해서 df_midterm에 할당
df_midterm <- data.frame(english, math)
df_midterm

class <- c(1, 1, 2, 2)
class

df_midterm <- data.frame(english, math, class)
df_midterm

# 달러 기호($)는 데이터 프레임 안에 있는 변수를 지정할 때 사용
mean(df_midterm$english)  # df_midterm의 english로 평균 산출
mean(df_midterm$math)     # df_midterm의 math로 평균 산술

df_midterm <- data.frame(english = c(90, 80, 60, 70),
                         math = c(50, 60, 100, 20),
                         class = c(1, 1, 2, 2))
df_midterm
> df_midterm
  english math class
1      90   50     1
2      80   60     1
3      60  100     2
4      70   20     2
```



## 외부 데이터 이용하기

```r
install.packages("readxl")
library(readxl)

# 엑셀 파일을 불러와서 df_exam에 할당
df_exam <- read_excel("Data/excel_exam.xlsx")  
# 출력
df_exam                                   

mean(df_exam$english)
mean(df_exam$science)
> df_exam                               
# A tibble: 20 x 5
      id class  math english science
   <dbl> <dbl> <dbl>   <dbl>   <dbl>
 1     1     1    50      98      50
 2     2     1    60      97      60
 3     3     1    45      86      78
 4     4     1    30      98      58
 5     5     2    25      80      65
 6     6     2    50      89      98
 7     7     2    80      90      45
 8     8     2    90      78      25
 9     9     3    20      98      15
10    10     3    50      98      45
11    11     3    65      65      65
12    12     3    45      85      32
13    13     4    46      98      65
14    14     4    48      87      12
15    15     4    75      56      78
16    16     4    58      98      65
17    17     5    65      68      98
18    18     5    80      78      90
19    19     5    89      68      87
20    20     5    78      83      58
> mean(df_exam$english)
[1] 84.9
> mean(df_exam$science)
[1] 59.45
```



### 엑셀 파일 첫 번째 행이 변수명이 아니라면?

→ 첫 번째 행의 데이터가 변수명으로 지정되면서 유실되는 문제가 발생

```r
df_exam_novar <- read_excel("Data/excel_exam_novar.xlsx")
df_exam_novar
> df_exam_novar
# A tibble: 7 x 5
  `1...1` `1...2` `50...3`  `98` `50...5`
    <dbl>   <dbl>    <dbl> <dbl>    <dbl>
1       2       1       60    97       60
2       3       2       25    80       65
3       4       2       50    89       98
4       5       3       20    98       15
5       6       3       50    98       45
6       7       4       46    98       65
7       8       4       48    87       12
```

→ `col_names = F` 파라미터를 설정

→ 첫 번째 행을 변수명이 아닌 데이터로 인식해 불러오고 변수명은 '...숫자'로 자동 지정됨

```r
df_exam_novar <- read_excel("Data/excel_exam_novar.xlsx", col_names = F)
df_exam_novar
> df_exam_novar
# A tibble: 8 x 5
   ...1  ...2  ...3  ...4  ...5
  <dbl> <dbl> <dbl> <dbl> <dbl>
1     1     1    50    98    50
2     2     1    60    97    60
3     3     2    25    80    65
4     4     2    50    89    98
5     5     3    20    98    15
6     6     3    50    98    45
7     7     4    46    98    65
8     8     4    48    87    12
```



### 엑셀 파일에 시트가 여러 개 있다면?

`sheet = 숫자` 파라미터를 이용해서 몇 번째 시트의 데이터를 불러올지 지정할 수 있음

```r
# 엑셀 파일의 세 번째 시트에 있는 데이터 불러오기
df_exam_sheet <- read_excel("Data/excel_exam_sheet.xlsx", sheet = 3)
```



### CSV 데이터 불러오기

`read.csv()` 를 이용하면 별도의 패키지를 설치하지 않고 csv를 불러올 수 있음

첫 번째 행에 변수명이 없는 CSV 파일을 불러올 때는 `header = F` 파라미터를 붙여주면 됨

문자가 들어있는 파일을 불러올 때는 `stringsAsFactors = F`

```r
df_csv_exam <- read.csv("Data/csv_exam.csv", stringsAsFactors = F)
```



### CSV 파일로 저장하기

```r
df_midterm <- data.frame(english = c(90, 80, 60, 70),
                         math = c(50, 60, 100, 20),
                         class = c(1, 1, 2, 2))
df_midterm

write.csv(df_midterm, file = "Data/df_midterm.csv")
```

R 내장함수인 `write.csv()`를 이용



## RDS 파일 활용하기

- RDS : R 전용 데이터 파일
- 다른 파일들에 비해 R에서 읽고 쓰는 속도가 빠르고 용량이 작다
- 일반적으로 R에서 분석작업을 할 때는 RDS 파일을 이용하고 R을 이용하지 않는 사람과 파일을 주고 받을 때는 CSV파일을 이용



### 데이터 프레임을 RDS 파일로 저장하기

```
saveRDS()
save(df_midterm, file = "Data/df_midterm.rda")
```



### RDS 파일 불러오기

```
readRDS()
load("Data/df_midterm.rda")
```