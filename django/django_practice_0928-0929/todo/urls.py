from django.urls import path
from . import views

# url namespace
# url을 이름으로 분류하는 기능

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("modify/<int:pk>", views.modify, name="modify"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),
]
