$(document).ready(function() {
    namespace = location.pathname;
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
    var socket2 = io.connect(location.protocol + '//' + document.domain + ':' + location.port + '/answers');

    socket.on('question', function(msg) {
    	console.log(msg)
    	$('#skill-id').text(msg.skillid);
    	$('#q-container').text(msg.question);
    });


    $('#send-answer').click(function() {
        socket2.emit('answer', {
            person: namespace[namespace.length - 1],
            answer: $('#answer').val()});
        $('#a-container input').val("");
        return false;
    });

});