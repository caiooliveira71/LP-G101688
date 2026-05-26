// Função que ira executar quando clicar no botao btnGerar.

function gerarTabuada() {
    // Pega o valor do campo input Html
    const numeroInput = document.getElementById('numeroInput')
    let numero = parseInt(numeroInput.value)

    // Pega o elemento onde a tabuada sera exibida.
    const resultadoDiv = document.getElementById('resultadoTabuada')

    // Limpar o conteudo anterior.
    resultadoDiv.innerHTML = ''

    // Adiciona um titulo para a tabuada.
    resultadoDiv.innerHTML += `<h2>Tabuada do numero ${numero}: <h2>`

    // Laço de repetição para gerar tabuada de 1 ate 10.
    for (let i = 1; i <= 10; i++) {
        let resultado = numero * i
        resultadoDiv.innerHTML += `<p>${numero} x ${i} = ${resultado}<p>`
    }
}

// Faz a função gerartabuada() ser executada quando clicar no botão.
const btnGerar = document.getElementById('btnGerar')
btnGerar.addEventListener('click', gerarTabuada)