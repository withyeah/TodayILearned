# Day 06 | 자유자재로 데이터 가공하기



## 데이터 전처리

데이터 전처리 : 분석에 적합하게 데이터를 가공하는 작업

예 ) 일부를 추출하기, 종류별로 나누기, 여러 데이터를 합치기 등



### dplyr 패키지로 데이터 가공하기

- `filter()` : 행 추출
- `select()` : 열(변수) 추출
- `arrange()` : 정렬
- `mutate()` : 변수 추가
- `summarise()` : 통계치 산출
- `group_by()` : 집단별로 나누기
- `left_join()` : 데이터 합치기 (열)
- `bind_rows()` : 데이터 합치기 (행)



## filter() : 조건에 맞는 데이터만 추출하기

1. `dplyr` 패키지를 로드한 후 예제 파일을 데이터 프레임으로 만들어 출력

   ```r
   library(dplyr)
   exam <- read.csv("Data/csv_exam.csv")
   exam
   ```

2. `dplyr` 패키지의 `filter()`를 이용해 데이터를 추출

   `%>%` : 파이프 연산자(pipe operator), 함수들을 연결해 주는 파이프라인

   `cmd + shift + m` 하면 삽입됨

   ```r
   # exam에서 class가 1인 경우만 추출하여 출력
   exam %>% filter(class == 1)  
   
   # 2반인 경우만 추출
   exam %>% filter(class == 2)  
   
   # 1반이 아닌 경우
   exam %>% filter(class != 1)
   
   # 3반이 아닌 경우
   exam %>% filter(class != 3)
   ```



### 초과, 미만, 이상, 이하 조건 걸기

```r
# 수학 점수가 50점을 초과한 경우
exam %>% filter(math > 50)

# 수학 점수가 50점 미만인 경우
exam %>% filter(math < 50)

# 영어 점수가 80점 이상인 경우
exam %>% filter(english >= 80)

# 영어 점수가 80점 이하인 경우
exam %>% filter(english <= 80)
```



### 여러 조건을 충족하는 행 추출하기

```r
# 1반이면서 수학 점수가 50점 이상인 경우
exam %>% filter(class == 1 & math >= 50)

# 2반이면서 영어 점수가 80점 이상인 경우
exam %>% filter(class == 2 & english >= 80)
```



### 여러 조건 중 하나 이상 충족하는 행 추출하기

```r
# 수학 점수가 90점 이상이거나 영어 점수가 90점 이상인 경우
exam %>% filter(math >= 90 | english >= 90)

# 영어 점수가 90점 미만이거나 과학점수가 50점 미만인 경우
exam %>% filter(english < 90 | science < 50)
```



### 목록에 해당하는 행 추출하기

`%in%` 기호 : '매치 연산자(Matching Operator)'

```r
# 1, 3, 5 반에 해당되면 추출
exam %>% filter(class == 1 | class == 3 | class == 5)

exam %>% filter(class %in% c(1,3,5))
```



## 추출한 행으로 데이터 만들기

```r
class1 <- exam %>% filter(class == 1)  # class가 1인 행 추출, class1에 할당
class2 <- exam %>% filter(class == 2)  # class가 2인 행 추출, class2에 할당

mean(class1$math)                      # 1반 수학 점수 평균 구하기
mean(class2$math)                      # 2반 수학 점수 평균 구하기
```



## select() : 필요한 변수만 추출하기

일부 변수만 추출해 활용하고자 할 때 활용

```r
exam %>% select(math)                  # math 추출
exam %>% select(english)               # english 추출
exam %>% select(class, math, english)  # class, math, english 변수 추출
exam %>% select(-math)                 # math 제외
exam %>% select(-math, -english)       # math, english 제외
```



## dplyr 함수 조합하기

dplyr 패키지의 함수들은 %>%를 이용해 조합할 수 있다는 장점이 있음

1. filter()와 select() 조합하기

   ```r
   # class가 1인 행만 추출한 다음 english 추출
   exam %>% filter(class == 1) %>% select(english)
   ```

2. 가독성있게 줄 바꾸기

   ```r
   exam %>%
     filter(class == 1) %>%  # class가 1인 행 추출
     select(english)         # english 추출
   ```

3. 일부만 출력하기

   ```r
   exam %>% 
     select(id, math) %>%    # id, math 추출
     head                    # 앞부분 6행까지 추출
   
   exam %>% 
     select(id, math) %>%  # id, math 추출
     head(10)              # 앞부분 10행까지 추출
   ```



## arrange() : 순서대로 정렬하기

default : 오름차순

내림차순 정렬하려면 기준 변수를 desc()에 적용하면 됨

```r
exam %>% arrange(math)         # math 오름차순 정렬
exam %>% arrange(desc(math))   # math 내림차순 정렬
exam %>% arrange(class, math)  # class 및 math 오름차순 정렬
```