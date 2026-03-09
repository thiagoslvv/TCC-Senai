function but(){

// Alerta de item cadastrado e não cadastrado

Swal.fire({
  title: "Você quer Cadastrar este item?",
  showDenyButton: true, 
  confirmButtonText: "Sim",
  denyButtonText: `Não`
}).then((result) => {
  if (result.isConfirmed) {
    Swal.fire("Cadastrado", "", "success");
  } else if (result.isDenied) {
    Swal.fire("Não Cadastrado", "", "error");
  }
});
}