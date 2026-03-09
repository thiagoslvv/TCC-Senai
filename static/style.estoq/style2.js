window.onload = function () {
    // Puxa o id do estoque e as colunas
    let linhas = document.querySelectorAll("#estoque tr");
    // Por onde começar na coluna
    for (let i = 1; i < linhas.length; i++) {
        let quantidade = parseInt(linhas[i].children[1].innerText);
    // Pega o numero da coluna quantidade para verificar se e menor que 5
    if (quantidade < 5) {
            linhas[i].classList.add("estoque-baixo");
    // Se for menor que 5 puxa a classe do css
        }
    }
};