"use strict";

function getResponse(){
    const userMsg = $("#user-input").val();
    const userHtml = '<p class="userText"><span>' + userMsg + '</span></p>';
    $("#user-input").val("");
    $("#chatbox").append(userHtml);

    // $("#chatbox").scrollIntoView({block: 'start', behavior:"smooth"});

    $.post("/get_response", {msg: userMsg}).done(function(data){
        const botHtml = `<p class="botText"><span>${data}</span></p>`;
        $('#chatbox').append(botHtml);
        // $('#chatbox').scrollIntoView({block: 'start', behavior : 'smooth'});


    });

}

$('#msg-form').on('submit', (evt) =>{
    evt.preventDefault();

    if($("#user-input").val() != ""){
        getResponse();
    }
});

