from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("ping/", views.ping),
    path("pong/", views.pong),
    path("is-odd-even/<number_>/", views.isoddeven),
    path("calculator/<number1>/<number2>/", views.calculator),
    path("name/", views.name),
    path("prev/", views.prev),
    path("sentence/", views.sentence),
    path("lorem/", views.lorem),
]
