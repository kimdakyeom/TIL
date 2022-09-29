from django.urls import path
from . import views

app_name = "practices"

urlpatterns = [
    path("", views.index),
    path("ping/", views.ping, name="ping"),
    path("pong/", views.pong, name="pong"),
    path("is-odd-even/<number_>/", views.isoddeven, name="is-odd-even"),
    path("calculator/<number1>/<number2>/", views.calculator, name="calculator"),
    path("name/", views.name, name="name"),
    path("prev/", views.prev, name="prev"),
    path("sentence/", views.sentence, name="sentence"),
    path("lorem/", views.lorem, name="lorem"),
]
