# 프로젝트 ORM 쿼리
> store을 store에 달린 리뷰에 따라 리뷰 개수순, 별점 높은순, 팔로우 많은순 세개의 필터로 보여줄 수 있도록 하기 위해 annotate, aggregate를 사용했다.

## 사용한 모델
- Store와 Review이며 아래와 같다.
- Store은 스토어에 대한 리뷰로 Review를 외래키로 참조한다.
```python
class Store(models.Model):
    name = models.TextField(max_length=30)
    lat = models.TextField()
    lon = models.TextField()    
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_stores', default=1)
    items = models.TextField()
    detail = models.TextField()
    following_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following_stores', blank=True)

class Review(models.Model):
    tags = models.ManyToManyField('Tag', related_name='tag_articles', blank=True)
    store_name = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_reviews', blank=True, null=True)
    restaurant_name = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_reviews', blank=True, null=True)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_reviews')
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
```

## annotate, aggregate
- `annotate()`는 QuerySet의 객체 하나하나에 부연 설명과 같은 것을 달아놓을 수 있다.
- `aggrate`은 QuerySet 객체를 합, 평균, 개수 등으로 계산할 수 있다.
- 외래키로 참조되어 있는 필드를 불러오기 위해서는 더블언더바(`__`)를 사용한다. -> 별점(grade)는 외래키로 참조되어 있는 필드이므로 `store_reviews__grade`로 가져왔다.
```python
from django.db.models import Count, Avg

def index(request):
    store = Store.objects.annotate(cnt_followings=Count('following_users'), avg_grade=Avg('store_reviews__grade'), cnt_reviews=Count('store_reviews'))
    store_review = store.order_by('-cnt_reviews')[:5]
    store_following = store.order_by('-cnt_followings')[:5]
    store_grade = store.order_by('-avg_grade')[:5]
    context = {
        "store_review": store_review,
        "store_grade": store_grade,
        "store_following": store_following,
    }
    return render(request, "articles/index.html", context)
```
- 카드를 슬라이드 형식으로 해서 코드가 약간 길다..

```html
<div class="tab-pane fade show active" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab" tabindex="0">
    <!-- 카드 슬라이더 효과 -->
    <div class='slider'>
        <div class='slide-track'>
            <!-- 이부분에 필터 씌울 내용을 넣기 -->
            {% for follow in store_following %}
                <div class='slide'>
                    <div class="train-card bg-white p-0 position-relative">
                        <a href="{% url 'foods:store_detail' team_pk=follow.team_id store_pk=follow.pk %}" class="text-decoration-none text-dark">
                        {% for image in follow.store_image.all %}
                            {% if forloop.counter == 1 %}
                                <img src="{{ image.image.url }}" class="card-img-top" alt="...">
                            {% endif %}
                        {% endfor %}
                        <div class="card-body py-2 border-top mb-5 pb-3">
                            <h5 class="card-title text-center my-3">{{follow.name}}</h5>
                            <p class="card-text small mx-3">
                            {{follow.items}}
                            </p>
                        </div>
                        <div class="position-absolute bottom-0 start-50 translate-middle-x w-100 pb-2">
                            <p class="small m-0 text-center">{{ follow.team.stadium.name }}</p>
                            <p class="small m-0 text-center">{{ follow.detail }}</p>
                            <p class="small m-0 text-center">
                            {% if follow.cnt_followings %}
                                <span class='small m-0'>팔로우 {{ follow.cnt_followings }}</span>
                            {% else %}
                                <span class='small m-0'>팔로우가 없습니다</span>
                            {% endif %}
                            </p>
                            <p class="small m-0 text-center">
                            {% if follow.store_reviews.all.count == 0 %}
                                <span class='small m-0'>평가가 없습니다</span>
                            {% else %}
                                {% for i in ""|ljust:follow.avg_grade %}
                                    <span>⭐</span>
                                {% endfor %}
                                <span>{{ follow.avg_grade|floatformat:"1" }}({{ follow.cnt_reviews }}명 평가)</span>
                            {% endif %}
                            </p>
                        </div>
                    </a>
                </div>
            </div>
        {% endfor %}

            <!-- 한번 더 반복하기 -->

            {% for follow in store_following %}
                <div class='slide'>
                  <div class="train-card bg-white p-0 position-relative">
                    <a href="{% url 'foods:store_detail' team_pk=follow.team_id store_pk=follow.pk %}" class="text-decoration-none text-dark">
                    {% for image in follow.store_image.all %}
                    {% if forloop.counter == 1 %}
                    <img src="{{ image.image.url }}" class="card-img-top" alt="...">
                    {% endif %}
                    {% endfor %}
                    <div class="card-body py-2 border-top mb-5 pb-3">
                      <h5 class="card-title text-center my-3">{{follow.name}}</h5>
                      <p class="card-text small mx-3">
                        {{follow.items}}
                      </p>
                    </div>
                    <div class="position-absolute bottom-0 start-50 translate-middle-x w-100 pb-2">
                      <p class="small m-0 text-center">{{ follow.team.stadium.name }}</p>
                      <p class="small m-0 text-center">{{ follow.detail }}</p>
                      <p class="small m-0 text-center">
                        {% if follow.cnt_followings %}
                        <span class='small m-0'>팔로우 {{ follow.cnt_followings }}</span>
                        {% else %}
                        <span class='small m-0'>팔로우가 없습니다</span>
                        {% endif %}
                      </p>
                      <p class="small m-0 text-center">
                      {% if follow.store_reviews.all.count == 0 %}
                      <span class='small m-0'>평가가 없습니다</span>
                      {% else %}
                      {% for i in ""|ljust:follow.avg_grade %}
                      <span>⭐</span>
                      {% endfor %}
                      <span>{{ follow.avg_grade|floatformat:"1" }}({{ follow.cnt_reviews }}명 평가)</span>
                      {% endif %}
                      </p>
                  </div>
                  </a>
                  </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
{% endfor %}
```

## 어려웠던 부분
외래키로 연결되어 있는 복잡한 형태의 데이터들을 어떻게 가져오면 좋을지 고민하다가 팀원이 Annotate와 Aggregate의 사용법을 알려주었다. 
ORM에 더 찾아보니 이 외에도 쿼리를 최적화하는 내용들이 많았다. ORM에 더 많은 공부를 해야할 필요성을 느꼈다.