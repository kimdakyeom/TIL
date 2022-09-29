from django.shortcuts import render, redirect
from .models import Article


def index(request):
    # DB에서 가져오기
    guestbook = Article.objects.all()

    return render(request, "articles/index.html", {"guestbook": guestbook})


def create(request):
    content = request.GET.get("content")
    # DB에 저장
    Article.objects.create(content=content)

    return redirect("articles:index")
