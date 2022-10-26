# Django 17
## 비동기 처리
### Axios
- 브라우저를 위한 Promise 기반의 클라이언트
- 원래는 “XHR”이라는 브라우저 내장 객체를 활용해 AJAX 요청을 처리하는데, 이보다 편리한 AJAX 요청이 가능하도록 도움을 줌
```html
<!-- Axios -->
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
  const URL = 'https://jsonplaceholder.typicode.com/todos/1'
  axios.get(URL)
    .then(res => console.log(res.data.title))
    .catch(err => console.log('Error!’))
</script> 
```
```html
<script>
  const xhr = new XMLHttpRequest()
  const URL = 'https://jsonplaceholder.typicode.com/todos/1'
  xhr.open('GET', URL)
  xhr.send()
  xhr.onreadystatechange = function (event) {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      const status = event.target.status
        if (status === 0 || (status >= 200 && status < 400)) {
        const res = event.target.response
        const data = JSON.parse(res)
        console.log(data.title)
        } else {
        console.error('Error!')
        }
    }
  }
</script>
```
### Promise
- 비동기 작업을 관리하는 객체
  - 미래의 완료 또는 실패와 그 결과 값을 나타냄
  - 미래의 어떤 상황에 대한 약속
- `.then()` : 성공(이행)에 대한 약속
  - 이전 작업(promise)이 성공했을 때(이행했을 때) 수행할 작업을 나타내는 callback 함수
  - 각 callback 함수는 이전 작업의 성공 결과를 인자로 전달받음
  - 성공했을 때의 코드를 callback 함수 안에 작성
- `.catch()` : 실패(거절)에 대한 약속
  - .then이 하나라도 실패하면(거부 되면) 동작 (동기식의 ‘try - except’ 구문과 유사)
  - 이전 작업의 실패로 인해 생성된 error 객체는 catch 블록 안에서 사용할 수 있음
- `.finally(callback)`
  - Promise 객체를 반환
  - 결과와 상관없이 무조건 지정된 callback 함수가 실행
  - Promise가 성공되었는지 거절되었는지 판단할 수 없기 때문에 어떠한 인자도 전달받지 않음
  - 무조건 실행되어야 하는 절에서 활용(`.then()`과 `.catch()` 블록에서의 코드 중복을 방지)
- `.then()`을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음 (Chaining)
- callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
  - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
  - 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용한 경우도 마찬가지
## 비동기 적용하기
### 팔로우 (follow)
- axios CDN 작성
```html
<!-- accounts/profile.html -->
{% block script %}
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
  </script>
{% endblock script %}
```
- form 요소 선택을 위해 id 속성 지정 및 선택
- form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소
- axios 요청 준비
- url에 작성할 user pk 가져오기 (HTML -> JavaScript)
```html
<!-- accounts/profile.html -->

<form id="follow-form" data-user-id="{{ person.pk }}">
  ...
</form>
```
```html
<!-- accounts/profile.html -->

<script>
  const form = document.querySelector('#follow-form')
  form.addEventListener('submit', function (event) {
    event.preventDefault()
    const userId = event.target.dataset.userId
    axios({
      method: 'post',
      url: `/accounts/${userId}/follow/`,
    })
  })
</script>
```

#### `data-*` attributes
- 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM사이에서 교환 할 수 있는 방법
- 예) `data-test-value`라는 이름의 특성을 지정했다면 JavaScript에서는 `element.dataset.testValue`로 접근
-속성명 작성 시 주의사항
  - 대소문자 여부에 상관없이 xml로 시작하면 안 됨
  - 세미콜론을 포함해서는 안됨
  - 대문자를 포함해서는 안됨
<hr>

- AJAX로 csrftoken을 보내는 방법
- hidden 타입으로 숨겨져있는 csrf 값을 가진 input 태그를 선택해야 함
```html
<!-- accounts/profile.html -->
<script>
  const form = document.querySelector('#follow-form')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
</script>
```
```html
<!-- accounts/profile.html -->
<script>
  const form = document.querySelector('#follow-form')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  form.addEventListener('submit', function (event) {
    event.preventDefault()
    const userId = event.target.dataset.userId
    axios({
      method: 'post',
      url: `/accounts/${userId}/follow/`,
      headers: {'X-CSRFToken': csrftoken,}
    })
</script>
```

- 팔로우 여부를 확인하기 위한 is_followed 변수 작성 및 JSON 응답
```python
# accounts/views.py
from django.http import JsonResponse
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login
```
```html
view 함수에서 응답한 is_followed를 사용해 버튼 토글하기
팔로우 (follow)
<!-- accounts/profile.html -->
<script>
  ...
  axios({
    method: 'post', 
    url: `/accounts/${userId}/follow/`, 
    headers: {'X-CSRFToken': csrftoken,}
  })
    .then((response) => {
      const isFollowed = response.data.is_followed
      const followBtn = document.querySelector('#follow-form > input[type=submit]')
      if (isFollowed === true) {
        followBtn.value = '언팔로우'
      } else {
        followBtn.value = '팔로우'
      }
    })
</script>
```

- 팔로워 & 팔로잉 수 비동기 적용
- 해당 요소를 선택할 수 있도록 span 태그와 id 속성 작성
```html
<!-- accounts/profile.html -->
{% extends 'base.html' %}
{% block content %}
    <h1>{{ person.username }}님의 프로필</h1>
    <div>
        팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span> /
        팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span>
    </div>
```

- 직전에 작성한 span 태그를 각각 선택
```html
<!-- accounts/profile.html -->
<script>
  ...
    axios({
      method: 'post',
      url: `/accounts/${userId}/follow/`,
      headers: {'X-CSRFToken': csrftoken,}
    })
      .then((response) => {
        ...
        const followersCountTag = document.querySelector('#followers-count')
        const followingsCountTag = document.querySelector('#followings-count')
    })
</script>
```
- 팔로워, 팔로잉 인원 수 연산은 view 함수에서 진행하여 결과를 응답으로 전달
```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    ...
        context = {
            'is_followed': is_followed,
            'followers_count': you.followers.count(),
            'followings_count': you.followings.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', you.username)
return redirect('accounts:login')
```
- view 함수에서 응답한 연산 결과를 사용해 각 태그의 인원 수 값 변경하기
```html
<!-- accounts/profile.html -->

<script>
  ...
  axios({
    method: 'post',
    url: `/accounts/${userId}/follow/`,
    headers: {'X-CSRFToken': csrftoken,}
  })
    .then((response) => {
      ...
      const followersCountTag = document.querySelecto('#followers-count')
      const followingsCountTag = document.querySelector('#followings-count')
      followersCountTag.innerText = followersCount
      followingsCountTag.innerText = followingsCount
      })
</script>
```