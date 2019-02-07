# ORM(Object-Relational Mapping)

1. CRUD 크루드

   - 소프트웨어 설계의 기본

2. Database <-> Code : SQL로 소통 -> 문제

   - SQL 숙지해야함 - 개발 생산성 떨어짐

   - DB에 종속


> 그래서 <u>ORM(번역기 역할)</u>을 씀!

1. <u>**장점**</u>
   - 코드 간소화
   - 객체지향적인 코드로 인해 직관적이고 비즈니스 로직에 더 집중할 수 있게 함
   - 재사용, 유지보수가 쉬움
   - DB에 대한 종속성이 줄어듦

2. <u>**단점**</u>
   - 오로지 ORM으로만은 거대한 서비스를 구현하기 어려움
   - 어느 정도의 속도 저하 (미미)



## ORM 실습



### 기본 세팅

```
$ pip install flask_sqlalchemy
$ pip install flask_migrate
```

```python
#app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# flask app 에 sqlalchemy 관련 설정
## 1. db_flask 만듬
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
## 2. sqlalchemy 데이터베이스 객체 수정 및 신호 방출 등을 추적하는 기능을 끔
### 메모리를 과도하게 사용하기 때문에
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlalchemy 초기화
db = SQLAlchemy(app)
# migrate도
migrate = Migrate(app, db)

# 테이블을 객체로 취급할 것이기 때문에 class로 테이블 생성
class User(db.Model):
    __tablename__ = 'users'
    # primary_key=True : pk
    id = db.Column(db.Integer, primary_key=True)
    # string을 80으로 제한, unique : 중복값 제한, nullable : 빈 값 가능
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User '{self.username}'>"
        

# 위와 같음    
# CREATE TABLE users (
#     id INTEGER PRIMARY KEY,
#     username TEXT,
#     email TEXT);
```

```
$ flask db init
$ flask db migrate
$ flask db upgrade
```

> /orm/ 에 db_flask.sqlite3와 /orm/migrations/ 생성됨

---



### ORM으로 CRUD짜기



#### 1. CREATE

```
>>> from app import *
>>> user = User(username='yerang', email='example@gmail.com')
>>> db.session.add(user)
>>> db.session.commit()
>>> user.username
'yerang'
>>> user.email
'example@gmail.com'
```
위를 sql 문법으로 나타내면
```sql
INSERT INTO users (username, email)
VALUES ('yerang', 'example@gmail.com')
```



#### 2. READ



```sql
SELECT * FROM users;
```

```
>>> users = User.query.all()
```



```sql
SELECT * FROM users WHERE username='yerang';
```

```
>>> users=User.query.filter_by(username='yerang').all()
```



```sql
SELECT * FROM users WHERE username='yerang' LIMIT 1;
```

```
>>> users=User.query.filter_by(username='yerang').first()
```

없는 값을 찾으면 None 리턴

```
>>> miss = User.query.filter_by(username='ssafy').first()
>>> type(miss)
<class 'NoneType'>
```



id값으로 접근 ( Get one by id ) : PK만 GET으로 가져올 수 있음

```sql
SELECT * FROM users WHERE id=1;
```

```
>>> user = User.query.get(1)
```



LIKE

```sql
SELECT * FROM
```

```
>>> users = User.query.filter(User.email.like('%exam%')).all()
```



```
# 2개 건너뛰고 1개만 select > 3번째꺼
>>> users = User.query.limit(1).offset(2).all()
```



#### 3. UPDATE

```python
>>> user
<User 'yerang'>
>>> user.username
'yerang'
>>> user.username = 'ssafy'
# update 할 때는 add 안해도 됨 
>>> db.session.commit()
>>> user.username
'ssafy'
```



#### 4. DELETE

```python
>>> user = User.query.get(1)
>>> db.session.delete(user)
>>> db.session.commit()
```



---



### 모듈화 : 모델 분리하기

> 왜? > 모델 여러개면 app.py 엄청 거대해짐 > 모듈화

```python
# models.py
from flask_sqlalchemy import SQLAlchemy

# app.py 에서 table 생성하는 class 분리

# app.py 에서 가져옴
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    # primary_key=True : pk
    id = db.Column(db.Integer, primary_key=True)
    # string을 80으로 제한, unique : 중복값 제한, nullable : 빈 값 가능
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User '{self.username}'>"
```

```python
# app.py
from models import db, User

# db = SQLAlchemy(app) 주석
## 분리할 때는 아래처럼 초기화
db.init_app(app)

## class 삭제
```



---



### FLASK_ORM

### 

### 1) C, R

##### 1. app.py

```python
@app.route('/')
# 뷰 함수
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

# db처리하는 함수
@app.route('/users/create')
def create():
    username = request.args.get('username')
    email = request.args.get('email')
    # 왼쪽이 컬럼 이름
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
```

##### 2. index.html

```html
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    <!-- css시트 등 추가할 때 base에 먹히니까 super 속성을 줌 -->
    {{ super() }}
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
{% endblock %}
{% block body %}
    <form action ="/users/create">
        <input type="text" name="username"/>
        <input type="email" name="email"/>
        <input type="submit" value="Submit"/>
    </form>
    
    <ul>
        {% for user in users %}
            <li>{{ user.username }} : {{ user.email }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

##### 3. base.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <!-- block 태그는 파생된 템플릿이 변경할 수 있는 항목을 정의함-->
    {% block head %}
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>{% block title %}{% endblock %} - My webpage</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    {% endblock %}
</head>

<body>
    <div class="container">
        <h1>이것은 BASE의 h1입니다.</h1>
        {% block body %}
        {% endblock %}
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>

</html>

```



### 2) D

```python
# app.py
# int 없이 하면 하나만 딜리트해도 다 날아감
@app.route('/users/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
```



### 3) E

```python
# app.py
# edit은 2개 필요함
@app.route('/users/edit/<int:id>')
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)

@app.route('/users/update/<int:id>')
def update(id):
    user = User.query.get(id)
    username = request.args.get('username')
    email = request.args.get('email')
    
    user.username = username
    user.email = email
    db.session.commit()
    
    return redirect(url_for('index'))
```

```html
<!-- edit.html -->
{% extends "base.html" %}

{% block body %}
    <h1>여기는 수정페이지입니다.</h1>
    <form action="/users/update/{{ user.id }}">
        
        <!-- value 값 넣어주는 게 좋음( 변경 전 내용 미리 떠있게 ) -->
        <input type="text" value="{{ user.username }}" name='username'/>
        <input type="text" value="{{ user.email }}" name='email'/>
        <input type="submit" value="Submit"/>
    </form>
{% endblock %}
```





