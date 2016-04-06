function singleTimepicker(start_datetime){	
	singleTimepickerGeneric(start_datetime, false);
}

function singleTimepickerWithHour(start_datetime){	
	singleTimepickerGeneric(start_datetime, true);
}

function singleTimepickerGeneric(start_datetime, include_time){	
	$(start_datetime).datetimepicker({
		showTimepicker:include_time,
	    showTime: include_time,
	    alwaysSetTime : include_time,
	    showHour: include_time,
	    showMinute: include_time,
	    changeYear: true,
	});
	
	$(start_datetime).keyup(function(event) {
		var len = $(this).val().length;
		if( len != 16 && len != 0) {
			$(start_datetime).attr('value', "");
		}
		return false;
	});
	
	$(start_datetime).mousedown(function(event){
		setTimeout(function(){
			$("#ui-datepicker-div").css('z-index', '2147483647');
		}, 100);
	});
}

function doubleTimepicker(start_datetime, end_datetime){	
	doubleTimepickerGeneric(start_datetime, end_datetime, false, null);
}

function doubleTimepickerWithHour(start_datetime, end_datetime){	
	doubleTimepickerGeneric(start_datetime, end_datetime, true, null);
}

function doubleTimepickerCombine(start_datetime, end_datetime, combine_datetime){	
	doubleTimepickerGeneric(start_datetime, end_datetime, false, combine_datetime);
}

function doubleTimepickerCombineWithHour(start_datetime, end_datetime, combine_datetime){	
	doubleTimepickerGeneric(start_datetime, end_datetime, true, combine_datetime);
}

function doubleTimepickerGeneric(start_datetime, end_datetime, include_time, combine_datetime){	
	$(start_datetime).datetimepicker({
		showTimepicker:include_time,
	    showTime: include_time,
	    alwaysSetTime : include_time,
	    showHour: include_time,
	    showMinute: include_time,
	    changeYear: true,
	    onSelect: function (selectedDateTime){
	    	var start = $(this).val();
	    	var end_date = $(end_datetime).val();
	    	
	    	var date = null;
	    	var edate = null;
	    	var new_start_date = null;
	    	var old_end_date = null;
	    	
	    	if(include_time){
	    		// update the start datetime if script error to put the time info
	    		if(start.length == 10){
	    			start += " 00:00";
	    			$(this).val(start);
	    		}
	    		// update the end datetime
	    		if(end_date.length == 0 && end_date.length != 16) {
	    			$(end_datetime).val(start);
	    		}
	    		date = start.split(/[\s:-]+/);
	    		edate = end_date.split(/[\s:-]+/);
	    		new_start_date = new Date(date[2], date[1]-1, date[0], date[3], date[4]);
	    		old_end_date = new Date(edate[2], edate[1]-1, edate[0], edate[3], edate[4]);
	    		$(end_datetime).datetimepicker('option', 'minDate', new_start_date);
	    		$(end_datetime).datetimepicker('option', 'minDateTime', new_start_date);
	    	} else{
	    		date = start.split("-");
	    		edate = start.split("-");
	    		new_start_date = new Date(date[2], date[1]-1, date[0]);
	    		old_end_date = new Date(edate[2], edate[1]-1, edate[0]);
	    		$(end_datetime).datetimepicker('option', 'minDate', new_start_date);
	    	}
	    	if (end_date == ""){
	    		$(end_datetime).val(start);
	    	} else{
	    		if(old_end_date < new_start_date) {
	    			$(end_datetime).val(start);
	    		}
	    		else {
	    			$(end_datetime).val(end_date);
	    		}
	    	}
	    	
	    	if (combine_datetime != null) {
	    		$(combine_datetime).val($(start_datetime).val()+","+$(end_datetime).val());
	    	}
	    }
	});
	$(end_datetime).datetimepicker({
		showTimepicker:include_time,
	    showTime: include_time,
	    alwaysSetTime : include_time,
	    showHour: include_time,
	    showMinute: include_time,
	    changeYear: true,
	    onSelect: function (selectedDateTime){
	        var end = $(this).val();
	        var start_date = $(start_datetime).val();
	        var date = null;
	        var sdate = null;
	        var new_old_date = null;
	        var old_start_date = null;
	        
	        if(include_time){
	        	// update the end datetime if script error to put the time info
	        	if(end.length == 10){
	    			end += " 00:00";
	    			$(this).val(end);
	    		}
	        	// update the start datetime
	    		if(start_date.length == 0 && start_date.length != 16) {
	    			$(start_datetime).val(end);
	    		}
	    		date = end.split(/[\s:-]+/);
	    		sdate = start_date.split(/[\s:-]+/);
	    		new_end_date = new Date(date[2], date[1]-1, date[0], date[3], date[4]);
	    		old_start_date = new Date(sdate[2], sdate[1]-1, sdate[0], sdate[3], sdate[4]);
	    		$(start_datetime).datetimepicker('option', 'maxDate', new_end_date);
	    		$(start_datetime).datetimepicker('option', 'maxDateTime', new_end_date);
	    	} else{
	    		date = end.split("-");
	    		sdate = start_date.split("-");
	    		new_end_date = new Date(date[2], date[1]-1, date[0]);
	    		old_start_date = new Date(sdate[2], sdate[1]-1, sdate[0]);
	    		$(start_datetime).datetimepicker('option', 'maxDate', new_end_date);
	    	}
	        if (start_date == ""){
	        	$(start_datetime).val(end);
	        }else{
	    		if(old_start_date > new_end_date) {
	    			$(start_datetime).val(end);
	    		}
	    		else {
	    			$(start_datetime).val(start_date);
	    		}
	        }
	        
	        if (combine_datetime != null) {
	    		$(combine_datetime).val($(start_datetime).val()+","+$(end_datetime).val());
	    	}
	    }
	});
	$(start_datetime).keyup(function(event) {
		var len = $(this).val().length;
		if( len != 16 && len != 0) {
			$(start_datetime).attr('value', "");
			$(end_datetime).attr('value', "");
		}
		if (combine_datetime != null) {
			$(combine_datetime).val($(start_datetime).val()+","+$(end_datetime).val());
		}
		return false;
	});
	$(end_datetime).keyup(function(event) {
		var len = $(this).val().length;
		if( len != 16 && len != 0) {
			$(start_datetime).attr('value', "");
			$(end_datetime).attr('value', "");
		}
		if (combine_datetime != null) {
			$(combine_datetime).val($(start_datetime).val()+","+$(end_datetime).val());
		}
		return false;
	});
	
	$(start_datetime).mousedown(function(event){
		setTimeout(function(){
			$("#ui-datepicker-div").css('z-index', '2147483647');
		}, 100);
	});
	
	$(end_datetime).mousedown(function(event){
		setTimeout(function(){
			$("#ui-datepicker-div").css('z-index', '2147483647');
		}, 100);
	});
}