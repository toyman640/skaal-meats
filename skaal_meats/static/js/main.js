(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner(0);
    
    
    // Initiate the wowjs
    new WOW().init();
    
    
   // Back to top button
   $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
        $('.back-to-top').fadeIn('slow');
    } else {
        $('.back-to-top').fadeOut('slow');
    }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Modal Video
    $(document).ready(function () {
        var $videoSrc;
        $('.btn-play').click(function () {
            $videoSrc = $(this).data("src");
        });
        console.log($videoSrc);

        $('#videoModal').on('shown.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0");
        })

        $('#videoModal').on('hide.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc);
        })
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Testimonial carousel
    $(".testimonial-carousel-1").owlCarousel({
        loop: true,
        dots: false,
        margin: 25,
        autoplay: true,
        slideTransition: 'linear',
        autoplayTimeout: 0,
        autoplaySpeed: 10000,
        autoplayHoverPause: false,
        responsive: {
            0:{
                items:1
            },
            575:{
                items:1
            },
            767:{
                items:2
            },
            991:{
                items:3
            }
        }
    });

    $(".testimonial-carousel-2").owlCarousel({
        loop: true,
        dots: false,
        rtl: true,
        margin: 25,
        autoplay: true,
        slideTransition: 'linear',
        autoplayTimeout: 0,
        autoplaySpeed: 10000,
        autoplayHoverPause: false,
        responsive: {
            0:{
                items:1
            },
            575:{
                items:1
            },
            767:{
                items:2
            },
            991:{
                items:3
            }
        }
    });
    $(".owl-carousel").owlCarousel({
        items: 1,
        loop: true,
        autoplay: true,
        autoplayTimeout: 4000,
        smartSpeed: 1000,
        animateOut: 'fadeOut'
    });
})(jQuery);

var clientHeight = document.getElementById('myDiv').clientHeight;
console.log(clientHeight);

// $(document).ready(function(){
//     $(".owl-carousel").owlCarousel({
//       loop: true,
//       margin: 10,
//       nav: true,
//       items: 1
//     });
// });

// document.addEventListener("DOMContentLoaded", () => {
//   const col8 = document.querySelector(".col8-content");
//   const col4 = document.querySelector(".col4-content");
//   alert("hello");

//   const col8Height = col8.scrollHeight;
//   const col4Height = col4.scrollHeight;
//   const heightDiff = col8Height - col4Height;

//   window.addEventListener("scroll", () => {
//     const col8Top = col8.getBoundingClientRect().top;
//     const col8Bottom = col8.getBoundingClientRect().bottom;

//     // Freeze col-4 when its content finishes
//     if (col8Top <= 0 && col8Bottom > window.innerHeight) {
//       if (-col8Top >= heightDiff) {
//         col4.style.position = "fixed";
//         col4.style.top = `${-heightDiff}px`;
//       } else {
//         col4.style.position = "fixed";
//         col4.style.top = "0";
//       }
//     } else {
//       col4.style.position = "static";
//     }
//   });
// });
