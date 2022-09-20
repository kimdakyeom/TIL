const form = document.querySelector('#form')
const password = document.querySelector('#password')
const password_confirmation = document.querySelector('#password_confirmation')

form.addEventListener('submit', function(event) {
  event.preventDefault()
  const formData = new FormData(form)
  console.log(formData)
  console.log(formData.get('password'))
  console.log(formData.get('password_confirmation'))

  if(formData.get('password') != formData.get('password_confirmation')) {
    alert("비밀번호를 확인해주세요")
    password.value = null
    password_confirmation.value = null
  }
  else if(formData.get('password') === formData.get('password_confirmation')) {
    alert("제출되었습니다")
    password.value = null
    password_confirmation.value = null
  }
})