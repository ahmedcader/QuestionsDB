$(document).ready(function () {
    $("a.comment-hide").click(function () {
        // console.log($(this).parent().parent().children().toggle())
        $(this).getElementsByClassName('div.comment-container').next().toggle()
    });
});