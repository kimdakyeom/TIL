const nextBtn = document.querySelector('#nextBtn')
const preBtn = document.querySelector('#preBtn')

nextBtn.addEventListener('click', function() {
  const currentElement = document.querySelector('.active')
  const items = document.querySelectorAll('.carousel-item')
  const idx = [...items].indexOf(currentElement)
  console.log(currentElement, items, idx)
  currentElement.classList.toggle('active')
  items[(idx+1)%items.length].classList.toggle('active')
})

preBtn.addEventListener('click', function() {
  const currentElement = document.querySelector('.active')
  const items = document.querySelectorAll('.carousel-item')
  const idx = [...items].indexOf(currentElement)
  console.log(currentElement, items, idx)
  currentElement.classList.toggle('active')
  items[(items.length+idx-1)%items.length].classList.toggle('active')
})