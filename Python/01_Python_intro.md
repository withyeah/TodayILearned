# 01_Python_intro



- 식별자 (if, elif, else, True, False...)

  ```python
  import keyword
  print (keyword.kwlist)
  ```



- 변수는 `=`를 통해 `할당(assignment)` 된다.



- 실수 처리

  ```python
  1. 3.5 - 3.12
  	#0.37999999999
  2. round(3.5 - 3.12, 2)
  	#0.38
  3. 0.1 * 3 == 0.3
  	#False
  	a. abs(0.1 * 3 - 0.3) <= 1e-10
      b. abs(0.1 * 3 - 0.3) <= sys.float_info.epsilon
      c. import math
  		math.isclose(0.1 * 3, 0.3)
  ```



- 문자열 안에 문장부호(`'`, `"`)가 활용될 경우 앞에 이스케이프 문자(`\`)를 붙여서 사용



- String interpolation

  ```python
  1. 'hello, %s' % name
  2. 'hello. {}'.format(name)
  3. f'hello, {name}'
  	# f-string에서는 형식을 지정할 수 있으며 연산도 가능
  ```



- 내장함수 divmod() - div modify: 몫과 나머지를 출력



- 논리연산자

  - and 는 a 가 거짓이면 a 를 리턴하고, 참이면 b 를 리턴한다.

  - or 은 a 가 참이면 a 를 리턴하고, 거짓이면 b 를 리턴한다.

    ```python
    print(3 and 5)
    #3에서 True -> 뒤로 넘어감 5출력
    print(0 and 3)
    #0에서 False 끝
    print(3 and 0)
    #3에서 True -> 뒤로 넘어감 0 False 0출력
    print(0 and 0)
    
    print(3 or 5)
    print(0 or 3)
    print(3 or 0)
    print(0 or 0)
    ```



- Identity  :  `is`

  ```python
  a = 1000006
  b = 1000006
  a is b
  #참조비교 - 메모리 참조 다름
  # -> False
  print(id(a))
  print(id(b)) #다름
  ```

  ```python
  a = 3
  b = 3
  a is b
  #파이썬에서는 -5부터 256까지는 캐싱되어 있음 - 같은 값
  # -> True
  #참고 : 스트링도 짧은 건 값비교, 긴 건 참조비교
  print(id(a))
  print(id(b))  #같음
  ```

  ```python
  #예외)같은 함수 내에서는 같은 메모리 주소를 쓴다
  def animal():
      cat = 1000006
      print(cat is 1000006)
  animal()
  #True
  ```



- 형변환 ( Type conversion / Typecasting )

  - <u>암시적 형변환 (Implicit Type Conversion)</u>

    `bool` 과 `Numbers` (int < float < complex) 만 가능

    bool : True == 1, False ==0

  - <u>명시적 형변환 (Explicit Type Conversion)</u>

    - str > int : 형식에 맞는 숫자만 가능  #str '3.5'를 int로 변환불가능, float 3.5는 int 변경 가능
    - int > str : 모두 가능
    - 암시적 형변환이 되는 모든 경우도 명시적으로 형변환 가능 ex. int(), float(), str() 등



- 자료형
  - 시퀀스 : 리스트, 튜플, 레인지, 문자열, 바이너리
  - 시퀀스 X : 세트, 딕셔너리