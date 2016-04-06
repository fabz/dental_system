$(document).ready(function(){
  $('.row-view').hover(function(){
    $(this).find('.row-tools').css('visibility','visible');
  }, function(){
    $(this).find('.row-tools').css('visibility','hidden');
  });
});

var ajax_typeahead = function(el_id, url, options){
  var field_value         = el_id;
  var field_label         = 'field_label' in options ? options['field_label'] : 'lookup_'+field_value;
  var label_key           = 'label_key' in options ? options['label_key'] : 'name';
  var value_key           = 'value_key' in options ? options['value_key'] : 'id';
  var url                 = url;
  
  $('#'+field_label).typeahead({
    property: label_key,
    source: function(typeahead, query){
      return $.get(url, { q:query }, function(data){
        return typeahead.process(data);
      });
    },
    onselect: function(obj){
      $('#'+field_value).val(obj[value_key]);
    }
  });
};