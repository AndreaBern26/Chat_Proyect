
$(document).ready(function(){
    var socket = io.connect('http://127.0.0.1:5000');

    socket.on('connect', function(){
        socket.send('User has connected')
    });

    socket.on('message', function(msg){
        $('.messages').append('<p>'+ msg + '</p>');
    });

    $('.submit').on('click', function(){
        socket.send($('.message').val());
        $('.message').val('')
    });
})
