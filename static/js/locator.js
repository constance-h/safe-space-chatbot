"use strict";

var map;

function initMap(mapCenter = {lat : 37.7749, lng : -122.4194}){
    const options ={
        zoom: 10,
        center: mapCenter
    };

    map = new google.maps.Map(document.querySelector('#map'), options);

}

$('#search-error').hide();

$('#search-form').on('submit', (evt) => {
    evt.preventDefault();

    const formData = $('#search-form').serialize();

    $.post('/therapy_data.json', formData, (res) => {
        if (res == "error"){
            $('#search-error').show();
        }
        else {
            //remove search message if one exists
            $('#search-error').hide();
            const therapists = res.therapists

            //re-center map based on search results
            initMap(therapists[0].coords);
            for (const i in therapists){
                const therapist = therapists[i];
                //create marker
                const marker = new google.maps.Marker({
                    position: therapist.coords,
                    map,
                    animation: google.maps.Animation.DROP
                });
                
                //format content for info window
                const contentHTML = 
                    '<p><strong>' + therapist.name + '</strong><p>'+
                    '<p>' + therapist.address[0] + ', ' + therapist.address[1] + ' </p>'+
                    '<p>' + therapist.address[2] + '</p>'+
                    '<p>' + therapist.phone + '</p>'
                    // '< a href src= "' + therapist.url + '">Yelp Page</a>'
                
                //create info window
                const infoWindow = new google.maps.InfoWindow({content: contentHTML});
                
                //add event listener to open window on click
                marker.addListener('click', () => {
                    infoWindow.open(map, marker);
                });
            }
        }
    });
        

});