# Django 04
## App URL mapping
- app의 view 함수가 많아지면서 사용하는 path() 또한 많아지고, 
app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음
- 하나의 프로젝트의 여러 앱이 존재한다면, 각각의 앱 안에 urls.py을 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁할 수 있음
- **각각의 app 폴더 안에 urls.py를 작성**하고 다음과 같이 수정 진행
```python
# articles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('dinner/', views.dinner),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.hello),
]
```
```python
# pages/urls.py
from django.urls import path

urlpatterns = [

]
```
### Including other URLconfs
- urlpattern은 언제든지 다른 URLconf 모듈을 포함(include)할 수 있음
- include되는 앱의 url.py에 urlpatterns가 작성되어 있지 않다면 에러가 발생
```python
# firstpjt/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```
#### `include()`
- 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 돕는 함수
- 함수 include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달

## Namespace
> 개체를 구분할 수 있는 범위를 나타내는 이름 공간

- 두번째 app pages의 index 페이지 작성시 문제 발생
1. 두번째 앱 index로 이동하는 하이퍼 링크를 클릭 시 현재 페이지로 다시 이동
2. index url(http://127.0.0.1:8000/pages/index/)로 직접 이동해도 articles app의 index 페이지가 출력됨

### URL namespace
- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 할 수 있음
- **app_name** attribute를 작성해 URL namespace를 설정
- “:” 연산자를 사용하여 지정
  - 예) app_name = 'articles', URL name = index -> 주소 참조 : **articles:index**

```python
# articles/urls.py
app_name = 'articles'

urlpatterns = [
  ...,
]
```
```html
<!-- articles/templates/index.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'articles:greeting' %}">greeting</a>
  <a href="{% url 'articles:dinner' %}">dinner</a>
  <a href="{% url 'articles:throw' %}">throw</a>
  <a href="{% url 'pages:index' %}">두번째 앱 index로 이동</a>
{% endblock %
```
```html
<!-- throw.html -->
{% extends 'base.html' %}
{% block content %}
  <h1>Throw</h1>
  <form action="{% url 'articles:catch' %}" method="GET">
    <label for="message">Throw</label>
    <input type="text" id="message" name="message">
    <input type="submit" value="던져">
  </form>
  <a href="{% url 'articles:index' %}">뒤로</a>
{% endblock content %}
```
```html
<!-- catch.html -->
<a href="{% url 'articles:throw' %}">다시 던지러</a>

<!-- greeting, dinner.html -->
<a href="{% url 'articles:index' %}">뒤로</a>
```
-> 첫번째 문제 해결

### Template namespace
- Django는 기본적으로 app_name/templates/ 경로에 있는 templates 파일들만 찾
을 수 있으며, settings.py의 INSTALLED_APPS에 작성한 app 순서로
template을 검색 후 렌더링 함
- Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해
폴더 구조를 app_name/templates/app_name/ 형태로 변경
- 폴더 구조 변경 후 변경된 경로로 해당하는 모든 부분을 수정하기
- Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해
폴더 구조를 **app_name/templates/app_name/** 형태로 변경

```python
# 폴더 구조 변경 후 변경된 경로로 해당하는 모든 부분 수정
# articles/views.py
return render(request, 'articles/index.html')

# pages/views.py
return render(request, 'pages/index.html')
```
### Naming URL patterns
- 문자열 주소를 바꿔야한다면 모든 곳을 찾아서 변경해야하는 번거로움이 발생하기 때문에 사용
- 링크에 URL을 직접 작성하는 것이 아니라 “path()” 함수의 name 인자를 정의해서 사용
- DTL의 Tag 중 하나인 URL 태그를 사용해서 “path()” 함수에 작성한 name을 사용할 수 있음
-  URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음
- `{% url '' %}`
```python
# articles/urls.py
urlpatterns = [
  path('index/', views.index, name='index'),
  path('greeting/', views.greeting, name='greeting'),
  path('dinner/', views.dinner, name='dinner'),
  path('throw/', views.throw, name='throw'),
  path('catch/', views.catch, name='catch'),
  path('hello/<str:name>/', views.hello, name='hello'),
]
```

## 장고의 디자인 패턴
> 각기 다른 기능을 가진 다양한 응용 소프트웨어를 개발할 때 공통적인 설계 문제가 존재하며, 이를 처리하는 해결책 사이에도 공통점이 있다는 것을 발견 -> 패턴
### MVC (Model - View – Controller) 소프트웨어 디자인 패턴
> 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론

- Model : 데이터와 관련된 로직을 관리
- View : 레이아웃과 화면을 처리
- Controller : 명령을 model과 view 부분으로 연결

#### MVC 소프트웨어 디자인 패턴의 목적
- 더 나은 업무의 분리와 향상된 관리를 제공
- 개발 효율성 및 유지보수가 쉬워짐
- 다수의 멤버로 개발하기 용이함

### MTV 디자인 패턴
|MVC|MTV|
|----|----|
|Model|Model|
|View|Template|
|Controller|View|
- Model
  - 데이터와 관련된 로직을 관리
  - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
  - MVC 패턴에서 Model의 역할에 해당
- Template
  - 레이아웃과 화면을 처리
  - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
  - MVC 패턴에서 View의 역할에 해당
- View
  - Model & Template과 관련한 로직을 처리해서 응답을 반환
  - 클라이언트의 요청에 대해 처리를 분기하는 역할
  - MVC 패턴에서 Controller의 역할에 해당

