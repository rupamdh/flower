$(document).ready(function () {
    $('#eye-btn').click(function (e) { 
        e.preventDefault();
        if($(this).prev().attr('type') === 'password'){
            $(this).prev().attr('type', 'text');
        } else {
            $(this).prev().attr('type', 'password');
        }
        if ($(this).html() == '<i class="fa-solid fa-eye"></i>') {
            $(this).html('<i class="fa-solid fa-eye-slash"></i></i>');
        } else {
            $(this).html('<i class="fa-solid fa-eye"></i>');
        }
    });
    
    $("#mobile").keypress(function(event){
        var inputValue = event.charCode;
        if(!(inputValue >= 48 && inputValue <= 57)) {
            event.preventDefault();
            $(this).parent().find('.err-msg').html('Enter only number');
        } else {
            $(this).parent().find('.err-msg').empty();
        }

    });

    $("#backbtn").click(function (e) {
        e.preventDefault();
        window.history.back();
    });

    $('.cat-sidebar .has-child').append('<div class="sub-btn"></div>');
    $('.sub-btn').click(function (e) {
        e.preventDefault();
        $(this).parent().siblings().find('ul').slideUp();
        $(this).prev().slideToggle();
        $(this).parent().siblings().removeClass('active');
        $(this).parent().siblings().find('.sub-btn').removeClass('open');
        $(this).toggleClass('open');
    });

    $('.cat-sidebar .active').parent().addClass('active');
    $('.cat-sidebar .active').parent().parent().addClass('active');
    $('.cat-sidebar .active').parent().parent().parent().parent().addClass('active');
});