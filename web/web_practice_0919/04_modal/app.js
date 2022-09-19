const open = function(e) {
    document.querySelector('#modal-content').classList.remove('hidden')
  }

const close = function(e) {
  document.querySelector('#modal-content').classList.add('hidden')
}

const modalBtn = document.querySelector('#modal-btn')
modalBtn.addEventListener('click', open)

const modalCancelBtn = document.querySelector('#modal-cancel-btn')
modalCancelBtn.addEventListener('click', close)

const modalOverlay = document.querySelector('#modal-content')
modalOverlay.addEventListener('click', close)