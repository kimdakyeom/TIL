from django.db import models

# Genre 클래스를 만드는데,
# models.Model 내부 클래스를 상속 받는다. 
# 왜 상속 받을까요? 기능들을 활용하고 싶어서. (미리 만들어진)


class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField(null=True,default='')


# class Person:
#     pass 

# # iu라고 하는 변수의 이름을 가진
# # Person 클래스의 인스턴스를 만드는 코드는?
# iu = Person() 
# # iu의 name 속성으로 아이유라고 하는 코드는?
# iu.name = '아이유'
