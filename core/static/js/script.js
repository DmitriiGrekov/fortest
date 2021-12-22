
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

    $('.auth_form').on('submit', function (e) {
        e.preventDefault()
        username = $('#auth_login').val()
        password = $('#auth_password').val()
        csrf = $('#modal_auth > div > div > div.modal-body > form > input[type=hidden]').val()
        data = {
            'username': username,
            'password': password,
            "csrfmiddlewaretoken": csrf
        }


        $.post('/accounts/login/', data, function (data, textStatus, xhr) {


            if (data.status == 302) {
                window.location.reload()
            }
            else {
                var message = $(data).find('.modal_auth_info').html().trim()
                console.log(message)
                $('.modal_auth_info').empty()
                $('.modal_auth_info').css('background-color', '#f85e5e')
                $('.modal_auth_info').css('display', 'block')
                $('.modal_auth_info').append(message)
            }

        })
    })



    $('.reg_form').on('submit', function (e) {
        e.preventDefault()
        username = $('#id_username').val()
        password = $('#id_password').val()
        password1 = $('#id_password1').val()
        email = $('#id_email').val()
        first_name = $('#id_first_name').val()
        last_name = $('#id_last_name').val()
        csrf = $('#modal_reg > div > div > div.modal-body > form > input[type=hidden]').val()
        data = {
            'username': username,
            'password': password,
            'password1': password1,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            "csrfmiddlewaretoken": csrf
        }
        console.log(data)


        $.post('/accounts/register/', data, function (data, textStatus, xhr) {
            console.log(data)
            if (data.status == 201) {
                window.location.reload()
            }
            else {

                $('.modal_reg_info').empty()
                $('.modal_reg_info').css('background-color', '#f85e5e')
                $('.modal_reg_info').css('display', 'block')
                for (var key in data.errors){
                    $('.modal_reg_info').append(data.errors[key] + '<br>')
                }
            }

        })
    })

});


