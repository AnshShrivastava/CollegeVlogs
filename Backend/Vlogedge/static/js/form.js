$(document).on('submit','#request-form',function(e){
    e.preventDefault();

    $.ajax({
        type:'POST',
        url:'newrequest',
        data:{
            name : $('#name').val(),
            email : $('#email').val(),
            myfile : $('#file').val(),
            collegename : $('#collegename').val(),
            requests : $('#requests').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },

        success:function () {
            alert("Data added")
            $("#request-form")[0].reset();       
        }
    });
});