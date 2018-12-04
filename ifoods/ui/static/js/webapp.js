$(document).ready(function(){
 $('#framework').multiselect({
  nonSelectedText: 'Select Framework',
  enableFiltering: true,
  enableCaseInsensitiveFiltering: true,
  buttonWidth:'400px'
 });

 $('#framework_form').on('submit', function(event){
  event.preventDefault();
  var form_data = $(this).serialize();
  $.ajax({
   url:"insert.php",
   method:"POST",
   data:form_data,
   success:function(data)
   {
    $('#framework option:selected').each(function(){
     $(this).prop('selected', false);
    });
    $('#framework').multiselect('refresh');
    alert(data);
   }
  });
 });

 $("#hiringManagerChk").on("change", function()
    {
        $('#companynameDiv').toggle(this.checked);
    });


    $("#interviewerChk").on("change", function()
    {
        $('.form-group.interviewerDiv').toggle(this.checked);
    });


	
    $("input[name$='optradio']").click(function() {
        var test = $(this).val();
        if(test > 1)
		{
        $("#radiovalue1").hide();
		$("#radiovalue2").show();
		}
		else{
			
			$("#radiovalue1").show();
			$("#radiovalue2").hide();
		}
        //$("#Cars" + test).show();
    });

	$("#DivContent").load("../html/resultTable.html");

    $("#searchId").on("click", function(ev){
      //alert('search')
      ev.preventDefault();

        radioSelection = $("input[type='radio'][name='optradio']:checked").val();
        if(radioSelection==1)
        {
           restaurant = $("#restraurantNameInpt").val();
        }
        else if (radioSelection==2)
        {
            restaurant = $("select#curlocres option").filter(":selected").val();
        }
      var modalid = $(this).data("target");
      var url = $(this).attr("href");

       $.ajax({
        type: 'GET',
        url: "search",
        data : { 'radioSelection': radioSelection,'restaurant':restaurant},
        success : function(data) {
        // Add response in Modal body
             $('#myModal').find('.modal-content').html(data);
             $("#myModal").modal("show"); // Triggering bootstrap modal.
            //$("#request-access").hide();

        }
    })

    });




var datadiv = [];

$("#restraurantName option").each(function()
{
   datadiv.push($(this).val());
});

var $input = $(".typeahead");
	$input.typeahead({
	  source: datadiv,
	  autoSelect: true
	});

});


function feedIframe(menu_item_id)
{
var id = menu_item_id+"_aid";
var frameid= menu_item_id+"_iframeid";
document.getElementById(frameid).src = document.getElementById(id).href;
}



