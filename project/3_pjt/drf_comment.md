# 프로젝트 drf 댓글, 좋아요
## 댓/대댓글
### models.py
- 블로그 글에 달리 댓글까지 모두 응답으로 역참조 형태로 보내줄 것이기 때문에 blog에 related_name 설정
- 대댓글도 입력 가능하도록 parent를 셀프참조하여 저장
```python
from django.db import models
from django.conf import settings

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField('생성시간', auto_now_add=True)
```

### serializer.py
- comment로 user와 blog의 pk는 로그인한 유저와, 현재 url에 들어와 있는 pk를 views.py에서 넘겨줄 것이기 때문에 readOnlyField로 구성
- BlogSerializer에서 CommentSerializer를 read only로 보여준다.
```python
from .models import Blog, Comment
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    blog = serializers.ReadOnlyField(source="blog.pk")
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Blog
        fields = ['pk', 'title', 'body', 'comments']
```

### urls.py
```python
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns =[
    path('', views.BlogList.as_view()),
    path('<int:pk>/', views.BlogDetail.as_view()),
    path('<int:pk>/comments', views.Commentlist.as_view()),
    path('<int:blog_pk>/comments/<int:comment_pk>', views.Commentdetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
```

### views.py
```python
from .models import Blog, Comment
from .serializer import BlogSerializer, CommentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# comment의 목록을 보여주는 역할
class Commentlist(APIView):
    permissions_classes = [IsAuthenticated]

    # comment list를 보여줄 때
    def get(self, request, pk):
        comments = Comment.objects.filter(blog_id=pk)
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    # 새로운 comment를 작성할 때
    def post(self, request, pk):
        # request.data는 사용자의 입력 데이터
        serializer = CommentSerializer(data=request.data)
        blog = Blog.objects.get(pk=pk)
        if serializer.is_valid():  # 유효성 검사
            serializer.validated_data["user"] = request.user
            serializer.validated_data["blog"] = blog
            serializer.save()  # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# comemnt의 detail을 보여주는 역할
class Commentdetail(APIView):
    # comment 객체 가져오기
    def get_object(self, request, blog_pk, comment_pk):
        try:
            return Comment.objects.get(
                blog_id = blog_pk, pk=comment_pk
            )
        except Blog.DoesNotExist:
            raise Http404

    # comment의 detail 보기
    def get(self, request, blog_pk, comment_pk, format=None):
        comment = Comment.objects.get(
            blog_id=blog_pk, pk=comment_pk
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    # 새로운 recomment를 작성할 때
    def post(self, request, blog_pk, comment_pk):
        # request.data는 사용자의 입력 데이터
        serializer = CommentSerializer(data=request.data)
        blog = Blog.objects.get(pk=blog_pk)
        comment = Comment.objects.get(pk=comment_pk)
        if serializer.is_valid():  # 유효성 검사
            serializer.validated_data["user"] = request.user
            serializer.validated_data["parent"] = comment
            serializer.validated_data["blog"] = blog
            serializer.save()  # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # comment 수정하기
    def put(self, request, blog_pk, comment_pk, format=None):
        comment = Comment.objects.get(
            blog_id=blog_pk, pk=comment_pk
        )
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # comment 삭제하기
    def delete(self, request, blog_pk, comment_pk, format=None):
        comment = Comment.objects.get(
            blog_id=blog_pk, pk=comment_pk
        )
        if comment.user == request.user:
            comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

## 좋아요
### models.py
- Like라는 중계테이블을 만들어 user와 blog를 외래키로 사용한다.
```python
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
```

### serializer.py
- 모든 필드를 readonly 필드로 줘서 post 요청이 들어오면 알아서 해당 내용들이 db에 저장되도록 한다.
```python
class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    blog = serializers.ReadOnlyField(source="blog.pk")
    class Meta:
        model = Like
        fields = '__all__'
```
### views.py
- db에 좋아요 된 데이터가 있다면 삭제, 없다면 저장
```python
class Likelist(APIView):
    def get(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        likes = Like.objects.filter(blog=blog)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        # request.data는 사용자의 입력 데이터
        serializer = LikeSerializer(data=request.data)
        blog = Blog.objects.get(pk=pk)
        like = Like.objects.filter(blog_id=pk, user=request.user)
        if serializer.is_valid():  # 유효성 검사
            if not like:
                serializer.validated_data["user"] = request.user
                serializer.validated_data["blog"] = blog
                serializer.save()  # 저장
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                like.delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```