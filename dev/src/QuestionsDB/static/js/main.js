$(document).ready(function () {
    $("a.comment-hide").click(function () {
    $(this).parent().parent().toggle()
    });
});