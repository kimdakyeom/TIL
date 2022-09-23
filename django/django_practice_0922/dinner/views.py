from django.shortcuts import render
import random

foods = [('삼겹살', 'https://item.kakaocdn.net/do/513cd68136b86afae89226a3ec76c45ceffd194bae87d73dd00522794070855d'),
('마라탕', 'https://item.kakaocdn.net/do/513cd68136b86afae89226a3ec76c45c8f324a0b9c48f77dbce3a43bd11ce785'),
('떡볶이', 'https://item.kakaocdn.net/do/513cd68136b86afae89226a3ec76c45cf604e7b0e6900f9ac53a43965300eb9a'),
('쌀국수', 'https://item.kakaocdn.net/do/513cd68136b86afae89226a3ec76c45c9f5287469802eca457586a25a096fd31'),
('냉면', 'https://item.kakaocdn.net/do/513cd68136b86afae89226a3ec76c45c9f17e489affba0627eb1eb39695f93dd'),
('닭갈비', 'https://item.kakaocdn.net/do/513cd68136b86afae89226a3ec76c45c15b3f4e3c2033bfd702a321ec6eda72c'),
('곱창', 'https://item.kakaocdn.net/do/513cd68136b86afae89226a3ec76c45c4022de826f725e10df604bf1b9725cfd'),
('샐러드', 'https://item.kakaocdn.net/do/513cd68136b86afae89226a3ec76c45c8b566dca82634c93f811198148a26065'),
('샌드위치', 'https://item.kakaocdn.net/do/513cd68136b86afae89226a3ec76c45c82f3bd8c9735553d03f6f982e10ebe70'),
('라멘', 'https://item.kakaocdn.net/do/513cd68136b86afae89226a3ec76c45cd0bbab1214a29e381afae56101ded106'),
('돈가스', 'https://item.kakaocdn.net/do/513cd68136b86afae89226a3ec76c45c7f9f127ae3ca5dc7f0f6349aebcdb3c4'),
('파스타', 'https://item.kakaocdn.net/do/513cd68136b86afae89226a3ec76c45ca88f7b2cbb72be0bdfff91ad65b168ab'),
]

def dinner(request):
  name, img = random.choice(foods)

  context = {
    'name': name,
    'img' : img,
  }

  return render(request, 'dinner.html', context)