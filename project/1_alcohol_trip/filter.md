# Django 필터
> 검색 기능과 카테고리 기능을 구현하였다.

## 검색 기능
- AND
```python
from .models import Restaurant

def search(request):
    restaurant = Restaurant.objects.filter(name="와이키키", category="바")
    return render(request, 'bars/search.html', {"restaurant": restaurant,})
```
- OR
```python
# bars/views.py

from .models import Restaurant
from django.db.models import Q
def search(request):
    searched = request.GET['searched']
    restaurants = Restaurant.objects.filter(
        Q(name__contains=searched)|
        Q(category__contains=searched)|
        Q(address__contains=searched)
        ).distinct().order_by('name')
    restaurants_count = restaurants.count()
    context = {
        "searched": searched,
        "restaurants_count": restaurants_count,
        "restaurants": restaurants,
    }
    return render(request, 'bars/search.html', context)
```
- `Q()` 를 이용해 여러 조건을 동시에 사용
```python
# bars/views.py

from .models import Restaurant
from django.db.models import Q

def search(request):
    q = Q()

    q.add(Q(name="와이키키"), q.AND)
    q.add(Q(address="서울")|Q(address="강원"), q.AND)
    q.add(~Q(category="포장마차"), q.AND)

    result = Restaurant.objects.filter(q)
return render(request, 'bars/search.html', {"result": result,})
```
1. `q = Q()` 로 선언
2. `q.add` 로 조건 추가
3. `q.add(Q(Field명=찾는 값), q.AND)` : 두번째 인자인 q.AND 는 앞의 값과 AND로 연결하는 역할
4. `q.add(Q(Field명=찾는 값), q.OR)` : 두번째 인자인 q.OR은 앞의 값과 OR로 연결하는 역할

## 카테고리 기능
- url에 카테고리 전달
```python
# bars/urls.py

urlpatterns = [
    path("<category>/category/", views.category, name="category"),
]
```
- url에 카테고리 전달
```html
<!-- base.html -->
<li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
    카테고리로 술집 찾기
    </a>
    <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="{% url 'bars:category' 'beer' %}">맥주, 호프</a></li>
    <li><a class="dropdown-item" href="{% url 'bars:category' 'izakaya' %}">이자카야</a></li>
    <li><a class="dropdown-item" href="{% url 'bars:category' 'pojangmacha' %}">포장마차</a></li>
    <li><a class="dropdown-item" href="{% url 'bars:category' 'restaurant' %}">요리주점</a></li>
    <li><a class="dropdown-item" href="{% url 'bars:category' 'bar' %}">바(BAR)</a></li>
    </ul>
    </li>
```
- url에 영어로 전달된 카테고리를 DB에 저장된 한글로 변환
- 해당하는 카테고리의 객체를 불러오기
```python
def category(request, category):
    category_table = {
        "beer": "맥주, 호프",
        "izakaya": "이자카야",
        "pojangmacha": "포장마차",
        "restaurant": "요리주점",
        "bar": "바(BAR)",
    }
    k_category = category_table.get(category)
    restaurants = Restaurant.objects.filter(category=k_category)
    # 입력 파라미터
    page = request.GET.get("page", "1")
    # 페이징
    paginator = Paginator(restaurants, 8)
    page_obj = paginator.get_page(page)
    print(restaurants)
    context = {
        "k_category": k_category,
        "restaurants": restaurants,
        "restaurants": page_obj,
    }
    return render(request, "bars/category.html", context)
```