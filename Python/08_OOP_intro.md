# 08_OOP_intro

> OOP : 컴퓨터 프로그래밍 패러다임의 하나. 컴퓨터 프로그램을 독립된 단위인 '객체'들의 모임으로 파악. 각각의 객체는 메시지를 주고받거나 데이터를 처리할 수 있음. 절차지향 프로그래밍에서 발전된 형태.
>
> 기본 구성요소 
>
> - `클래스` : 같은 종류의 집단에 속하는 속성과 행위를 정의한 것, user define data type
> - `인스턴스` : 메모리상에 할당된 클래스의 인스턴스, 클래스에서 정의한 행위 + 자신 고유의 속성, 객체의 행위는 클래스의 행위에 대한 정의를 공유하여 메모리를 경제적으로 사용
> - `메서드` : 클래스로부터 생성된 객체를 사용하는 방법, 객체에 명령을 내리는 것, 객체의 속성을 조작하는 데 사용됨



## A. 클래스

```python
class ClassName:
```

- 선언과 동시에 클래스 객체 생성
- 선언된 공강은 지역 스코프로 사용됨
- 정의된 속성 중 변수 : 멤버 변수
- 정의된 함수(def) : 메서드

```python
class Person:
    name = '고길동'
    def sayhello(self):  #self 꼭 써줘야 함
        print(f"Hello, I'm {self.name}.")
```



## B. 인스턴스

- 인스턴스 객체는 ClassName()을 호출함으로써 선언
- 인스턴스 객체와 클래스 객체는 서로 다른 이름공간을 가짐
- 인스턴스 > 클래스 > 전역 순으로 탐색

```python
# 클래스 Person의 iu라는 인스턴스 선언
iu = Person()
```

```python
# sayhello 메서드 호출
iu.sayhello()  # Hello, I'm 고길동
```

```python
# iu의 이름을 확인 
# 변수에 접근할 때는 () 없이!!!
iu.name  #'고길동'
```

```python
# iu로 이름을 바꿈
iu.name = 'iu'

iu.sayhello() # Hello, I'm iu.

#iu와 Person이 같은지 확인
isinstance(iu, Person)  # True
```

```python
iu = Person()
iu.sayhello()

#풀어서쓰면
Person.sayhello(iu)
인스턴스 자기 자신을 호출한다는 의미로 self
```



## C. 실습

```python
class Person:
    name = 'kim'
    phone = '01099685932'
    pocket = {'won': 500, 'phone': 1, 'candy': 3}
    
    def in_my_pocket(self, stuff, count):
        if self.pocket.get(stuff):
            self.pocket[stuff] += count
        else:
            self.pocket[stuff] = count
        return self.pocket
     
    def greeting(self):
        return f'안녕, 나는 {self.name}이야. 내 번호는 {self.phone}야.'
    
    def get_my_pocket(self):
        return self.pocket
```

