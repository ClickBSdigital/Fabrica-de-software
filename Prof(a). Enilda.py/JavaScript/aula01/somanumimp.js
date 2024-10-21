// Ler 10 números e exibir a soma dos números ímpares. 
// tem que por essa constante (const prompt = require("prompt-sync")();), para que o código funcione ... 
const prompt = require("prompt-sync")();
let somaImpares = 0;

for (let i = 1; i <= 10; i++) {
  let numero = parseInt(prompt(`Digite o número ${i}: `));

  if (numero % 2 !== 0) { // Verifica se o número é ímpar
    somaImpares += numero;
  }
}

console.log("A soma dos números ímpares digitados é: " + somaImpares);
