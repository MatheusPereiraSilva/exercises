let inputHomens = document.getElementById("homens");

let inputCriancas = document.getElementById("criancas");
let inputDuracao = document.getElementById("duracao");

let resultado = document.getElementById("resultado");

function calcular() {
  console.log("calculando....");

  let homens = inputHomens.value;

  let criancas = inputCriancas.value;
  let duracao = inputDuracao.value;

  let qdtTotalCarne =
    carnePP(duracao) * homens + (carnePP(duracao) / 2) * criancas;
  let qdtTotalCerveja = cervejaPP(duracao) * homens;
  let qdtTotalBebida =
    bebidaPP(duracao) * homens + (bebidaPP(duracao) / 2) * criancas;

  resultado.innerHTML = `<p>${parseInt(qdtTotalCarne / 1000)} Kg de Carne</p>`;
  resultado.innerHTML += `<p>${Math.ceil(
    parseInt(qdtTotalCerveja / 355)
  )} Latas de Cerveja</p>`;
  resultado.innerHTML += `<p>${Math.ceil(
    parseInt(qdtTotalBebida / 2000)
  )} Garrafas de Bebidas</p>`;
}

function carnePP(duracao) {
  if (duracao >= 6) {
    return 650;
  } else {
    return 400;
  }
}
function cervejaPP(duracao) {
  if (duracao >= 6) {
    return 2000;
  } else {
    return 1200;
  }
}
function bebidaPP(duracao) {
  if (duracao >= 6) {
    return 1500;
  } else {
    return 1000;
  }
}