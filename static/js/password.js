const old_password = document.getElementById('id_old_password')
const new_password = document.getElementById('id_new_password1')
const new_password_1 = document.getElementById('id_new_password2')

function style(inputs=[]) {
  inputs.forEach((input) => {
  	input.classList.add('form-control')
  })
}

style([old_password, new_password, new_password_1])