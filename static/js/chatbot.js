"use strict";

function getResponse(){
    const chatDiv = document.getElementById('chatbox')
    const userMsg = $("#user-input").val();
    const userHtml = '<p class="userText"><span>' + userMsg + '</span></p>';
    $("#user-input").val("");
    $("#chatbox").append(userHtml);

    const status = '<p id="status" class="botText"><span><i>Spacey is writing...</i></span></p>';
    $('#chatbox').append(status);
    chatDiv.scrollTop = chatDiv.scrollHeight;

    $.post("/get_response", {msg: userMsg}, (res) => {
        const botHtml = `<p class="botText"><span>${res}</span></p>`;
        $('#status').remove();
        $('#chatbox').append(botHtml);
        chatDiv.scrollTop = chatDiv.scrollHeight;
    });


}

$('#msg-form').on('submit', (evt) => {
    evt.preventDefault();
    if($("#user-input").val() != ""){
        getResponse();
    }
});

