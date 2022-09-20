const h1 = document.querySelector('h1')

h1.addEventListener('copy', function(event) {
  event.preventDefault()
  alert("삐빅 복사를 할 수 없습니다")
})

h1.addEventListener('click', function(event) {
  event.preventDefault()
  if (event.button === 0) {
    alert("마우스 사용 금지")
  }
})