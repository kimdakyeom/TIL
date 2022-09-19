let countNumber = 0

const plusBtn = document.querySelector('#plus-btn')
const initBtn = document.querySelector('#init-btn')

plusBtn.addEventListener('click', function() {
    console.log('click')
    countNumber += 1

    const counter = document.querySelector('#counter')
    counter.innerText = countNumber
})

initBtn.addEventListener('click', function() {
    console.log('click')
    countNumber = 0

    const counter = document.querySelector('#counter')
    counter.innerText = countNumber
})