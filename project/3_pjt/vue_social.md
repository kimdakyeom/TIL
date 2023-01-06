# 프로젝트 vue 소셜로그인
> 클라이언트에서 소셜로그인을 진행할 때 바로 구글로 리다이렉트되는 서버로 요청을 보내면 에러가 난다. 구글에서 axios 요청을 막아놔서 해당 에러가 나는 것이다.

- 해결 방법
  - 클라이언트단에서 바로 구글 로그인 api로 연결을 한다. 그러면 응답이 url 주소로 넘어오는데 이 주소를 구글 로그인 로직이 있는 서버단으로 요청을 보낸다. access token을 응답으로 받아온 후 이를 local storage에 저장하여 로그인 로직을 수행한다.
```vue
<!-- component -->
<template>
  <a :href="GOOGLE_AUTH_URL">Google Login</a>
</template>

<script>
  const BASE_URL = 'http://localhost:8080/'
  const GOOGLE_CALLBACK_URI = BASE_URL + 'google/callback/'
  const SOCIAL_AUTH_GOOGLE_CLIENT_ID = '409441996370-7iii74jatbk3hkgnortm3ol157oq9k4f.apps.googleusercontent.com'
  const scope = "https://www.googleapis.com/auth/userinfo.email"

  export default {
  data() {
    return {
      GOOGLE_AUTH_URL: `https://accounts.google.com/o/oauth2/v2/auth?client_id=${SOCIAL_AUTH_GOOGLE_CLIENT_ID}&response_type=code&redirect_uri=${GOOGLE_CALLBACK_URI}&scope=${scope}`
    }
  }
}
</script>
```
```vue
<!-- views -->
<script>
import axios from 'axios'

export default {
  created() {
    const code = this.$route.query.code
    console.log(code)
    axios.get(`https://pjtpjt.tk/api/accounts/v1/google/callback/?code=${code}`)
    .then(res => {
        localStorage.setItem('access_token', res.data.access_token)
        localStorage.setItem('refresh_token', res.data.refresh_token)
        this.$store.dispatch('user', response.data.user)
      })
  }
}
</script>
```

## 후기
drf와 vue를 사용하지 않았을 때는 axios 요청을 하지 않았으므로 구글에서 axios 요청을 막아둔지 몰랐다. 그래서 클라이언트단에서 바로 구글로 요청을 보냈는데 생각보다 클라이언트단에서 처리해야하는 부분이 많았다. vue에는 익숙치 않은 부분이 많아서 구현하는데 시간이 걸렸다. 뷰->구글->서버단->구글->서버단->뷰 형태로 응답을 주고받으면서 요청과 응답의 개념을 확실히 잡을 수 있었다.