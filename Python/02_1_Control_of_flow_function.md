# 02_1_Control of flow_function



#### 1.1 내장함수 목록

```python
dir(__builtins__)
```



#### 2.1 기본 매개변수 이후에 기본 값이 없는 매개변수 사용 불가

```python
def greeting(name='ssafy', age):
    print(f'{name}은 {age}살 입니다.')   
# > SyntaxError: non-default argument follows default argument

def greeting(age, name='ssafy'):
    print(f'{name}은 {age}살 입니다.')
# > 이 경우는 가능
```

#### 2.2 키워드 인자를 활용한 뒤에 위치 인자를 활용 불가

```python
greeting(age=24, "철수")
# > SyntaxError: positional argument follows keyword argument
```



#### 3.1 정수를 여러 개 받아서 가장 큰 값을 반환(return)하는 `my_max()`

```python
def my_max(*args):
    max_num = args[0]
    for i in range(1, len(args)):
        if max_num < args[i]:
            max_num = args[i]
    print(max_num)
```



#### 4.1 dictionary 반환 함수 `my_dict()`

```python
def my_dict(**kwargs):
    for kw in kwargs:
        kwargs[kw] = kwargs[kw]
    return kwargs
my_dict(한국어="안녕",영어="hi")
#{'한국어': '안녕', '영어': 'hi'}
```



#### 5.1 dictionary를 인자로 넘기기(unpacking arguments list)

```python
def user(username, password, password_confirmation):
    if password == password_confirmation:
        print(f'{username}님 회원가입이 완료되었습니다.')
    else:
        print('비밀번호와 비밀번호 확인이 일치하지 않습니다.')
```

```python
user(my_account)
# 인자 1개로 인식함

user(**my_account)
# dictionary **언패킹해서 넘겨주면 인자 3개로 인식해서 작동!
```



#### 6.1 네임스페이스 원칙 (LEGB)

- def 내에 할당된 이름들은 오직 그 def 코드에 의해서만 보임. 함수 외부에서는 그 이름을 확인조차 할 수 없다.

- def 내에 할당된 이름들은 비록 동일한 이름이 다른 곳에서 사용되더라도 def 바깥의 변수들과 충돌하지 않는다. 즉 def 문 안에 할당된 이름 x는 def 밖에서 할당된 x와는 전혀 다르다.

```python
global_num = 3
def localscope2():
    global_num = 5
    print(f'global_num이 {global_num}로 설정되었습니다.')

localscope2() #global_num이 5로 설정되었습니다.
print(global_num) #3
```

