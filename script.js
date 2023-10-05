// Função para calcular a potência parcial do secundário com base em tensão e corrente
function calcularPotenciaParcial(tensao, corrente) {
    return tensao * corrente;
}

// Função para calcular a potência total do secundário
function calcularPotenciaTotalSecundario() {
    // Seleciona todos os elementos de classe "tensao" e "corrente"
    const tensoes = document.querySelectorAll(".tensao");
    const correntes = document.querySelectorAll(".corrente");

    let potenciaTotalSecundario = 0;

    // Itera sobre os elementos e calcula as potências parciais
    for (let i = 0; i < tensoes.length; i++) {
        const tensao = parseFloat(tensoes[i].value);
        const corrente = parseFloat(correntes[i].value);

        // Verifica se os valores inseridos são números válidos
        if (!isNaN(tensao) && !isNaN(corrente)) {
            const potenciaParcial = calcularPotenciaParcial(tensao, corrente);
            potenciaTotalSecundario += potenciaParcial;
        }
    }

    return potenciaTotalSecundario;
}

function calcularSeccaoNucleo(F, Pw) {
  // Fator de segurança (1.1) para garantir eficiência do transformador
  const fatorSeguranca = 1.1;
  
  // Cálculo da seção transversal mínima do núcleo (Sg)
  const Sg = fatorSeguranca * (7.5 * Math.sqrt(Pw) / F);
  
  return Sg;
}


// Função para calcular a potência do primário
function calcularPotenciaPrimario(potenciaTotalSecundario) {
    return potenciaTotalSecundario * 1.1;
}

// Função principal que recebe os dados do HTML e escreve os resultados no HTML
function calcularEExibirPotencias() {
    const potenciaTotalSecundario = calcularPotenciaTotalSecundario();
    const potenciaPrimario = calcularPotenciaPrimario(potenciaTotalSecundario);

    // Exibe o resultado da potência total do secundário na página HTML
    const resultadoSpan = document.getElementById("resultado");
    resultadoSpan.textContent = potenciaTotalSecundario.toFixed(2) + " Watts";

    // Exibe o resultado da potência do primário na página HTML
    const potenciaPrimarioSpan = document.getElementById("potencia-primario");
    potenciaPrimarioSpan.textContent = potenciaPrimario.toFixed(2) + " Watts";
}

// Adiciona um ouvinte de evento para o botão "Calcular Potência"
const calcularButton = document.querySelector("button");
calcularButton.addEventListener("click", calcularEExibirPotencias);
