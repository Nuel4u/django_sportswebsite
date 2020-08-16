const responsive ={
    0:{
        items:1
    },
    240:{
        items :1
    },
    320:{
        items:2
    },
    520:{
        items :3
    },
    
    
}

$(document).ready(function (){
    $nav =$('.nav');
    $toggleCollapse = $('.toggle-collapse');

    /** click event on toggle menu */
    $toggleCollapse.click(function(){
        $nav.toggleClass('collapse');

    })
    // owl carousel for blog
    $('.owl-carousel').owlCarousel({
        loop :true,
        autoplay:false,
       autoplayTimeout:3000,
        dots:false,
        nav:true,
        navText:[$('.owl-navigation .owl-nav-prev'), $('.owl-navigation .owl-nav-next')],
        responsive: responsive
    });

    //click to scroll up

    $('.move-up span').click(function(){
        $('html,body').animate({
            scrollTop:0
        },3000)
    })
    //AOS Instance
    AOS.init();
})