const button = document.querySelector('#input-btn')
const input = document.querySelector('#input')
const result = document.querySelector('#result')
const num = document.createElement('div')

button.addEventListener('click', function() {
  num.innerText = input.value
  result.append(num)
  input.value = null
})