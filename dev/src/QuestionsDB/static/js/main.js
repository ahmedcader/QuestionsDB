$(document).ready(function () {
    $("a.comment-reply").click(function (e) {
        e.preventDefault();
        $(this).parent().parent().children('div.add-comment.add-reply').slideToggle();
        var text = $(this).text() === 'reply' ? 'cancel reply' : 'reply';
        $(this).text(text)
    });

    $("a.comment-hide").click(function (e) {
        e.preventDefault();
        $(this).parent().parent().next().slideToggle();
         var text = $(this).text() === 'hide replies' ? 'show replies' : 'hide replies';
        $(this).text(text)
    });
});