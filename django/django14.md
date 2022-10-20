# Django 14
## 참조 vs 역참조
### 모델
```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
```
- 참조
  - 내가 참조하는 table 접근
  - 해당 객체가 다른 객체의 ForeignKey를 가지고 있거나 1:1 관계인 상황에서 참조 하는 경우
  - 위와 같은 모델이 존재할 때 comment 모델에서 article을 불러들이는 것
- 역참조
  - 위와 반대로 article 모델이 comment 모델을 불러들이는 것
  - 다른 객체가 ForeignKey를 가지고 있거나 N:N 관계인 상황, 해당 객체를 참조하고 있는 다른 객체를 참조하려는 경우
    - `_set manager` 사용하기
      - `article.comment_set.all` : 글에 달린 댓글 가져오기
      - `user.article_set.all` : 로그인 한 유저가 쓴 글 가져오기
      - `user.comment_set.all` : 로그인 한 유저가 단 댓글 가져오기