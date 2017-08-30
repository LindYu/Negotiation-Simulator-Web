/*** 
   Testing\static\js\ajax.js
   Aug 28th, 2017
   Author: Linda Yu 

***/

/*On Submit Button, if the student's offer falls within threshold, update the counteroffer*/

$(function(){
	$('#survey').on('submit',function(event){
		event.preventDefault();
		create_post();
		$.ajax({
			type: "POST",
			url:'/vote/',
			data:{
				'R1B1':$("input:radio[name=R1B1]:checked").val(),
				'R1B2':$("input:radio[name=R1B2]:checked").val(),
				'R1B3':$("input:radio[name=R1B3]:checked").val(),
				'R2B1':$("input:radio[name=R2B1]:checked").val(),
				'R2B2':$("input:radio[name=R2B2]:checked").val(),
				'R2B3':$("input:radio[name=R2B3]:checked").val(),
				'R3B1':$("input:radio[name=R3B1]:checked").val(),
				'R3B2':$("input:radio[name=R3B2]:checked").val(),
				'R3B3':$("input:radio[name=R3B3]:checked").val(),	
			},
			dataType: "html",			
			success: function(){
				
				// expected sets the threshold of the sum of points offered by the student 
				var expected = 20;
				if ($("#Bid1").val() <= expected || $("#Bid2").val() <= expected ||$("#Bid3").val() <= expected)
				alert("Your bid is below expected value "+expected+ " , please check your Sum column");	
			
				else{
				
				if ($(document.activeElement).val() == "Submit"){	
				// submit successful, show the counteroffer columns 				
				alert("Form submitted! Please check the counteroffers.")
				$("#survey").css("width","125%")
				var x = document.getElementById('col1');
				x.style.visibility = 'visible';
				var x = document.getElementById('col2');
				x.style.visibility = 'visible';
				var x = document.getElementById('col3');
				x.style.visibility = 'visible';
				var x = document.getElementById('T1');
				x.style.visibility = 'visible';
				var x = document.getElementById('T2');
				x.style.visibility = 'visible';
				var x = document.getElementById('T3');
				x.style.visibility = 'visible';
				
				var x = document.getElementById('copy1');
				x.style.visibility = 'collapse';
				var x = document.getElementById('copy2');
				x.style.visibility = 'collapse';
				var x = document.getElementById('copy3');
				x.style.visibility = 'collapse';
				var x = document.getElementById('T1C');
				x.style.visibility = 'collapse';
				var x = document.getElementById('T2C');
				x.style.visibility = 'collapse';
				var x = document.getElementById('T3C');
				x.style.visibility = 'collapse';
				
				$('input:radio:checked').each(function() {
				var attrName = $(this).attr("name");	
				
				/******PUT ALGORITHM HERE, CURRENTLY ECHOING THE STUDENTS' CHOICES******/	
				
				var counter = attrName[0]+attrName[1]+"C"+attrName[3]		 
				$("#"+counter).html(parseInt($(this).attr("value")));	 
				$("#"+counter).val(parseInt($(this).attr("value")));
				$("#"+counter + "C").html(parseInt($(this).attr("value")));	 
				$("#"+counter + "C").val(parseInt($(this).attr("value")));
				
				/***********************************************************************/
				});
				}	
				
				//if not submitting but want to change layout
				else if ($(document.activeElement).val() == "Bids"){
					console.log("LAYOUT BIDS REQUESTED");
					// check if bids filled out but didn't submit yet
					if ($("#R3C1").val() == "undefined" || $("#R3C1").val() == ""){
					alert("Please submit your bids first to choose layout.");					
					}
					// if submitted show the columns resulting a group by bid layout  
				    else{
						$("#survey").css("width","125%")
						var x = document.getElementById('col1');
						x.style.visibility = 'collapse';
						var x = document.getElementById('col2');
						x.style.visibility = 'collapse';
						var x = document.getElementById('col3');
						x.style.visibility = 'collapse';
						var x = document.getElementById('T1');
						x.style.visibility = 'collapse';
						var x = document.getElementById('T2');
						x.style.visibility = 'collapse';
						var x = document.getElementById('T3');
						x.style.visibility = 'collapse';
						
						var x = document.getElementById('copy1');
						x.style.visibility = 'visible';
						var x = document.getElementById('copy2');
						x.style.visibility = 'visible';
						var x = document.getElementById('copy3');
						x.style.visibility = 'visible';
						var x = document.getElementById('T1C');
						x.style.visibility = 'visible';
						var x = document.getElementById('T2C');
						x.style.visibility = 'visible';
						var x = document.getElementById('T3C');
						x.style.visibility = 'visible';
					  			
					}
						
				}
				
				// group by offer
				else{
					if ($("#R3C1").val() == "undefined" || $("#R3C1").val() == ""){
					alert("Please submit your bids first to choose layout.");					
					}
					else{
						$("#survey").css("width","125%")
						var x = document.getElementById('col1');
						x.style.visibility = 'visible';
						var x = document.getElementById('col2');
						x.style.visibility = 'visible';
						var x = document.getElementById('col3');
						x.style.visibility = 'visible';
						var x = document.getElementById('T1');
						x.style.visibility = 'visible';
						var x = document.getElementById('T2');
						x.style.visibility = 'visible';
						var x = document.getElementById('T3');
						x.style.visibility = 'visible';
						
						var x = document.getElementById('copy1');
						x.style.visibility = 'collapse';
						var x = document.getElementById('copy2');
						x.style.visibility = 'collapse';
						var x = document.getElementById('copy3');
						x.style.visibility = 'collapse';
						var x = document.getElementById('T1C');
						x.style.visibility = 'collapse';
						var x = document.getElementById('T2C');
						x.style.visibility = 'collapse';
						var x = document.getElementById('T3C');
						x.style.visibility = 'collapse';
					}	
				}
				}
			}
	});	
});
});


/*Upon clicking, add the sum of points at the bottom of the table*/
$(function()
	{$('input[type = "radio"]').change(function(event){
		event.preventDefault();
		var response_data = $(this).attr('name');
		$.ajax({
			type: "GET",
			url:'/vote/',	 
			dataType: "html",	
			success: function(){
				var sub = response_data.substring(2,4);
				var score = 0;
				
				//loop through to group and add up scores from each option
				$('input:radio:checked').each(function() {
                var attrName = $(this).attr("name");
                if (attrName.indexOf(sub) >= 0){
					score += parseInt($(this).attr("value"));
					return true;
				}	
				})
				$("#Bid"+sub[1]).html("<font color = 'red'>"+score+"</font>");
				$("#Bid"+sub[1]).val(score);
			}	
		});				
	});
});
	

// Debug function
function create_post() {
    console.log("create post is working!") 
};


/*Django csrf token code*/
// using jQuery csrf
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});