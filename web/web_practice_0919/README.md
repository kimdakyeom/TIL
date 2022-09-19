# 0919 js 실습
- `02_input.html` input에 작성된 내용을 그대로 출력하기
- `04_modal.html` 모달 직접 만들어보기
- `05_carousel.html` 이전(previous) 버튼 만들기
- 비밀번호 및 비밀번호 일치 여부 확인하기
    - 조건
        - 비밀번호는 8자리 이상이어야 합니다.
        - 비밀번호는 비밀번호와 비밀번호 확인 값이 일치해야 합니다.
    - 일치하지 않는 경우 `alert` 를 통해 메시지를 전달합니다.
```html
<form action="">
  <input type="password" name="password" id="password">
  <input type="password" name="password_confirmation" id="password_confirmation">
</form>
```