from django.shortcuts import render
import random

foods = [('삼겹살', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5DL5WmsaUzKhKgYl03aRi7IRXSJIFM5b2uA&usqp=CAU'),
('짜장면', 'https://img.hankyung.com/photo/202205/99.24436255.1.jpg'),
('떡볶이', 'http://img.choroc.com/newshop/goods/024703/024703_1.jpg'),
]

def dinner(request):
  name, img = random.choice(foods)

  context = {
    'name': name,
    'img' : img,
  }

  return render(request, 'dinner.html', context)