# Day 05 | 데이터 분석하기 기초



## 데이터 파악하기

데이터를 파악할 때 사용하는 함수들

- `head()` : 데이터 앞부분 출력
- `tail()` : 데이터 뒷부분 출력
- `View()` : 뷰어 창에서 데이터 확인
- `dim()` : 데이터 차원 출력
- `str()` : 데이터 속성 출력
- `summary()` : 요약 통계량 출력



### `head()` : 데이터 앞부분 출력

디폴트로 앞에서부터 여섯 번째 행까지 출력함

괄호 안 데이터 프레임 이름 뒤에 숫자를 입력하면 입력한 행까지의 데이터를 출력함

```r
head(exam)      # 앞에서부터 6행까지 출력
head(exam, 10)  # 앞에서부터 10행까지 출력
```



### `tail()` : 데이터 뒷부분 출력

디폴트로 뒤에서부터 여섯 번째 행까지 출력함

괄호 안 데이터 프레임 이름 뒤에 숫자를 입력하면 입력한 행만큼 데이터를 출력함

```r
tail(exam)      # 뒤에서부터 6행까지 출력
tail(exam, 10)  # 뒤에서부터 10행까지 출력
```



### `View()` : 뷰어 창에서 데이터 확인

엑셀과 유사하게 생긴 '뷰어 창'에 원자료를 직접 보여주는 기능

```r
View(exam)      # 데이터 뷰어 창에서 exam 데이터 확인
```

![https://user-images.githubusercontent.com/45819975/96958913-be012f80-1539-11eb-85ee-1de3c3ec95c3.png](https://user-images.githubusercontent.com/45819975/96958913-be012f80-1539-11eb-85ee-1de3c3ec95c3.png)



### `dim()` : 데이터가 몇 행, 몇 열로 구성되어 있는지 알아보기

dimension의 약자

```r
dim(exam)       # 행, 열 출력
> dim(exam)       # 행, 열 출력
[1] 20  5
```



### `str()` : 속성 파악하기

데이터에 들어있는 변수들의 속성을 보여줌

모든 변수의 속성을 한눈에 파악하고 싶을 때 사용

```r
str(exam)       # 데이터 속성 확인
> str(exam)       # 데이터 속성 확인
'data.frame':	20 obs. of  5 variables:
 $ id     : int  1 2 3 4 5 6 7 8 9 10 ...
 $ class  : int  1 1 1 1 2 2 2 2 3 3 ...
 $ math   : int  50 60 45 30 25 50 80 90 20 50 ...
 $ english: int  98 97 86 98 80 89 90 78 98 98 ...
 $ science: int  50 60 78 58 65 98 45 25 15 45 ...
```

obs : Observation, 관측치 == 행(row)



### `summary()` : 요약 통계량 산출하기

```r
summary(exam)   # 요약 통계량 출력
> summary(exam)   # 요약 통계량 출력
       id            class        math          english        science
   Min.   : 1.00   Min.   :1   Min.   :20.00   Min.   :56.0   Min.   :12.00
   1st Qu.: 5.75   1st Qu.:2   1st Qu.:45.75   1st Qu.:78.0   1st Qu.:45.00
   Median :10.50   Median :3   Median :54.00   Median :86.5   Median :62.50
   Mean   :10.50   Mean   :3   Mean   :57.45   Mean   :84.9   Mean   :59.45
   3rd Qu.:15.25   3rd Qu.:4   3rd Qu.:75.75   3rd Qu.:98.0   3rd Qu.:78.00
   Max.   :20.00   Max.   :5   Max.   :90.00   Max.   :98.0   Max.   :98.00
```

- `Min` : 최솟값(Minimum) - 가장 작은 값
- `1st Qu` : 1사분위수(1st Quantile) - 하위 25%(4분의 1) 지점에 위치하는 값
- `Median` : 중앙값 - 중앙에 위치하는 값
- `Mean` : 평균 - 모든 값을 더해 값의 개수로 나눈 값
- `3rd Qu` : 3사분위수(3rd Quantile) - 하위 75%(4분의 3) 지점에 위치하는 값
- `Max` : 최댓값(Maximum) - 가장 큰 값



## 변수명 바꾸기

`dplyr` 패키지의 `rename()`이용

```r
df_raw <- data.frame(var1 = c(1, 2, 1),
                     var2 = c(2, 3, 2))
df_raw

install.packages("dplyr")  # dplyr 설치
library(dplyr)             # dplyr 로드

df_new <- df_raw  # 복사본 생성
df_new            # 출력

df_new <- rename(df_new, v2 = var2)  # var2를 v2로 수정
df_new

df_new <- rename(df_new, first = var1)
df_new
```



## 파생변수 만들기

변수를 조합하거나 함수를 적용해 새 변수를 만들어 분석할 수도 있음

기존의 변수를 변형해 만든 변수를 `'파생변수(Derived Variable)'`라고 함

```r
df <- data.frame(var1 = c(4, 3, 8),
                 var2 = c(2, 6, 1))
df

df$var_sum <- df$var1 + df$var2       # var_sum 파생변수 생성
df
> df  var1 var2 var_sum
1    4    2       6
2    3    6       9
3    8    1       9
df$var_mean <- (df$var1 + df$var2)/2  # var_mean 파생변수 생성
df
> df  var1 var2 var_sum var_mean
1    4    2       6      3.0
2    3    6       9      4.5
3    8    1       9      4.5
```



### mpg 예제로 통합 연비 변수 만들기

```r
mpg$total <- (mpg$cty + mpg$hwy)/2  # 통합 연비 변수 생성
head(mpg)
> head(mpg)
  manufacturer model displ year cyl      trans drv cty hwy fl   class total
1         audi    a4   1.8 1999   4   auto(l5)   f  18  29  p compact  23.5
2         audi    a4   1.8 1999   4 manual(m5)   f  21  29  p compact  25.0
3         audi    a4   2.0 2008   4 manual(m6)   f  20  31  p compact  25.5
4         audi    a4   2.0 2008   4   auto(av)   f  21  30  p compact  25.5
5         audi    a4   2.8 1999   6   auto(l5)   f  16  26  p compact  21.0
6         audi    a4   2.8 1999   6 manual(m5)   f  18  26  p compact  22.0
mean(mpg$total)  # 통합 연비 변수 평균
> mean(mpg$total)  # 통합 연비 변수 평균
[1] 20.14957
```



## 조건문을 활용해 파생변수 만들기

예제 ) 고연비 자동차 pass / fail

1. 기준값 정하기

   `summary()`를 이용해 통합연비변수 `total`의 평균(mean)과 중앙값(medium)을 확인

   ```r
   summary(mpg$total)  # 요약 통계량 산출
   ```

   ```r
   > summary(mpg$total)  # 요약 통계량 산출
      Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
      10.50   15.50   20.50   20.15   23.50   39.50
   ```

   hist(mpg$total)을 이용해 histogram을 눈으로 확인하고 판단해도 됨

   → 20을 넘기면 pass, 아니면 fail로 하자

2. 합격 판정 변수 만들기

   ```r
   # 20이상이면 pass, 그렇지 않으면 fail 부여
   mpg$test <- ifelse(mpg$total >= 20, "pass", "fail")
   ```

3. 빈도표로 합격 판정 자동차 수 살펴보기 : `table()` 함수 이용

   ```r
   table(mpg$test)   # 연비 합격 빈도표 생성
   ```

   ```r
   > table(mpg$test)   # 연비 합격 빈도표 생성
   fail pass  
   106  128
   ```

4. 막대 그래프로 빈도 표현하기

   ```r
   library(ggplot2)  # ggplot2 로드
   qplot(mpg$test)   # 연비 합격 빈도 막대 그래프 생성
   ```

![https://user-images.githubusercontent.com/45819975/96963418-944d0600-1543-11eb-9b2e-83d1019ffd15.png](https://user-images.githubusercontent.com/45819975/96963418-944d0600-1543-11eb-9b2e-83d1019ffd15.png)



## 중첩 조건문 활용하기

여러 개의 조건문을 중첩한 코드를 '중첩 조건문'이라고 함

예제 ) 연비에 따라 grade 부여

1. 연비에 따라 세 가지 종류의 등급을 부여해 grade 변수를 생성

   ```r
   # total을 기준으로 A, B, C 등급 부여
   mpg$grade <- ifelse(mpg$total >= 30, "A",
                       ifelse(mpg$total >= 20, "B", "C"))
   ```

   이 코드는 아래와 같은 순서로 진행됨

   1. 첫 번째 ifelse()의 조건에 따라 total이 30이상이면 "A"를 부여
   2. 조건에 맞지 않으면 두 번째 ifelse()를 실행, 두 번째 조건에 따라 total이 20이상이면 "B"를 부여
   3. 두 번째 조건도 맞지 않으면 "C"를 부여

2. 빈도표, 막대 그래프로 연비 등급 살펴보기

   ```r
   table(mpg$grade)  # 등급 빈도표 생성
   ```

   ```r
   > table(mpg$grade)  # 등급 빈도표 생성
     A   B   C
    10 118 106
   ```

   ```r
   qplot(mpg$grade)  # 등급 빈도 막대 그래프 생성
   ```

   ![https://user-images.githubusercontent.com/45819975/96964122-dd518a00-1544-11eb-996f-75d41904eeab.png](https://user-images.githubusercontent.com/45819975/96964122-dd518a00-1544-11eb-996f-75d41904eeab.png)



### 원하는 만큼 범주 만들기

`ifelse()`를 더 중첩하면 원하는 만큼 범주의 수를 늘릴 수 있음

```r
# A, B, C, D 등급 부여
mpg$grade2 <- ifelse(mpg$total >= 30, "A",
                     ifelse(mpg$total >= 25, "B",
                            ifelse(mpg$total >= 20, "C", "D")))
```



------



## 정리

```r
# 1.데이터 준비, 패키지 준비
mpg <- as.data.frame(ggplot2::mpg)  # 데이터 불러오기
library(dplyr)                      # dplyr 로드
library(ggplot2)                    # ggplot2 로드

# 2.데이터 파악
head(mpg)     # Raw 데이터 앞부분
tail(mpg)     # Raw 데이터 뒷부분
View(mpg)     # Raw 데이터 뷰어창에서 확인
dim(mpg)      # 차원
str(mpg)      # 속성
summary(mpg)  # 요약 통계량

# 3.변수명 수정
mpg <- rename(mpg, company = manufacturer)

# 4.파생변수 생성
mpg$total <- (mpg$cty + mpg$hwy)/2                   # 변수 조합
mpg$test <- ifelse(mpg$total >= 20, "pass", "fail")  # 조건문 활용

# 5.빈도 확인
table(mpg$test)  # 빈도표 출력
qplot(mpg$test)  # 막대 그래프 생성
```



iris 연습문제

```r
iris
iris$wide <- iris$Sepal.Length * iris$Sepal.Width
summary(iris$Sepal.Length)
hist(iris$Sepal.Length)
iris$level <- ifelse(iris$Sepal.Length >= 6.5, "A",
                     ifelse(iris$Sepal.Length >= 5, "B", "C"))
iris
```