$(document).on('submit','#request-form',function(e){
    e.preventDefault();

    $.ajax({
        type:'POST',
        url:'newrequest',
        data:{
            name : $('#name').val(),
            collegename : $('#collegename').val(),
            email : $('#email').val(),
            requests : $('#requests').val(),
            filenew : $('#filenew').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },

        success:function () {
            alert("Data added")
            $("#request-form")[0].reset();       
        }
    });
});