// Validação do formulário de verificação
document.getElementById("verification-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o envio do formulário

    // Verifique se o formulário está válido
    if (this.checkValidity()) {
        alert("A referência Multibanco será enviada por email para finalizar a compra.");
    } else {
        alert("Por favor, preencha corretamente todos os campos.");
    }
});