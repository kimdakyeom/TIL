from django.shortcuts import render
import random

def index(request):
  # 환영하는 메인 페이지
  names = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ']

  name = random.choice(names)

  context = {
    'name' : name,
    'img': 'https://img2.quasarzone.com/editor/2021/04/29/4de4a853c5ad342eb3c024b688b89837.jpg',
  }

  return render(request, 'index.html', context)

def welcome(request, name):
  # url에 이름을 넣으면 해당 이름을 환영하는 페이지
  context = {
    'name': name,
  }

  return render(request, 'welcome.html', context)