'use strict';

function handleResponse(response) {
    $('#results').html(response);
}

let request = null;

function getResults() {

    let keyword = $('#keyword').val();
    let url = '/search?q=' + encodeURIComponent(keyword);

    console.log(url);

    if (request != null)
        request.abort();

    request = $.ajax(
    {
        type: 'GET',
        url: url,
        success: handleResponse
    }
    );
}

function setup() {

    $('#index').addClass('current_page');
    $('#keyword').on('input', getResults);
}

$('document').ready(setup);