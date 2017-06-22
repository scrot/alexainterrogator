var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + location.pathname);
var socket2 = io.connect(location.protocol + '//' + document.domain + ':' + location.port + '/answers');

$(document).ready(function() {
    socket.on('question', handleQuestion);

    $('#a-container').keyup(function(e){
        if(e.keyCode == 13){
            sendAnswer();
        }
    });

});

function handleQuestion(msg){
    console.log(msg)
    $('#skill-id').text(msg.skillid);
    $('#q-container').text(msg.question);
}

function sendAnswer(){
    socket2.emit('answer', {
        person: location.pathname[location.pathname.length - 1],
        answer: $('#answer').val()});
    $('#a-container input').val("");
    return false;
}