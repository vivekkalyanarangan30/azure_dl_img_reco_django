$(document).ready( function() {
	$("#pred_response").hide();
	$("#pred_response_b").hide();
	$("#pred_response_o").hide();
	$("#error_div").hide();
	
    	$(document).on('change', '.btn-file :file', function() {
		var input = $(this),
			label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
		input.trigger('fileselect', [label]);
		});

		$('.btn-file :file').on('fileselect', function(event, label) {
		    
		    var input = $(this).parents('.input-group').find(':text'),
		        log = label;
		    
		    if( input.length ) {
		        input.val(log);
		    } else {
		        if( log ) alert(log);
		    }
	    
		});
		function readURL(input) {
		    if (input.files && input.files[0]) {
		        var reader = new FileReader();
		        
		        reader.onload = function (e) {
		            $('#img-upload').attr('src', e.target.result);
		        }
		        
		        reader.readAsDataURL(input.files[0]);
		    }
		}
		
		function scroll_to_predict() {
			$('html, body').animate({
				scrollTop: $('#tf_predict').offset().top
			}, 'slow', function() { 
				$('#tf_predict').focus(); 
			});
		}

		$("#imgInp").change(function(){
		    readURL(this);
			$("#pred_response").show();
			$("#pred_response_b").show();
			$("#pred_response_o").show();
			scroll_to_predict();
			$("#error_div").hide();
		}); 
		
		$("#imgForm").submit(function (e){
			e.preventDefault();
			file = $('#imgInp')[0].files[0];
			
			// var fr = new FileReader;
			// var img_OK = true;
			// fr.onload = function() { // file is loaded
			// 	var img = new Image;
			// 	img.onload = function() {
			// 		if(img.width < 100){
			// 			$('#img_width').text("No");
			// 		}
			// 		if(img.height < 100){
			// 			$('#img_height').text("No");
			// 		}
			// 	};
			// 	img.src = fr.result; // is the data URL because called with readAsDataURL
			// };
			// fr.readAsDataURL(file); 

			var myFormData = new FormData($(this)[0]);
			var csrftoken = Cookies.get('csrftoken');
			myFormData.append('csrfmiddlewaretoken', csrftoken);
			
			var width_img = $('#img_width').text();
			console.log(width_img);
			if( width_img != "No"){
				$.ajax({
					type: $(this).attr('method'),
					url: $(this).attr('action'),
					enctype: $(this).attr('enctype'),
					headers: { "X-CSRFToken": '{{csrf_token}}' },
					processData: false,
					contentType: false,
					data: myFormData, //$(this).serialize(),
					success: function(data) {
						console.log(data)
						resp = JSON.parse(data);

						perc_prob = resp.house * 100;
						perc_prob = perc_prob.toFixed(2);
						value = perc_prob.toString()+'%';
						$('#progress_bar').text(value); 
						$('#progress_bar').attr("style","width:"+value); 

						perc_prob_b = resp.blueprint * 100;
						perc_prob_b = perc_prob_b.toFixed(2);
						value_b = perc_prob_b.toString()+'%';
						$('#progress_bar_b').text(value_b); 
						$('#progress_bar_b').attr("style","width:"+value_b); 

						perc_prob_o = resp.others * 100;
						perc_prob_o = perc_prob_o.toFixed(2);
						value_o = perc_prob_o.toString()+'%';
						$('#progress_bar_o').text(value_o); 
						$('#progress_bar_o').attr("style","width:"+value_o); 

						console.log(resp.ind);
						if(resp.ind == "yes"){
							
							$("#error_div").show();
							$("#error_message").text("Looks like you uploaded a picture of "+resp.aux_txt+". Please upload image of a house or blueprint.");
						}
					},
					error: function(xhr, textStatus, errorThrown) {
						$("#error_div").show();
						$("#error_message").text(errorThrown+'\t'+xhr.status+'. Please upload images above 100x100 dimensions');
						$('#progress_bar').text('0%'); 
						$('#progress_bar').attr("style","width: 0%"); 
						$('#progress_bar_b').text('0%'); 
						$('#progress_bar_b').attr("style","width: 0%"); 
						$('#progress_bar_o').text('0%'); 
						$('#progress_bar_o').attr("style","width: 0%"); 
					}
				});
			} else{

				err_msg = "Please upload image more than 100x100 in dimensions";
				alert(err_msg);

				$("#error_div").show();
				$("#error_message").text(err_msg);

				$('#progress_bar').text('0%'); 
				$('#progress_bar').attr("style","width: 0%"); 
				$('#progress_bar_b').text('0%'); 
				$('#progress_bar_b').attr("style","width: 0%"); 
				$('#progress_bar_o').text('0%'); 
				$('#progress_bar_o').attr("style","width: 0%"); 

			}
			return false;
		});
	});