# Django 소셜 로그인 02
> 전 날엔 장고에 내장되어있는 allauth 익스텐션을 썼다. 중간에 써드파티 화면이 나오는걸 원하지 않았고, 회원을 User 모델에서 다루고 싶어서 javascript로 AJAX를 이용해 소셜 로그인을 구현해봤다.

## 카카오 소셜 로그인
- 로그인 한 후 DB에 저장하고, 로컬 서버에서 로그인을 처리할 함수 url 생성
```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('id_check/', views.id_check, name='id_check'),
]
```
- kakao api와 통신한 후 로그인 내용을 AJAX를 이용해 서버단에 넘겨준다.
```html
<!-- accounts/login.html -->

<a id="kakao-login-btn"></a>
<div id="result"></div>

<script type="text/javascript">
  function unlinkApp() {
    Kakao.API.request({
      url: '/v1/user/unlink',
      success: function(res) {
        alert('success: ' + JSON.stringify(res))
      },
      fail: function(err) {
        alert('fail: ' + JSON.stringify(err))
      },
    })
  }
</script>
<script src="https://developers.kakao.com/sdk/js/kakao.js"></script>
<script type="text/javascript">
  Kakao.init('kakao developer에서 발급받은 javascript 키 값을 넣어주세요');
  console.log(Kakao.isInitialized());
   
  Kakao.Auth.createLoginButton({
    container: '#kakao-login-btn',
    success: function(authObj) {
      Kakao.API.request({
        url: '/v2/user/me',
        success: function(result) {
          $('#result').append(result);
          id = result.id
          connected_at = result.connected_at
          kakao_account = result.kakao_account
          console.log(kakao_account)
          $('#result').append(kakao_account);

          resultdiv="<h2>로그인 성공 !!"
          resultdiv += '<h4>id: '+id+'<h4>'
          resultdiv += '<h4>connected_at: '+connected_at+'<h4>'
          profile_image = "";
          email ="";
          gender = "";
          if(typeof kakao_account != 'undefined'){
            email = kakao_account.email;
            profile_image = kakao_account.profile.thumbnail_image_url;
        	  gender = kakao_account.gender;
          }
          resultdiv += '<h4>email: '+email+'<h4>'
          resultdiv += '<h4>profile_image: '+profile_image+'<h4>'
          resultdiv += '<h4>gender: '+gender+'<h4>'
          $('#result').append(resultdiv);
          const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
          axios({
            method: 'post',
            url: `/accounts/id_check/`,
            headers: {'X-CSRFToken': csrftoken},
            data: {'username': id, 'email': email, 'profile_image': profile_image,}
            }).then(response => {
              
            })
        },
        fail: function(error) {
          alert(
            'login success, but failed to request user information: ' +
              JSON.stringify(error)
          )
        },
      })
    },
    fail: function(err) {
      alert('failed to login: ' + JSON.stringify(err))
    },
  })
</script>
```
- id 앞에 'k'을 붙혀서 네이버 로그인 회원을 구분
- 회원가입이 되어있는 회원이면 로그인, 안되어 있는 회원이면 회원 DB에 AJAX로 받아온 내용들을 넣어준 후 로그인 구현
```python
# accounts/views.py

import json
from django.http import JsonResponse
from .models import User
from django.contrib.auth import login as auth_login

def id_check(request):
    jsonObject = json.loads(request.body)
    # user = User()
    username = jsonObject.get('username')
    username = "k" + str(username)
    print(username)
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
    else:
        email = jsonObject.get('email')
        profile_image = jsonObject.get('profile_image')
        user = User.objects.create(username=username, email=email, profile_image=profile_image)
        user.save()
    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return JsonResponse({'username': user.username, 'email': user.email, 'profile_image':user.profile_image.url })
```

## 네이버 소셜 로그인
- 로그인 한 후 DB에 저장하고, 로컬 서버에서 로그인을 처리할 함수 url 생성
```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('id_check_naver/', views.id_check_naver, name='id_check_naver'),
]
```
- naver api 설정
```html
<!-- accounts/login.html -->

<a id="naverIdLogin_loginButton" href="javascript:void(0)" class="text-decoration-none">네이버 로그인</a>

<script src="https://static.nid.naver.com/js/naveridlogin_js_sdk_2.0.2.js" charset="utf-8"></script>
<script>
var naverLogin = new naver.LoginWithNaverId(
{
    clientId: "내 애플리케이션 정보에 cliendId",
    callbackUrl: "내 애플리케이션 API설정의 Callback URL",
    isPopup: false,
    callbackHandle: true,
}
);	

naverLogin.init();

window.addEventListener('load', function () {
naverLogin.getLoginStatus(function (status) {
if (status) {
    var email = naverLogin.user.getEmail(); // 필수로 설정할 값
    
    console.log(naverLogin.user); 
    
    if( email == undefined || email == null) {
        alert("이메일은 필수정보입니다. 정보제공을 동의해주세요.");
        naverLogin.reprompt();
        return;
        }
} else {
    console.log("callback 처리에 실패하였습니다.");
}
});
});


var testPopUp;
function openPopUp() {
    testPopUp= window.open("https://nid.naver.com/nidlogin.logout", "_blank", "toolbar=yes,scrollbars=yes,resizable=yes,width=1,height=1");
}
function closePopUp(){
    testPopUp.close();
}

function naverLogout() {
    openPopUp();
    setTimeout(function() {
    closePopUp();
}, 1000);


}
</script>
```
- 네이버 소셜 로그인은 콜백 페이지가 필요하다.
- 로그인을 완료한 후, 로그인 내용을 AJAX를 이용해 서버단에 넘겨준다.
```html
<!-- accounts/naver_callback.html -->
<script type="text/javascript" src="https://static.nid.naver.com/js/naverLogin_implicit-1.0.3.js" charset="utf-8"></script>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
<script src="https://static.nid.naver.com/js/naveridlogin_js_sdk_2.0.2.js" charset="utf-8"></script>
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script type="text/javascript">
  var naver_id_login = new naver_id_login("hgD9ymV7P0RHFNuOlyZD", "http://127.0.0.1:8000/accounts/naver_callback/");
  // 접근 토큰 값 출력
  $('body').append('<h4>접속토큰:'+naver_id_login.oauthParams.access_token+'</h4>');
  // 네이버 사용자 프로필 조회
  naver_id_login.get_naver_userprofile("naverSignInCallback()");
  // 네이버 사용자 프로필 조회 이후 프로필 정보를 처리할 callback function
  function naverSignInCallback() {
    const id = naver_id_login.getProfileData('id');
    const email = naver_id_login.getProfileData('email');
    const nickname = naver_id_login.getProfileData('nickname');
    const name = naver_id_login.getProfileData('name');
    const profile_image = naver_id_login.getProfileData('profile_image');
    const gender = naver_id_login.getProfileData('gender');
    const birthday = naver_id_login.getProfileData('birthday');
    const mobile = naver_id_login.getProfileData('mobile');
    
	let body = $('body');
	body.append('로그인 성공!');
    body.append(profile_image);
    axios({
        method: 'post',
        url: `/accounts/id_check_naver/`,
        headers : {'X-CSRFTOKEN' : '{{ csrf_token }}'},
        data: {'id': id, 'name': name, 'email': email, 'profile_image': profile_image,}
        }).then(response => {
        // location.reload();
        window.close()
        })
    }
</script>
```
- id 앞에 'n'을 붙혀서 네이버 로그인 회원을 구분
- 회원가입이 되어있는 회원이면 로그인, 안되어 있는 회원이면 회원 DB에 AJAX로 받아온 내용들을 넣어준 후 로그인 구현
```python
# accounts/views.py
def id_check_naver(request):
    jsonObject = json.loads(request.body)
    # user = User()
    username = jsonObject.get('id')
    username = "n" + str(username)
    print(username)
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
    else:
        email = jsonObject.get('email')
        profile_image = jsonObject.get('profile_image')
        user = User.objects.create(username=username, email=email, profile_image=profile_image)
        user.save()
    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return JsonResponse({'username': user.username, 'email': user.email})
```

## 구현하며 어려웠던 부분
소셜 로그인 개발 공식 문서나 다른 블로그를 참고했지만 javascript로 해당 서버에서의 로그인하는 방법만 나왔다.

로그인 내용들을 user DB에 저장하고, 로컬 서버에서도 로그인이 되게하는 로직을 짜는데에 시간이 조금 걸렸다.

서버단에서의 처리를 구현되어있는 코드를 보고 처리한 것이 아니라 직접 로직을 생각하고 구현을 하면서 AXIOS를 이용한 AJAX 비동기 통신이 어떻게 진행되는지 헷갈렸던 부분이 완전히 이해가 되었다.