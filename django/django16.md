# Django 16
## Profile 구현
- url 및 view 함수 작성
```python
# accounts/urls.py

urlpatterns = [
    …
    path('profile/<username>/', views.profile, name='profile'),
]
```
```python
# accounts/views.py

from django.contrib.auth import get_user_model
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
return render(request, 'accounts/profile.html', context)
```
- profile 템플릿 작성
```html
<!-- accounts/profile.html -->

{% extends 'base.html' %}
{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <hr>
  <h2>{{ person.username }}'s 게시글</h2>
  {% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
  {% endfor %}
<hr>
<h2>{{ person.username }}'s 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}
  <hr>
  <h2>{{ person.username }}'s 좋아요한 게시글</h2>
  {% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
  {% endfor %}
  <hr>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```
- Profile 템플릿으로 이동할 수 있는 하이퍼 링크 작성
```html
<!-- base.html -->

<body>
  <div class="container">
    {% if request.user.is_authenticated %}
      <h3>Hello, {{ user }}</h3>
      <a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
```
```html
<!-- articles/index.html -->

<p>
  <b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
</p>
```
## Follow 구현
- ManyToManyField 작성 및 Migration 진행
```python
# accounts/models.py

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```
- url 및 view 함수 작성
```python
# accounts/urls.py
urlpatterns = [
    ...,
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```
```python
# accounts/views.py
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
        # if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
```
- 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성
```html
<!-- accounts/profile.html -->

{% extends 'base.html' %}
{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    <div>
      팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
    </div>
    {% if request.user != person %}
      <div>
        <form action="{% url 'accounts:follow' person.pk %}" method="POST">
          {% csrf_token %}
          {% if request.user in person.followers.all %}
            <input type="submit" value="Unfollow">
          {% else %}
            <input type="submit" value="Follow">
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>
```

## View decorators & functions
### 데코레이터 (Decorator)
- 기존 함수를 수정하지 않고 기능을 추가해주는 wrapper 함수
- Django는 HTTP 처리를 위해 view 함수에 적용 할 수 있는 데코레이터를 제공
### 405 Method Not Allowed
- django.views.decorators.http의 데코레이터를 사용하여 요청 메서드를 기반으로 접근을 제한할 수 있음
- 일치하지 않는 메서드 요청이라면 405 Method Not Allowed를 반환
#### `require_http_methods()`
- View 함수가 특정한 요청 method만 허용하도록 하는 데코레이터
```python
# views.py

from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def create(request):
    pass
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    pass
```
#### `require_POST()`
- View 함수가 POST 요청 method만 허용하도록 하는 데코레이터
- POST 외에 다른 요청이 들어오면 405 http status code
```python
# views.py

from django.views.decorators.http import require_http_methods, require_POST

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```
#### `require_safe()`
- require_GET이 있지만 Django에서는 require_safe를 사용하는 것을 권장
```python
# views.py

from django.views.decorators.http import require_http_methods, require_POST, require_safe
@require_safe
def index(request):
    ...
@require_safe
def detail(request, pk):
    ...
```

### 404 Not Found
- Django Shortcut functions : 해당하는 객체가 존재하지 없는 경우 404 상태코드를 반환
  - `get_object_or_404(klass, *args, **kwargs)`
  - `get_list_or_404(klass, *args, **kwargs)`