$( function() {
    $( ".sortable" ).disableSelection();
    $( ".sortable" ).sortable({
        connectWith: ".sortable",
    });
    var rls = $('ranked-lists');
});