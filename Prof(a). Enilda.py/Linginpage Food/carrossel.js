var radio = document.querySelector('.manual-btn')
var cont = 1

document.getElementById('radio1').checked = true

setInterval(() => {
    proximaImagem()
}, 5000)

function proximaImagem(){
    cont++
    if(cont>3){
        cont = 1
    }
    document.getElementById('radio'+cont).checked = true
}