$(document).ready(function () {
    $('#pop-button').click(function () {
        $('.pop').css('transition', '0s')
        $('.pop').css('opacity', '0%')
        $('.pop').css('z-index', '0')

        $('.front').css('transform', 'rotateY(180deg)')
        $('.back').css('transform', 'rotateY(360deg)')
    })

    /*Dropdown Menu*/
    $('.dropdown').click(function () {
        $(this).attr('tabindex', 1).focus();
        $(this).toggleClass('active');
        $(this).find('.dropdown-menu').slideToggle(300);
    });
    $('.dropdown').focusout(function () {
        $(this).removeClass('active');
        $(this).find('.dropdown-menu').slideUp(300);
    });
    $('.dropdown .dropdown-menu li').click(function () {
        $(this).parents('.dropdown').find('span').text($(this).text());
        $(this).parents('.dropdown').find('input').attr('value', $(this).attr('id'));
    });
    /*End Dropdown Menu*/

    let menuBtn = document.querySelector('.menu-btn');
    let menu = document.querySelector('.menu');
    menuBtn.addEventListener('click', function () {

        menuBtn.classList.toggle('active');
        menu.classList.toggle('active');
    })
});


