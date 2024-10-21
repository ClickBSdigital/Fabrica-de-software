// Ler 30 números e exibir a soma dos números que são divisíveis por 5. 
// tem que por essa constante (const prompt = require("prompt-sync")();), para que o código funcione ... 
const prompt = require("prompt-sync")();
let somaDivisiveisPor5 = 0;

for (let i = 1; i <= 30; i++) {
  let numero = parseInt(prompt(`Digite o número ${i}: `));

  if (numero % 5 === 0) { // Verifica se o número é divisível por 5
    somaDivisiveisPor5 += numero;
  }
}

console.log("A soma dos números divisíveis por 5 é: " + somaDivisiveisPor5);
