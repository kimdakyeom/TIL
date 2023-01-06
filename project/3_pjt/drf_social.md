# 프로젝트 drf rest-auth로 소셜로그인
[애플리케이션 등록 보고오기](https://github.com/kimdakyeom/TIL/blob/master/project/1_alcohol_trip/social_login.md)

## settings.py
```python
INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth'
    ...,
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    ...,
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
)

SITE_ID = 6
```

## accounts/views.py
- google_login : google 로그인 api로 리다이렉트 되어 로그인을 수행한다.
- google_callback : 로그인 후 callback을 클라이언트단으로 한다. 이때 url에 클라이언트에 해당하는 code를 받아온 후 이를 활용해서 oauth로 로그인 요청을 보낸다. 이후 발급받은 acess token을 가지고 유저 db에 저장 후 회원가입을 진행하거나 로그인을 진행한다.
```python
state = os.getenv("STATE")
BASE_URL = 'https://pjtpjt.tk/'
GOOGLE_CALLBACK_URI = BASE_URL + 'api/accounts/v1/google/callback/'
def google_login(request):
    """
    Code Request
    """
    scope = "https://www.googleapis.com/auth/userinfo.email"
    client_id =  os.getenv("SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")
def google_callback(request):
    client_id =  os.getenv("SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    client_secret = os.getenv("SOCIAL_AUTH_GOOGLE_SECRET")
    code = request.GET.get('code')
    GOOGLE_CALLBACK_URI_FRONT = "https://pjt.vercel.app/google/callback/"
    """
    Access Token Request
    """
    token_req = requests.post(
        f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI_FRONT}&state={state}")
    token_req_json = token_req.json()
    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_req_json.get('access_token')
    """
    Email Request
    """
    email_req = requests.get(
        f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")
    email_req_status = email_req.status_code
    if email_req_status != 200:
        return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)
    email_req_json = email_req.json()
    email = email_req_json.get('email')
    """
    Signup or Signin Request
    """
    try:
        user = User.objects.get(email=email)
        # 기존에 가입된 유저의 Provider가 google이 아니면 에러 발생, 맞으면 로그인
        # 다른 SNS로 가입된 유저
        social_user = SocialAccount.objects.get(user=user)
        if social_user is None:
            return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)
        if social_user.provider != 'google':
            return JsonResponse({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)
        # 기존에 Google로 가입된 유저
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"{BASE_URL}api/accounts/v1/google/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)
    except User.DoesNotExist:
        # 기존에 가입된 유저가 없으면 새로 가입
        data = {'access_token': access_token, 'code': code}
        print(data)
        accept = requests.post(
            f"{BASE_URL}api/accounts/v1/google/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)
class GoogleLogin(SocialLoginView):
    adapter_class = google_view.GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client
```

## accounts/urls.py
```python
from django.urls import path, include
from .views import *

app_name = "accounts"
urlpatterns = [
    path('google/login/', views.google_login, name='google_login'),
    path('google/callback/', views.google_callback, name='google_callback'),
    path('google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),
]
```

## 힘들었던 부분
- 구글 소셜 로그인에 자꾸 리다이렉트 에러가 났다. admain 페이지에 들어가려고 했더니 Site matching query does not exist. 가 났다. DB를 삭제하고 aullauth랑 연동? 하면서 Django가 DB에 갖고 있던 사이트 정보가 사라진 것이 원인이이었다.

![](./drf_social_login.assets/error_solve0.PNG)
- shell 작업을 통해 Site 객체를 다시 DB에 입력했다.

![](./drf_social_login.assets/error_solve.PNG)
- site_id를 확인하고 해당 번호로 변경하니 구글 소셜 로그인까지 잘 됐다.
## REFERENCE
[django-rest-auth](https://django-rest-auth.readthedocs.io/en/latest/installation.html#social-authentication-optional)