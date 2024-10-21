// var numero = parseInt(prompt('Digite um número: '));
// // = atribuiçõa
// // == so o valor dentro
// // === verifica se o 0 é parecido identico
// if (numero % 2 === 0){
//     console.log(numero + 'É par.!!!');
// }
// // ReferenceError: prompt is not defined
// //     at Object.<anonymous> (C:\Users\EliandroSilva\Desktop\aulaGitFabrica\Python\Fabrica-de-software\Prof(a). Enilda.py\JavaScript\aula01\par.js:1:14)
// //     at Module._compile (node:internal/modules/cjs/loader:1256:14)
// //     at Module._extensions..js (node:internal/modules/cjs/loader:1310:10)
// //     at Module.load (node:internal/modules/cjs/loader:1119:32)
// //     at Module._load (node:internal/modules/cjs/loader:960:12)
// //     at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:81:12)
// //     at node:internal/main/run_main_module:23:47
const prompt = require("prompt-sync")();
var numero = parseInt(prompt('Digite um número: '));
if (numero % 2 === 0){
     console.log(numero,' É par.!!!');
}
else{
    console.log(numero+' É ompar...!!!');
}