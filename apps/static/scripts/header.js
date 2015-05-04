/**
 * Created by scb53 on 2015/4/22.
 */


$('#id_sidebar-opener').click(function () {
    $('#id_sidebar-wrapper').fadeToggle('fast','linear');
    //if($('#id_content').css())
    $('#id_content').hide('fast').toggleClass('col-md-10');
    $('#id_content').toggleClass('col-md-12').fadeToggle('fast');
});
