# Django 15
## M:N 관계
### 1:N의 한계
- 각각 2명의 의사와 환자를 생성하고 환자는 서로 다른 의사에게 예약을 했다고 가정

hospitals_doctor
|id|name|
|----|----|
|1|alice|
|2|bella|

hospitals_patient
|id|name|doctor_id|
|----|----|----|
|1|carol|1|
|2|dane|2|

- 1번 환자가 두 의사 모두에게 방문하려고 함

hospitals_doctor
|id|name|
|----|----|
|1|alice|
|2|bella|

hospitals_patient
|id|name|doctor_id|
|----|----|----|
|1|carol|1,2|
|2|dane|2|

- 동일한 환자지만 다른 의사에게 예약하기 위해서는 객체를 하나 더 만들어서 예약을 진행하야 함
- 외래 키 컬럼에 ‘1, 2’ 형태로 참조하는 것은 Integer 타입이 아니기 때문에 불가능

### 중계 모델
- 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 작성
- 예약 모델은 의사와 환자에 각각 1:N 관계를 가짐

hospitals_reservation
|id|doctor_id|patient_id|
|----|----|
|.|.|.|

```python
# hospitals/models.py

class Patient(models.Model):
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# 중개모델 작성
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

- 의사와 환자 생성 후 예약 만들기

hospitals_doctor
|id|name|
|----|----|
|1|alice|

hospitals_patient
|id|name|
|----|----|
|1|carol|

hospitals_reservation
|id|doctor_id|patient_id|
|----|----|----|
|1|1|1|

```python
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')

Reservation.objects.create(doctor=doctor1, patient=patient1)
```

- 예약 정보 조회
```bash
# 의사 -> 예약 정보 찾기
doctor1.reservation_set.all()
<QuerySet [<Reservation: 1번 의사의 1번 환자>]>

# 환자 -> 예약 정보 찾기
patient1.reservation_set.all()
<QuerySet [<Reservation: 1번 의사의 1번 환자>]>
```

- 1번 의사에게 새로운 환자 예약이 생성된다면

hospitals_doctor
|id|name|
|----|----|
|1|alice|

hospitals_patient
|id|name|
|----|----|
|1|carol|
|2|dane|

hospitals_reservation
|id|doctor_id|patient_id|
|----|----|----|
|1|1|1|
|2|1|2|

```python
patient2 = Patient.objects.create(name='dane’)

Reservation.objects.create(doctor=doctor1, patient=patient2)
```

- 1번 의사의 예약 정보 조회
```bash
# 의사 -> 환자 목록
doctor1.reservation_set.all()
<QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 1번 의사의 2번 환자>]>
```

### Django ManyToManyField
> Django는 ManyToManyField를 통해 중개 테이블을 자동으로 생성함

- 환자 모델에 Django ManyToManyField 작성
```python
# hospitals/models.py

class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}’
```

- 의사 1명과 환자 2명 생성
```bash
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='dane')
```

- 예약 생성 (환자가 의사에게 예약)
```bash
# patient1이 doctor1에게 예약
patient1.doctors.add(doctor1)

# patient1 - 자신이 예약한 의사목록 확인
patient1.doctors.all()
<QuerySet [<Doctor: 1번 의사 alice>]>

# doctor1 - 자신의 예약된 환자목록 확인
doctor1.patient_set.all()
<QuerySet [<Patient: 1번 환자 carol>]>
```

- 예약 생성 (의사가 환자를 예약)
```bash 
# doctor1이 patient2을 예약
doctor1.patient_set.add(patient2)

# doctor1 - 자신의 예약 환자목록 확인
doctor1.patient_set.all()
<QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 dane>]>

# patient1, 2 - 자신이 예약한 의사목록 확인
patient1.doctors.all()
<QuerySet [<Doctor: 1번 의사 alice>]>
patient2.doctors.all()
<QuerySet [<Doctor: 1번 의사 alice>]>
```

- 예약 취소하기 (삭제)
```bash
# doctor1이 patient1 진료 예약 취소
doctor1.patient_set.remove(patient1)
doctor1.patient_set.all()
<QuerySet [<Patient: 2번 환자 harry>]>
patient1.doctors.all()
<QuerySet []>
```

#### `related_name` argument
- target model이 source model을 참조할 때 사용할 manager name
- ForeignKey()의 related_name과 동일
```python
class Patient(models.Model):
    # ManyToManyField - related_name 작성
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

- related_name 설정 값 확인하기
```bash
# 1번 의사 조회하기
doctor1 = Doctor.objects.get(pk=1)

# 에러 발생 (related_name 을 설정하면 기존 _set manager는 사용할 수 없음)
doctor1.patient_set.all()
AttributeError:
'Doctor' object has no attribute 'patient_set'

# 변경 후
doctor1.patients.all()
<QuerySet []>
```

#### `through` argument
- 중개 테이블을 수동으로 지정하려는 경우 through 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
- 가장 일반적인 용도는 중개테이블에 추가 데이터를 사용해 다대다 관계와 연결하려는 경우

```python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```
### ManyToManyField
- `ManyToManyField(to, **options)`
- 다대다 (M:N, many-to-many) 관계 설정 시 사용하는 모델 필드
- 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있음 (`add()`,`remove()`, `create()`, `clear()`, ...)
#### 데이터베이스에서의 표현
- Django는 다대다 관계를 나타내는 중개 테이블을 만듦
- 테이블 이름은 ManyToManyField 이름과 이를 포함하는 모델의 테이블 이름을
조합하여 생성됨
- `db_table` arguments을 사용하여 중개 테이블의 이름을 변경할 수도 있음
##### ManyToManyField 인자
- `related_name`
  - target model이 source model을 참조할 때 사용할 manager name
  - ForeignKey의 related_name과 동일
- `through`
  - 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정
  - 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우에 사용됨
- `symmetrical`
  - 기본 값 : True
  - ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
  - True일 경우
    - _set 매니저를 추가 하지 않음
    - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)
  - False일 경우
    - 대칭을 원하지 않는 경우
#### Related Manager
- N:1 혹은 M:N 관계에서 사용 가능한 문맥(context)
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 역참조시에 사용할 수 있는 manager를
생성
- 같은 이름의 메서드여도 각 관계(N:1, M:N)에 따라 다르게 사용 및 동작
- 메서드 종류
  -  `add()`
    - 지정된 객체를 관련 객체 집합에 추가
    - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
    - 모델 인스턴스, 필드 값(PK)을 인자로 허용
  - `remove()`
    - 관련 객체 집합에서 지정된 모델 개체를 제거
    - 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제됨
    - 모델 인스턴스, 필드 값(PK)을 인자로 허용
  - `create()`, `clear()`, `set()` 
## 좋아요 기능 구현
### 모델 관계 설정
- like_users 필드 생성 시 자동으로 역참조에는 article_set 매니저가 생성되지만 이전 Article-User 관계에서 이미 해당 매니저를 사용중이다. 따라서 user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야 한다.
```python
# articles/models.py

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
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```
- User - Article간 사용 가능한 related manager 정리
  - article.user : 게시글을 작성한 유저 - N:1
  - user.article_set : 유저가 작성한 게시글(역참조) - N:1
  - article.like_users : 게시글을 좋아요한 유저 - M:N
  - user.like_articles : 유저가 좋아요한 게시글(역참조) - M:N
### LIKE 구현
```python
# articles/urls.py
urlpatterns = [
    ...
    path('<int:pk>/likes/', views.likes, name='likes'),
]
```
```python
# articles/views.py
def likes(request, pk):
    article = Article.objects.get(pk=pk)
    if article.like_users.filter(pk=request.user.pk).exists():
    # if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:detail', pk)
```
- `.exists()`
  - QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환
  - 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

```html
<!-- articles/index.html -->
{% extends 'base.html' %}
{% block content %}
  …
  {% for article in articles %}
      …
      <div>
        <form action="{% url 'articles:likes' article.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
            <input type="submit" value="좋아요 취소">
        {% else %}
            <input type="submit" value="좋아요">
        {% endif %}
        </form>
      </div>
  <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
  <hr>
  {% endfor %}
{% endblock content %}
```