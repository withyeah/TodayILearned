# Day 02 | 데이터 분석을 위한 연장 챙기기

## 변수

변수는 '변하는 수'다

- 변수는 데이터 분석의 대상
- 상수는 분석할 게 없다 : 고정된 값

### 할당 연산자

`a <- 1` : a에 1을 할당함

참고) `ctrl(cmd) + enter(return)` : 실행

참고2) `a = 1` 처럼 등호(=)를 사용해도 됨, 하지만 R에서는 등호가 할당 외에 다른 기능도 하기 때문에 변수를 만들 때에는 화살표 기호를 사용

- 변수를 만들고 나면 (할당 후 실행) 변수를 이용해 연산을 할 수 있음
- 변수끼리 연산할 수도 있고 변수와 숫자를 조합해 연산할 수도 있음

```r
a <- 1  # a에 1 할당
a       # a 출력
```



### 변수명 생성 규칙

- 알아보기 쉽고 기억하기 쉽도록 의미를 담아 이름을 정함
- 문자, 숫자, 대시(-), 언더바(_)를 조합해 정할 수 있음
- 단, 문자로 시작해야 함
- 모두 소문자로 만드는 습관을 들이는 게 좋다(대문자를 혼합하면 디버깅이 어려움)



### 여러 값으로 구성된 변수 만들기

- ```
  c()
  ```

   : combine 함수

  - `c(시작숫자 : 마지막 숫자)` : 1씩 증가하면서 연속된 숫자변수를 만듬

- ```
  seq()
  ```

   : sequence 함수

  - `seq(시작숫자, 마지막 숫자)` : 연속 값을 지닌 변수를 만듬
  - `seq(시작숫자, 마지막 숫자, by = 간격)` : by 파라미터를 이용하면 일정한 간격을 두고 연속된 숫자로 된 변수를 만듬

```r
var1 <- c(1, 2, 5, 7, 8)    # 숫자 다섯 개로 구성된 var1 생성
var1                        # 1 2 5 7 8

var2 <- c(1:5)              # 1~5까지 연속값으로 var2 생성
var2                        # 1 2 3 4 5

var3 <- seq(1, 5)           # 1~5까지 연속값으로 var3 생성
var3                        # 1 2 3 4 5

var4 <- seq(1, 10, by = 2)  # 1~10까지 2 간격 연속값으로 var4 생성
var4                        # 1 3 5 7 9

var5 <- seq(1, 10, by = 3)  # 1~10까지 3 간격 연속값으로 var5 생성
var5                        # 1  4  7 10

var1
var1+2                      # 3  4  7  9 10

var1
var2
var1+var2                   # 2  4  8 11 13
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1c4cf374-20cf-4e79-bdb6-1574048e8adc/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1c4cf374-20cf-4e79-bdb6-1574048e8adc/Untitled.png)

띄어쓰기? num vs int??



### 문자로 된 변수 만들기

변수에 문자를 넣을 때는 문자 앞뒤에 따옴표("")를 붙여야 함

```r
str1 <- "a"
str1

str2 <- "text"
str2

str3 <- "Hello World!"
str3

str4 <- c("a", "b", "c")
str4

str5 <- c("Hello!", "World", "is", "good!")
str5
# "Hello!" "World"  "is"     "good!"
```

- 참고 : 단어들 중 가장 긴 단어의 길이를 기준으로 출력 구간을 정하기 때문에 "is"와 "good!"사이의 간격이 벌어진 형태로 출력됨

```r
str1+2  
# Error in str1 + 2 : non-numeric argument to binary operator
```

- 문자로 된 변수로는 연산할 수 없다



## 함수

데이터 분석은 함수로 시작해 함수로 끝난다

### 숫자를 다루는 함수 이용하기

- `mean()` : 평균

- `max()` : 최대

- `min()` : 최소

  ```r
  # 변수 만들기
  x <- c(1, 2, 3)
  x
  
  # 함수 적용하기
  mean(x)
  max(x)
  min(x)
  ```



### 문자를 다루는 함수 이용하기

- `paste()` : 여러 문자를 합쳐 하나로 만드는 함수

  ```r
  paste(str5, collapse = ",")  # 쉼표를 구분자로 str4의 단어들 하나로 합치기
  # "Hello!,World,is,good!"
  paste(str5, collapse = " ") 
  # "Hello! World is good!" 
  ```



### 함수의 결과물로 새 변수 만들기

함수의 결과물을 새 변수에 집어넣을 수도 있음

```r
str5_paste <- paste(str5, collapse = " ")
str5_paste                   
# "Hello! World is good!"
```



## 패키지 : 함수 꾸러미

패키지 설치하기 → 패키지 로드하기 → 함수 사용하기

```r
install.packages("ggplot2")  # ggplot2 패키지 설치
library(ggplot2)             # ggplot2 패키지 로드

# 여러 문자로 구성된 변수 생성
x <- c("a", "a", "b", "c")
x

# 빈도 그래프 출력
qplot(x)
```

- `qplot()` : 막대그래프 출력

  ![https://user-images.githubusercontent.com/45819975/96548812-7b491880-12e9-11eb-8a79-5ef222564cb7.png](https://user-images.githubusercontent.com/45819975/96548812-7b491880-12e9-11eb-8a79-5ef222564cb7.png)

- mpg 예시 데이터

  ```r
  # data에 mpg, x축에 hwy 변수 지정하여 그래프 생성
  qplot(data = mpg, x = hwy)
  
  # x축 cty
  qplot(data = mpg, x = cty)
  
  # x축 drv, y축 hwy
  qplot(data = mpg, x = drv, y = hwy)
  
  # x축 drv, y축 hwy, 선 그래프 형태
  qplot(data = mpg, x = drv, y = hwy, geom = "line")
  
  # x축 drv, y축 hwy, 상자 그림 형태
  qplot(data = mpg, x = drv, y = hwy, geom = "boxplot")
  
  # x축 drv, y축 hwy, 상자 그림 형태, drv별 색 표현
  qplot(data = mpg, x = drv, y = hwy, geom = "boxplot", colour = drv)
  
  # qplot 함수 매뉴얼 출력
  ?qplot
  
  mpg
  ```