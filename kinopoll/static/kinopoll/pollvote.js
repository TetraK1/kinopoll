$( function() {
    $(".sortable").disableSelection();
    $('.ranked-question').each(function(){
        rq = $(this)
        rq.find('.sortable').sortable({
            connectWith: '#' + rq.attr('id') + ' .sortable',
            //containment: $(this)
        })
    });
});