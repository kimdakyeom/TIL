# Django 페이지네이션
> 많은 양의 식당 데이터가 있었기 때문에 페이징 처리를 할 필요성을 느껴서 구현하였다.

## 검색 후 결과 데이터들 페이지네이션
- views.py
```python
from django.core.paginator import Paginator 
def search(request):
    searched = request.GET['searched']
    restaurants = Restaurant.objects.filter(
        Q(name__contains=searched)|
        Q(category__contains=searched)|
        Q(address__contains=searched)
        ).distinct().order_by('name')
    restaurants_count = restaurants.count()
    # 입력 파라미터
    page = request.GET.get("page", "1")
    # 페이징
    paginator = Paginator(restaurants, 16)
    page_obj = paginator.get_page(page)
    context = {
        "searched": searched,
        "restaurants_count": restaurants_count,
        "restaurants": page_obj,
    }
    return render(request, 'bars/search.html', context)
```
- index.html
  - 검색기능 구현
  - `method="get"`으로 처리해서 주소창에 `/?searched="검색 내용"`이 함께 전달된다.
```html
<div class="container">
  <div class="d-flex justify-content-center align-items-center" style="height: 300px;">
    <form class="d-flex w-75 h-25" role="search"  method="GET" action="{% url 'bars:search' %}">
      <input class="form-control me-2" name="searched" type="search" placeholder="술집 이름/카테고리/지역을 입력하세요" aria-label="Search">
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
  </div>
</div>
```
- search.html
```html
<!-- 페이징처리 시작 -->
<ul class="pagination justify-content-center">
  <!-- 이전페이지 -->
  {% if restaurants.has_previous %}
  <li class="page-item">
    <a class="page-link" href="?page={{ restaurants.previous_page_number }}&searched={{searched}}">이전</a>
  </li>
  {% else %}
  <li class="page-item disabled">
    <a class="page-link" tabindex="-1" aria-disabled="true" href="#">이전</a>
  </li>
  {% endif %}
    <!-- 페이지리스트 -->
  {% for page_number in restaurants.paginator.page_range %}
  {% if page_number >= restaurants.number|add:-3 and page_number <= restaurants.number|add:3 %}
  {% if page_number == restaurants.number %}
  <li class="page-item active" aria-current="page">
    <a class="page-link" href="?page={{ page_number }}&searched={{searched}}">{{ page_number }}</a>
  </li>
  {% else %}
  <li class="page-item">
    <a class="page-link" href="?page={{ page_number }}&searched={{searched}}">{{ page_number }}</a>
  </li>
  {% endif %}
  {% endif %}
  {% endfor %}
  <!-- 다음페이지 -->
  {% if restaurants.has_next %}
  <li class="page-item">
    <a class="page-link" href="?page={{ restaurants.next_page_number }}&searched={{searched}}">다음</a>
  </li>
  {% else %}
  <li class="page-item disabled">
    <a class="page-link" tabindex="-1" aria-disabled="true" href="#">다음</a>
  </li>
  {% endif %}
</ul>
<!-- 페이징처리 끝 -->
```

## 구현하며 어려웠던 부분
대부분 문서들을 보면 nav바에 검색 창을 구현해서 어떤 페이지가 됐든 검색 내용에 대한 요청을 받아 페이지네이션 처리가 되었다.

우리 프로젝트는 index 페이지에서 검색을 하면 검색 결과를 search.html에서 보여주었는데, 페이지마다 get 요청을 받지 못해서 url에 get 요청을 받아온 내용을 이동하는 링크에 덧붙혀줬다.