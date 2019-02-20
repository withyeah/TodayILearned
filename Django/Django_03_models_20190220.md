# Django_models

20190220



## CRUD

### Create

기본설정 후

>  앱 > models.py 에서 class 줌

```python
# 각 모델은 django.db.models.Model 클래스의 서브 클래스로 표현  
class Board(models.Model):
    
    # max_length 는 charfield의 필수 인자 (유효성 검사에 사용됨)
    title = models.CharField(max_length=10)
    # 제한 없으면 TextField()
    content = models.TextField()
    # 필수 인자는 없음, 
    # auto_now_add 켜두면 글이 생성된 시간이 박힘(기본적으로는 UTC)
    # auto_now_add=True : 장고 모델이 최초 저장시에만 현재 날짜를 적용
    # settings.py 에서 USE_TZ = False 꺼주면 국제화가 모든 곳에 적용됨
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now=True : 장고 모델이 save 될 때마다 현재 날짜로 갱신
    updated_at = models.DateTimeField(auto_now=True)
```



```
# '0001'은 버전, 알아서 계속 버전을 쌓아간다
$ python manage.py makemigrations boards
Migrations for 'boards':
  boards/migrations/0001_initial.py
    - Create model Board
```

```
# DB에 아직 들어가지 않은 설계도 /  확인하기
$ python manage.py sqlmigrate boards 0001 
BEGIN;
--
-- Create model Board
--
CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL);
COMMIT;
```



테이블 만들기

```
$ python manage.py migrate
```

db확인

```
$ sqlite3 db.sqlite3
```

table 뭐있는지 확인

```
sqlite> .tables
auth_group                  boards_board              
auth_group_permissions      django_admin_log          
auth_permission             django_content_type       
auth_user                   django_migrations         
auth_user_groups            django_session            
auth_user_user_permissions
```

boards_board의 스키마 확인

```
sqlite> .schema boards_board
CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
```

sqlite exit

```
sqlite> .exit
```



```
$ python manage.py shell
```

```
>>> from boards.models import Board
# SELECT * FROM board 와 같음
>>> Board.objects.all()
<QuerySet []>
```

> 현재 비어있음



```
>>> board = Board()
>>> board.title = 'first'
>>> board.content = 'django!'
>>> board.save()
>>> Board.objects.all()
<QuerySet [<Board: Board object (1)>]>
```

> 한 줄 생김!



```python
# models.py 에서 추가
def __str__(self):
        return f'{self.id}: {self.title}'
```

```
$ python manage.py shell

>>> from boards.models import Board
>>> Board.objects.all()
<QuerySet [<Board: 1: first>]>
```



매번 from import 치기 귀찮으니까 [장고 익스텐션](https://django-extensions.readthedocs.io/en/latest/)을 설치하자

```
$ pip install django-extensions
```

```python
# settings.py 의 INSTALLED_APPS 리스트에 추가
'django_extensions',
```

```
$ python manage.py shell_plus
```

> shell의 기능이 업그레이드b (익스텐션) > 모든 것들이 import됨

```
>>> board = Board(title='second', content='django!!')
>>> board.save()
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: second>]>
```

> 두 개의 객체를 확인할 수 있다



더 짧게!!!

```
>>> Board.objects.create(title='third', content='django!!!')
<Board: 3: third>
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>]>
```

> create 에는 save 속성이 있음



저장의 필요성

```
>>> board = Board()
>>> board.title = 'fourth'
>>> board.content = 'django!!!!'
>>> board.id            #NONE
>>> board.created_at    #NONE
>>> board.save()
>>> board.id
4
>>> board.created_at
datetime.datetime(2019, 2, 20, 10, 35, 24, 583582)
```



모델 검증 (validation, 예외처리)

```
>>> board = Board()
>>> board.title = 'awegawefjawoeigawoieaeg'
>>> board.full_clean()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/ubuntu/.pyenv/versions/django-venv/lib/python3.6/site-packages/django/db/models/base.py", line 1152, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'title': ['이 값이 최대 10 개의 글자인지 확인하세요(입력값 23 자).'], 'content': ['이 필드는 빈 칸으로 둘 수 없습니다
```



### Read



```
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>, <Board: 4: fourth>]>
>>> Board.objects.filter(title='first').all()
<QuerySet [<Board: 1: first>]>
```

> first인 전체를 read하기 때문에 일단 리스트로 생성

```
>>> Board.objects.filter(title='first').first()
<Board: 1: first>
```

> 하나만 read 할 것이기 때문에 리스트 X



없는 title 찾을 때 > None 리턴

```
>>> Board.objects.filter(title='missing').first()
```



```
>>> board = Board.objects.get(pk=1)
>>> board
<Board: 1: first>
>>> board = Board.objects.filter(id=1)
>>> board
<QuerySet [<Board: 1: first>]>
```

> ID는 항상 .get으로 가져와야 한다!!!!!



LIKE

```
>>> boards = Board.objects.filter(title__contains='fi').all()
>>> boards
<QuerySet [<Board: 1: first>]>
>>> boards = Board.objects.filter(title__startswith='fi')
>>> boards
<QuerySet [<Board: 1: first>]>
>>> boards = Board.objects.filter(title__endswith='!')
>>> boards
<QuerySet []>
```



정렬

```
>>> boards = Board.objects.order_by('-title').all()
>>> boards
<QuerySet [<Board: 3: third>, <Board: 2: second>, <Board: 4: fourth>, <Board: 1: first>]>
```

> order_by 기본적으로 오름차순
>
> '-title' > title 내림차순으로 정렬





### Update



```
>>> board = Board.objects.get(pk=1)
>>> board.title = 'hello'
>>> board.save()
>>> board.title
'hello'
```





### Delete



현재 board에 1번글 담겨있음

```
>>> board.delete()
(1, {'boards.Board': 1})
```





## 다음



참고

모듈 import 순서

1. 파이썬 표준 라이브러리 ex) os, random...
2. core django : 장고 프레임워크에 내장되어 있는 것 ex) django.shortcuts
3. 3rd party library : pip로 설치한 것들 ex)django-extension, bs4...
4. 장고 프로젝트 app





처음(render > 'index.html')에 글이 보이지 않았던 이유는 보여지는 페이지 자체를 index이지만 index의 url로는 돌아가지 못했기 때문

create는 model에 record를 생성해! 라는 요청이기 때문에. 단순히 페이지를 달라고 하는 GET 방식 보다는 POST가 의미상 더 적절하다

(그리고 모델과 관련된 데이터이기 때문에 url 에 직접 보여지는 것은 좋지 않다)



