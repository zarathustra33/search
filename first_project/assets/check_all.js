$('#select-all').click(function(event) {   
    if(this.checked) {
        // Iterate each checkbox
        $(':checkbox').each(function() {
            this.checked = true;                        
        });
    } else {
        $(':checkbox').each(function() {
            this.checked = false;                       
        });
    }
});

$('#submit-position').click(function(event){
    var checked=$('#result-table').find(':checked').length;
    if (!checked){
        alert('to send email, please select at least one candidate');
    }
})


$(function () {
    $("#id_resume_submited_date").datetimepicker( {
       format:'Y-m-d',
    });
  });