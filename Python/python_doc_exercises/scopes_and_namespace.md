# Scopes and Namespace

20190209 python doc p.71 

scopes and namespaces example 

**nonlocal, global**의 기능

```python
def scope_test():
    def do_local():
        spam = "local spam"
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

> ```
> After local assignment: test spam
> After nonlocal assignment: nonlocal spam
> After global assignment: nonlocal spam
> In global scope: global spam
> ```



1. do_local() 했는데 왜 test spam?

   - do_local() 은 로컬에 spam이 없기 때문에 새로 변수를 생성하며 local spam을 할당
   - 그래서 scope_test()에 있는 spam에는 영향을 미치지 않음

2. `nonlocal` : 가장 가까운 상위 함수의 변수로 만들어줌

   - 상위함수에 spam이 없으면 오류 뿜뿜

3. `global` : global에 spam이 없어도 생성하며 할당

4. do_global() 했는데 왜 nonlocal spam?

   - do_global()은 global의 spam에 할당한 것이고 do_nonlocal()에 의해 현재 spam은 nonlocal spam

5. 마지막에 global에서 spam을 불러올 때는 do_global()의 결과인 global spam을 찾음

   