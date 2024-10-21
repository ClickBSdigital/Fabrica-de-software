// Ler 10 números e exibir o maior número
// tem que por essa constante (const prompt = require("prompt-sync")();), para que o código funcione ... 
const prompt = require("prompt-sync")();
var limite = parseInt(prompt("digite um numero"));
for (var i = 2; i <= limite; i += 2){
    console.log(i);
}



// Esse código é um exemplo em JavaScript que solicita ao usuário que digite um número e, em seguida, imprime todos os números pares a partir de 2 até o número fornecido. Vamos quebrar isso em partes:

// var limite = prompt("digite um numero");: Aqui, o programa exibe uma caixa de diálogo pedindo ao usuário que digite um número. O valor digitado é armazenado na variável limite. Note que o valor retornado pelo prompt é uma string.

// for (var i = 2; i <= limite; i += 2){: Este é um loop for que inicia com i igual a 2. O loop continuará enquanto i for menor ou igual a limite, e a cada iteração, i será incrementado em 2. Isso significa que o loop vai gerar apenas números pares.

// console.log(i);: Dentro do loop, console.log(i) imprime o valor atual de i no console.

// Funcionamento
// Se o usuário, por exemplo, digitar 10, o código imprimirá:

// Copiar código
// 2
// 4
// 6
// 8
// 10
// Observação
// Para que a comparação funcione corretamente, é importante lembrar que limite deve ser convertido para um número, já que prompt retorna uma string. Para isso, você pode usar parseInt ou Number, como abaixo:

// javascript
// Copiar código
// var limite = parseInt(prompt("digite um numero"));
// Assim, o código ficaria mais robusto ao lidar com a entrada do usuário.

// ==============================================

// Para ler 10 números e exibir o maior deles em JavaScript, podemos usar um loop forpara capturar cada número e comparar para encontrar o maior. Aqui está um exemplo de como fazer isso:

// Javascript-escritor

// Copiar código
// let maiorNumero = -Infinity; // Inicializa com o menor valor possível

// for (let i = 1; i <= 10; i++) {
//   let numero = parseFloat(prompt(`Digite o número ${i}:`));

//   if (numero > maiorNumero) {
//     maiorNumero = numero;
//   }
// }

// console.log("O maior número digitado foi: " + maiorNumero);
// Neste código:

// maiorNumeroé inicializado com -Infinitypara garantir que qualquer número digitado será maior que ele.
// O loop foritera 10 vezes, solicitando ao usuário que insira um número em cada reprodução.
// A função promptcaptura o número inserido e parseFloatconverte-o para um número decimal.
// Em cada iteração, verifique se o número atual é maior que maiorNumero; se for, maiorNumeroé atualizado.
// Ao final, o maior número é exibido no console.