function change_to_timestamp(ddmmyy) {
	splits = ddmmyy.split("-");
	dd = parseInt(splits[0], 10);
	mm = parseInt(splits[1], 10);
	yy = parseInt(splits[2], 10);
	return new Date(yy, mm - 1, dd).getTime() / 1000;
}

function on_amount_key_up() {
	field = $(this);
	field_val = extract_digit(field.val());
	field_val = addCommas(field_val);
	field.val(field_val);
}

function on_amount_key_up_non_ajax(id_field) {
	field = $(id_field);
	field_val = extract_digit(field.val());
	field_val = addCommas(field_val);
	field.val(field_val);
}

function addCommas(str) {
    var amount = new String(str);
    amount = amount.split("").reverse();

    var output = "";
    for ( var i = 0; i <= amount.length-1; i++ ){
        output = amount[i] + output;
        if ((i+1) % 3 == 0 && (amount.length-1) !== i)output = ',' + output;
    }
    return output;
}

function removeCommas(str) {
    var output = new String(str);
    output = output.replace(/\./g,'');
    output = output.replace(/,/g,'');
    return output;
}

function extract_digit(str) {
	var output = new String(str);
    output = output.replace(/[^0-9]+/g,'');
    return output;
}
