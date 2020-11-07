$(document).on('submit','#leads-form',function(e){
    e.preventDefault();

    $.ajax({
        type:'POST',
        url:'leadsrequest',
        data:{
            name : $('#name').val(),
            collegename : $('#collegename').val(),
            email : $('#email').val(),
            requests : $('#requests').val(),
            collegeemail : $('#collegeemail').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },

        success:function () {
            alert("Request send...")
            $("#leads-form")[0].reset();
        }
    });
});
