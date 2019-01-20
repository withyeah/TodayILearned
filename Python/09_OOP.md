# 09_OOP

> 용어 정리
>
> ```python
> class Person:  #=> 클래스 정의(선언) : 클래스 객체 생성 클래스 첫 글자는 대문자
>     name = '홍길동'   #=> 멤버 변수(데이터 어트리뷰트)
>     def greeting(self):  #=> 멤버 메서드(메서드)
>         print(f'{self.name}')
>         
> iu = Person()       # 인스턴스 객체 생성
> daniel = Person()   # 인스턴스 객체 생성
> iu.name             # 데이터 어트리뷰트 호출
> iu.greeting()       # 메서드 호출
> ```



## A. self : 인스턴스 객체 자기자신

- 대부분 메서드에서 self를 첫 번째 인자로 설정
- 메서드는 인스턴스 객체가 함수의 첫 번째 인자로 전달되도록 되어있음

- 클래스 선언부 내부에서도 반드시 self를 통해 데이터 어트리뷰트에 접근해야함

  - ```python
    name = '?'
    class Person:
        name = '홍길동'
        def greeting(self):
            print(f'{name}')   
    # self.name이 아니라서 전역변수인 name = '?'을 가져옴
    ```



## B. 클래스-인스턴스간의 이름공간

- 클래스 정의 > 클래스 객체 생성, 해당되는 이름공간 생성
- 인스턴스 생성 > 인스턴스 객체 생성, 해당되는 이름공간 생성
- 인스턴스의 어트리뷰트가 변경되면, 변경된 데이터를 인스턴스 객체 이름공간에 저장
- 인스턴스에서 특정한 어트리뷰트에 접근하게 되면 인스턴스 > 클래스 순으로 탐색함



## C. 생성자 / 소멸자

- `생성자` : 인스턴스 객체가 생성될 때 호출되는 함수
- `소멸자` : 객체가 소멸되는 과정에서 호출되는 함수
- 스페셜 메서드 / 매직 메서드 : 양 쪽에 언더스코어가 있는 메서드

```python
def __init__(self):
    print('생성될 때 자동으로 호출되는 메서드입니다.')

def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
```

- 생성자도 메서드기 때문에 추가적인 인자를 받을 수 있음

  - ```python
    class Person:
        def __init__(self, name):
            print(f'응애, {name}')
        def __del__(self):
            print('빠이')
            
    # 홍길동이라는 이름을 가진 hong 을 만들어봅시다.
    hong = Person('홍길동')
    ```

- 생성자는 값을 초기화하는 과정에서 자주 활용됨



## D. 클래스 변수 / 인스턴스 변수

```python
class Person:
    population = 0              
    # 클래스 변수 : 모든 인스턴스가 공유함.

    def __init__(self, name):   
        self.name = name        
        # 인스턴스 변수 : 인스턴스별로 각각 가지는 변수
```

```python
class Person:
    population = 0
    
    def __init__(self, name):
        self.name = name
        Person.population += 1

# 본인의 이름을 가진 인스턴스를 만들어봅시다.
me = Person('예랑')

# 이름을 출력해봅시다.
me.name  # '예랑'

# population을 출력해봅시다.
Person.population # 1
```



## E. 정적 메서드 / 클래스 메서드

- 클래스가 메서드 호출을 할 수 있도록 구성 가능

- 정적 메서드 : 객체가 전달되지 않은 형태,

  - ```python
    @staticmethod
    def methodname():
        codeblock
    ```

  - Class.methodname() : 클래스.메서드() 호출 가능!

- 클래스 메서드 : 인자로 클래스를 넘겨줌

  - ```python
    @classmethod
    def methodname(cls):        
        #정적 메소드와 차이점 : 클래스메소드는 인자를 받는다 (cls)
        codeblock
    ```



## F. 실습 - 스택

**Stack** 클래스 구현

1. `empty()`: 스택이 비었다면 참을 주고,그렇지 않다면 거짓이 된다.
2. `top()`: 스택의 가장 마지막 데이터를 넘겨준다. 스택이 비었다면 None을 리턴해주세요.
3. `pop()`: 스택의 가장 마지막 데이터의 값을 넘겨주고 해당 데이터를 삭제한다. 스택이 비었다면 None을 리턴해주세요.
4. `push()`: 스택의 가장 마지막 데이터 뒤에 값을 추가한다. 리턴값 없음

```python
class Stack:
    def __init__(self):   
# init 무조건 줘야 함! 인스턴스끼리 각각 다른 리스트를 가져야 하기 때문에
        self.items = []
    def empty(self):
        return not self.items
    def top(self):
        if self.items:
            return self.items[-1]
    def pop(self):
        if self.items:
            return self.items.pop()
    def push(self, datum):
        self.items.append(datum)
```



## G. 연산자 오버라이딩(중복 정의)

- 파이썬에 기본적으로 정의된 연산자를 직접 정의하여 활용할 수 있음

```python
+  __add__   
-  __sub__
*  __mul__
<  __lt__
<= __le__
== __eq__
!= __ne__
>= __ge__
>  __gt__
```

```python
# 사람과 사람을 더하면, 나이의 합을 반환하도록 만들어봅시다.
class Person:
    population = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
        
    def __add__(self, other):  #other : 다른 인스턴스
        return f'나이 합은 {self.age + other.age}'
    
    def __sub__(self, other):
        return f'나이 차는 {self.age - other.age}'
```

```python
# 연산자를 호출해봅시다.
p1 = Person('아저씨', 40)
p2 = Person('청소년', 16)
# 원하는 연산자로 사람과 사람을 비교해보세요.
p1 + p2 #'나이 합은 56'
```



## H. 상속

- 부모 클래스의 모든 속성이 자식 클래스에게 상속되므로 코드 재사용성이 높아짐

- ```python
  class DerivedClassName(BaseClassName):
      code block
  ```

```python
# 인사만 할 수 있는 간단한 사람 클래스를 만들어봅시다.
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print(f'안녕하세요! {self.name}입니다.')
```

```python
# 사람 클래스를 상속받아 학생 클래스를 만들어봅시다.
class Student(Person):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
```

```python
# 학생을 만들어봅시다.
s1 = Student('예랑', '20190116')
```

```python
# 부모 클래스에 정의를 했음에도 메소드를 호출 할 수 있습니다.
s1.greeting() # 안녕하세요! 예랑입니다.
```

- 상속관계 확인 : issubclass(자식, 부모)

- ```python
  issubclass(Person, Student) #False
  issubclass(Student, Person) #True
  ```