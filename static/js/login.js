const username = document.getElementById('id_username')
const password = document.getElementById('id_password')

function style(inputs=[]) {
  inputs.forEach((input) => {
  	input.classList.add('form-control')
  })
}

style([username, password])