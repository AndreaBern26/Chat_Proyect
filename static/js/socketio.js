
$(document).ready(function(){
    var socket = io.connect('http://127.0.0.1:5000');

    socket.on('message', function(msg){
        $('.messages').append( msg + '<br>');
        console.log('received message');
    })

    $('.submit').on('click', function(){
        socket.send($('.myMessage').val());
        $('.myMessage').val('');
    });
});