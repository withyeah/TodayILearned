# Django_intro

20190213


**Content**

[0. 준비 사항](#0-준비사항)

[1. Django start](#1-django-start)

[2. MTV](#2-mtv)

[3. views-urls](#3-views-urls)

[4. Template](#4-template)

[5. Form](#5-form)

[6. Template Inheritance](#6-template-inheritance)



## Intro

### A. Django

- Opinionated 다소 독선적
- MTV (model template view) / MVC (model view controller) 
  - 장고는 굳이 MVC 안 쓰고 MTV라고 함,,,



## 0. 준비사항

1. pyenv > python > pyenv-virtualenv 설치 및 설정
   - python 3.6.7
   - git

   ```
   # install pyenv
   git clone https://github.com/pyenv/pyenv.git ~/.pyenv
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
   source ~/.bashrc
   pyenv install 3.6.7
   pyenv global 3.6.7
   pyenv rehash
   
   # install pyenv-virtualenv
   git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
   echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
   source ~/.bashrc
   ```

2. 가상환경 생성

   ```
   # 가상환경 생성
   pyenv virtualenv 3.6.7 가상환경명
   
   # 가상환경 확인
   pyenv virtualenvs
   ```

3. 프로젝트 폴더 생성 및 이동

4. local 가상환경 활성화

   ```
   pyenv local 가상환경명
   ```

5. 장고 설치

   ```
   pip install django
   ```

   

---



## 1. Django start

### 1.1 장고 프로젝트

1. 프로젝트 생성

   > django, test, class, - 등은 프로젝트 이름으로 사용하면 안됨

   ```
   django-admin startproject 프로젝트명
   ```

2. 서버 실행

   > ALLOWED_HOSTS = [*]
   >
   > or
   >
   > ALLOWED_HOSTS = ['example-username.c9users.io']

3. `.gitignore` 설정 (gear > show hidden files)

   > root dir에 .gitignore 만들어준 후 gitignore.io에서 내용 가져다 붙이기

4. TIMEZONE / LANGUAGE_CODE 설정

5. 로켓 페이지 한글화 확인

   ```
   # runserver (c9 환경에서)
   python manage.py runserver $IP:$PORT
   
   # local에서는
   python manage.py runserver
   ```

6. 프로젝트 구조 확인

   - `manage.py` : 장고 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
   - `프로젝트이름폴더` : 디렉토리 내부에는 프로젝트를 위한 실제 파이썬 패키지들이 저장됨. 이 디렉토리 내의 이름을 이용하여 프로젝트 어디서나 파이썬 패키지들을 import 할 수 있음
   - `settings.py` : 현재 장고 프로젝트의 모든 환경과 구성을 저장함
   - `__init__.py` : 파이썬으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일
   - `urls.py` : 현재 장고 프로젝트의 URL선언을 저장. 사이트의 URL과 VIEWS의 연결을 지정.
   - `wsgi.py` : 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점 (Web Server Gateway Interface)

---

### 1.2 장고 어플리케이션(APP)

- 실제로 특정한 역할을 하는 친구가 바로 APP
- 프로젝트는 이러한 어플리케이션의 집합
- 하나의 프로젝트는 여러 개의 어플리케이션을 가질 수 있음
- 각각의 어플리케이션은 MTV 패턴으로 구성되어 있음

> <u>project 와 app 의 차이점?</u> 
>
> app 은 (블로그나 공공 기록물을 위한 데이터베이스나, 간단한 설문조사 앱과 같은) 특정한 기능을 수행하는 웹 어플리케이션을 말합니다. project 는 이런 특정 웹 사이트를 위한 app 들과 각 설정들을 한데 묶어놓은 것 입니다. project 는 다수의 app 을 포함할 수 있고, app 은 다수의 project 에 포함될 수 있습니다.



1. 어플리케이션 만들기

   ```
   python manage.py startapp 앱이름
   ```

2. 어플리케이션 구조

   - `admin.py` : 관리자용 페이지 커스터마이징 장소
   - `apps.py` : 앱의 정보가 있는 곳. 우리는 수정할 일이 없다
   - `models.py` : 앱에서 사용하는 Model을 정의하는 곳
   - `test.py` : 테스트 코드를 작성하는 곳
   - `views.py` : 뷰들이 정의되는 곳. 사용자에게 어떤 데이터를 보여줄 지 구현되는 곳.

3. 어플리케이션 등록 (settings) `예시) 앱 이름 : home`

   > /home > apps.py > class 들어가보면 `HomeConfig()` 이 있다!
   >
   > settings.py 의 `INSTALLED_APPS` 리스트에 
   >
   > `home.apps.HomeConfig,` 등록 (대문자 주의)
   >
   > 혹은 그냥 `home`이름 만으로 작성 가능, 다만 추후 자세한 설정을 할 수 없다

---



## 2. MTV

- 장고를 제외하면 일반적으로 MVC 패턴으로 사용된다.
  - **M**odel : 어플리케이션의 핵심 로직의 동작을 수행한다. (Database)
  - **T**emplate(View) : 어떻게 데이터가 보여질지를 수행한다. (Interface)
  - **V**iew(Controller) : 어떤 데이터를 보여줄지를 구현한다. (Logic)
- .py 3대장
- `models.py` : 데이터베이스 관리
- `views.py` : 페이지 관리 (페이지 하나 당, 하나의 함수)
- `urls.py` : 주소(URL) 관리

> flask 에서 app.py 한 곳에서 했던 걸, django 는 모두 나눠서 한다.



## 3. views-urls

우리는 앞으로 views > urls > template 순으로 코드를 작성할 것 ( 실행은 url > views > template 순으로 된다 )

1. views 설정 (`home/views.py`)

   ```python
   from django.shortcuts import render, HttpResponse
   # 혹은 from django.http import HttpResponse
   
   # Create your views here.
   def index(request):
       return HttpResponse('Welcome to Django !')
   ```

   > 여기서 우리가 접속해서 볼 페이지를 작성한다.

2. urls 설정 (`django_intro/urls.py`)

   ```python
   from django.contrib import admin
   from django.urls import path
   from home import views
   
   urlpatterns = [
       path('home/index/', views.index, name='index'),
       path('admin/', admin.site.urls),
   ]
   ```

   - 장고 서버로 요청(`request`)이 들어오면, 이 요청이 어디로 가야하는지 인식하고 관련된 함수(view)로 넘겨준다.

     ```python
     def index(request):
         # 실제로 어떤 값이 오는지 확인해보자.
         print(request) # <WSGIRequest: GET '/home/'>
         print(type(request)) # <class 'django.core.handlers.wsgi.WSGIRequest'>
         print(request.META)
     	return HttpResponse('Welcome to Django !')
     ```

   - 위에서부터 하나씩 검사하면서 찾기 때문에 순서가 중요하다. 아직은 이 순서 때문에 문제가 생기지 않지만 후에 복잡한 페이지가 만들면 이 순서가 중요해진다.

   - flask 에서 `app.route()`의 역할을 하나의 파일로 모아 놓은 것이다.



 > **path()** 함수 [[doc\]](https://docs.djangoproject.com/ko/2.1/intro/tutorial01/#path-argument-route)
   >
   > - `path()`함수에는 2개의 필수 인수인 `route` 와 `view`, 2개의 선택 가능한 인수로 `kwargs` 와 `name` 까지 모두 4개의 인수가 전달된다. (`kwargs` 는 다루지 않는다.)
   > - `path(route, view, name)`
   >
   > **HttpResponse**
   >
   > - HttpResponse(content='', content_type=None, status=200, reason=None, charset=None)
   > - Content 로 넘겨줄 수 있는 것은 iteraror 혹은 string 만 가능하다.
   >   - iterator 는 join 해서 string 으로 만들어서 넘겨주고, int 는 string 으로 형변환해서 넘겨준다.
   >
   > **나중에 url 을 나누게 된다면, 직접 app 에 urls.py 를 만들고 아래처럼 구조를 만든다.**
   >
   > ```python
   > # app url
   > from django.urls import path
   > from . import views
   > 
   > url patterns = [
   >  path('index/', views.index, name='index')
   > ]
   > ```
   >
   > ```python
   > # 프로젝트 url
   > from django.contrib import admin
   > from django.urls import include, path
   > 
   > urlpatterns = [
   >  path('home/', include('home.urls')),
   >  path('admin/', admin.site.urls),
   > ]
   > ```



- HttpResponse로 첫 리턴 값 출력해보기

  ```python
  # views.py
  from django.shortcuts import render, HttpResponse
  
  def index(request):
      return HttpResponse('Welcome to Django !')
  ```

  ```python
  # urls.py
  from home import views
  
  urlpatterns = [
      path('index/', views.index, name='index'),
      path('admin/', admin.site.urls),
  ]
  ```

- 저녁 메뉴 리턴 실습

  ```python
  # views.py
  import random
  
  def dinner(request):
      menus = ['a', 'b', 'c']
      pick = random.choice(menus)
      return HttpResponse(pick)
  ```

  ```python
  # urls.py > urlpatterns 리스트에 추가
  path('dinner/', views.dinner, name='dinner'),
  ```

  

---



## 4. Template

- 장고에서 사용되는 템플릿은 DTL(Django Template Language) 이다.
- jinja2와 문법이 유사하지만 다르다.

### 4.1 Template Variable

- render()
  - render(request, template_name, context=None, content_type=None, status=None, using=None) 앞 2가지 필수인수 나머지는 선택. context는 딕셔너리로 

---

### 4.2 Variable Routing

```python
# urls.py > urlpatterns 리스트에 추가
path('hello/<name>/', views.hello, name='hello'),
```

> url/hello/<이름> 입력 시 이름을 name이라는 key에 value로 담아 views의 hello함수에 넘겨줌

```python
def hello(request, name):
	return render(request, 'hello.html', {'name':name}) 
```

> name으로 받은 value를 'name'에 담아서 hello.html로 넘겨줌

```html
<!-- hello.html -->
<h1>Hello {{ name }} !</h1>
```

---



## 5. Form

- request.GET.get('data')

- request.POST.get('data')

> {% csrf_token %}를 form 안에서 같이 보내줘야 함 (보안)
>
> cf) csrf 공격과 같은 보안과 관련된 사항은 settings의 MIDDLEWARE에 되어 있다, 실제로 요청은 MIDDLEWARE 설정 사항들을 순차적으로 거친다 (위에서 아래로). 응답은 아래에서 위로 거쳐서 응답이 리턴된다. (장고는 코드의 순서가 매우 중요한 프레임워크)

#### 핑퐁

1. GET 방식

   ```python
   # views.py
   def user_new(request):
       return render(request, 'user_new.html')
       
   def user_create(request):  # 주의! 인자는 request만 받는다
       nickname = request.GET.get('nickname')
       pwd = request.GET.get('pwd')
       return render(request, 'user_create.html', {'nickname':nickname, 'pwd':pwd})
   ```

   ```python
   path('user_create/', views.user_create, name='user_create'),
   path('user_new/', views.user_new, name='user_new'),
   ```

   ```html
   <!-- user_new.html -->
   <form action='/user_create'>
       <input type="text" name="nickname"/>
       <input type="text" name="pwd"/>
       <input type="submit" value="Submit"/>
   </form>
   ```

   ```html
   <!-- user_create.html -->
   <h1>닉네임 : {{ nickname }}</h1>
   <h1>패스워드 : {{ pwd }}</h1>
   ```

2. POST 방식

   - post 는 url 끝에 슬래쉬(`/`) 필수

   ```python
   def user_create(request):
       nickname = request.POST.get('nickname')
       pwd = request.POST.get('pwd')
       return render(request, 'user_create.html', {'nickname':nickname, 'pwd':pwd})
   ```

   ```html
   <form action='/user_create/' method='post'>
       {% csrf_token %}
       <input type="text" name="nickname"/>
       <input type="text" name="pwd"/>
       <input type="submit" value="Submit"/>
   </form>
   ```



---



## 6. Template Inheritance

앱/templates/base.html 생성

- `home/templates/base.html` 만들기 (+bootstrap)

  > html 파일 모두 상속받게 수정하기

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>{% block title %}{% endblock %}</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/css/bootstrap.min.css" integrity="sha384-PDle/QlgIONtM1aqA2Qemk5gPOE7wFq8+Em+G/hmo5Iq0CCmYZLv3fVRDJ4MMwEA" crossorigin="anonymous">
  </head>
  <body>
      <h1>장고 연습</h1>
      <hr>
      <div class="container">
          {% block body %}
          {% endblock %}
      </div>
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/js/bootstrap.min.js" integrity="sha384-7aThvCh9TypR7fIc2HV4O/nFMVCBwyIUKL8XCtKE+8xgCgl/PQGuFsvShjr74PBp" crossorigin="anonymous"></script>
  </body>
  </html>
  ```