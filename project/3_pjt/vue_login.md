# 프로젝트 vue 로그인, 회원가입

## 로그인
- 로그인을 하기 위한 vue, 상태관리를 하기 위한 store(Vuex) 필요
### LoginView.vue
- form에 제출을 prevent 한 후 함수 실행
```vue
<template>
  <div class="row w-100">
    <div class="signup col-12 col-lg-6 d-flex align-items-center">
      <div class="login-box w-100">
        <h1 class="title login-title fw-bold my-5">Login</h1>
        <form
          class="w-100 d-flex flex-column align-items-center"
          @submit.prevent="handleSubmit()" >
          <div class="mb-3 w-100">
            <input
              type="email"
              class="form-control"
              id="email"
              aria-describedby="emailHelp"
              placeholder="E-mail"
              v-model="email"
            />
            <div id="emailHelp" class="form-text">
              We'll never share your email with anyone else.
            </div>
          </div>
          <div class="mb-3 w-100">
            <input
              type="password"
              class="form-control"
              id="password"
              placeholder="Password"
              v-model="password"
            />
          </div>
          <button type="submit" class="btn w-100 my-3 shadow btn-login">
            로그인
          </button>
          <p class="my-1">
            <a style="color: gray" :href="signupUrl">계정이 없으신가요?</a>
          </p>
        </form>
      </div>
    </div>
  </div>
</template>
```

```vue
- 로컬 스토리지에 access token과 refresh token 저장
- user 상태 변환
<script>
import axios from 'axios'
export default {
  data() {
    return {
      email: '',
      password: '',
      msg: '',
    }
  },
  methods: {
    async handleSubmit() {
      const response = await axios.post('login/', {
        email: this.email,
        password: this.password
      })
      localStorage.setItem('access_token', response.data.access_token)
      localStorage.setItem('refresh_token', response.data.refresh_token)
      this.$store.dispatch('user', response.data.user)
      this.$router.push('/')
    }
  }
}
</script>
```

### axios.py
- 베이스 URL 설정
```js
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/accounts/v1/'
```

### store/index.js
- vuex의 상태 관리
  - state -> actions -> mutations -> state 순서로 진행
- **getters**
  - 유저의 로그인 상태 정보 반환
- **mutations**
  - 로직을 동기적으로 정의
  - state 값을 변경하는 로직
- **actions**
  - 로직을 비동기적으로 정의
  - 상태가 변화하는 것을 추적
  - mutations의 메서드를 호출(commit)
```js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  user: null
}

const store = new Vuex.Store({
  state,
  getters: {
    user: (state) => {
      return state.user
    }
  },
  actions: {
    user(context, user) {
      context.commit('user', user)
    }
  },
  mutations: {
    user(state, user) {
      state.user = user
    }
  }
})

export default store
```

### components/NavBar.vue
```vue
<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <routerLink class="navbar-brand" to="/">Navbar</routerLink>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav" v-if="!user">
          <li class="nav-item">
            <routerLink class="nav-link" to="/login">로그인</routerLink>
          </li>
          <li class="nav-item">
            <routerLink class="nav-link" to="/signup">회원가입</routerLink>
          </li>
        </ul>
        <ul class="navbar-nav" v-if="user">
          <li class="nav-item">
            <a class="nav-link" href="javascript:void(0)" @click="handleClick"
              >로그아웃</a
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
```
- `{ mapGetters }`로 사용자의 로그인 상태를 가져온다.
```vue
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'NavBar',
  methods: {
    handleClick() {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      this.$store.dispatch('user', null)
      this.$router.push('/')
    }
  },
  computed: {
    ...mapGetters(['user'])
  }
}
</script>
```

## 회원가입
- form에 제출을 prevent 한 후 함수 실행
```vue
<template>
  <div class="signup container d-flex flex-column align-items-center">
    <h1 class="title fw-bold my-5">Signup</h1>
    <form
      class="w-50 d-flex flex-column align-items-center"
      @submit.prevent="submitForm"
    >
      <div class="mb-3 w-100">
        <input
          type="email"
          class="form-control"
          id="email"
          aria-describedby="emailHelp"
          placeholder="E-mail"
          v-model="email"
        />
        <div id="emailHelp" class="form-text">
          We'll never share your email with anyone else.
        </div>
      </div>
      <div class="mb-3 w-100">
        <input
          type="password"
          class="form-control"
          id="password1"
          placeholder="Password"
          v-model="password1"
        />
      </div>
      <div class="mb-3 w-100">
        <input
          type="password"
          class="form-control"
          id="password2"
          placeholder="Password Check"
          v-model="password2"
        />
      </div>
      <button type="submit" class="btn w-75 my-3 btn-signup">회원가입</button>
    </form>
  </div>
</template>
```
```vue
<script>
import { registerUser } from '@/api/index'

export default {
  data() {
    return {
      // form
      email: '',
      password1: '',
      password2: '',
      // log
      logMessage: ''
    }
  },
  methods: {
    async submitForm() {
      // API 요청시 전달할 userData 객체
      const userData = {
        email: this.email,
        password1: this.password1,
        password2: this.password2
      }
      const { data } = await registerUser(userData)

      this.logMessage = `${data.email} 님이 가입되었습니다.`

      // 가입 후 폼 초기화
      this.initForm()
    },
    initForm() {
      this.email = ''
      this.password1 = ''
      this.password2 = ''
    }
  }
}
</script>
```

### api/index.js
- 요청할 url, 요청할 때 보내줄 인자들 따로 파일로 관리
```js
import axios from 'axios'

function registerUser(userData) {
  // 요청할 URL
  const url = 'http://127.0.0.1:8000/api/accounts/v1/registration/'
  console.log('userData :', userData)
  return axios.post(url, userData, {
    'Content-Type': 'application/json'
  })
}
// 함수 export
export { registerUser }
```