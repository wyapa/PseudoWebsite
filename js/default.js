$(document).ready(function(){
	var code = $(".codemirror-textarea")[0];
	var editor = CodeMirror.fromTextArea(code, {
		lineNumbers : true
	});



});

$.ajax({
  type: "GET",
  url: "../test.py"
}).done(function( o ) {
   console.log(o);
});