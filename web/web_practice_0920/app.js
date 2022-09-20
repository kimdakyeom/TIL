function asdf() {
	document.getElementById("qwerty").innerHTML="<br>"
}

const comboBox = document.querySelector('#combo-box') // 콤보박스 선택
const button = document.querySelector('#lotto-btn') // 버튼 선택

button.addEventListener('click', function() { // 버튼을 누르면
console.log(comboBox.value *= 1)
const iter = comboBox.value *= 1

const ballContainer = document.createElement('div') // ballContainer라는 div 생성
ballContainer.classList.add('ball-container') // ballContainer에 ball-container 클래스 추가
const numbers = _.sampleSize(_.range(1, 46), 6) // 1~45 숫자 중 6개 뽑기

for (let i = 0; i < iter; i++) {

	for (let b of numbers) {
			const ball = document.createElement('div') // ball 넣을 div 만들기
			ball.classList.add('ball')
			ball.innerText = b // ball에 number 넣기

			if (b < 10) {
				ball.style.backgroundColor = 'yello'
			}
			else if (b < 20) {
				ball.style.backgroundColor = 'blue'
				ball.style.color = 'white'
			}
			else if (b < 30) {
				ball.style.backgroundColor = 'red'
			}
			else if (b < 40) {
				ball.style.backgroundColor = 'black'
				ball.style.color = 'white'
			}
			else if (b < 46) {
				ball.style.backgroundColor = 'green'
				ball.style.color = 'white'
			}

			ballContainer.appendChild(ball)
			const result = document.querySelector('#result')
		}
		result.innerHTML = ""
		result.appendChild(ballContainer)
		asdf()
		if(i == iter){break;}
	}
})