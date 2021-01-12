$( function() {
    $( ".sortable" ).disableSelection();
    $( ".sortable" ).sortable({
        connectWith: ".sortable"
    });
});