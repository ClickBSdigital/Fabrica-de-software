// const btn = document.querySelector(".active");
// btn.addEventListener("click",())

$(document).ready(function(){
    // $ = biblioteca em js por meio da DOM que e´a hierarquia
    $('.mobile-btn').on('click',function(){
        $('.mobile-menu').toggleClass('active');
        $('.mobile-btn').find('i').toggleClass('fa-x')
    })
})

// alert('foi') = uma maneira de ver se o js esta sendo chamando no flont