$(".validate").on("click", function () {
  var {isValid, message} = valid() 
  if (!isValid) {
    Swal.fire({
      title: 'Error!',
      text:  message,
      icon: 'error',
      showCancelButton: true,
      showConfirmButton: false,
    });
    return false;
  }
  else {
    Swal.fire({
      title: 'Muy Bien!',
      text: 'Deseas enviar la nueva contraseña?',
      icon: 'success',
      confirmButtonText: 'Sí',
      showCancelButton: true,
    }).then((result) => {
      if (result.value) {
        $("#form").submit();
      }
      return false;

    });
    return false;
  }
});

function valid() {
  var message = ""
  var valid = true
  var validators =[
     [$("#password").val(),"la contraseña no es valida"],
     [!password.length < 8,"la contraseña debe tener un minimo de 8 digitos"],
     [/[A-Z]/.test(password),"la contraseña debe tener una Mayuscula"],
     [/[a-z]/.test(password),"la contraseña debe tener una minuscula"],
     [/\d/.test(password),"la contraseña debe tener una especial"],
     [/\W/.test(password),"la contraseña debe tener una especial"],
     [!password == "","la contraseña está vacia"],
     [$("#password").val() == $("#confirm").val(),"las contraseñas no coinciden"],
  ]

  validators.map((validator)=>{
    if (!validator[0]) {
      valid = false
      message = validator[1]
    }

  })


  return { valid, message };

}

$('input').attr('class', 'input');
