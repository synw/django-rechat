function postMsg(postUrl) {
	var form = document.getElementById("chatform");
	var data = serializeForm(form);
	var url = postUrl;
	var msgbox = document.getElementById("message");
	msgbox.value = "";
	postForm(url, data, data.csrfmiddlewaretoken);
	return false
}
function postForm(url, data, token) {
	var ax = axios.create({headers: {'X-CSRFToken': token}});
	ax({
		method: 'post',
		url: url,
		data: data,
	}).catch(function (err) {
		console.log(err);
	});
}
function serializeForm(form) {
	var obj = {};
	var elements = form.querySelectorAll( "input" );
	for( var i = 0; i < elements.length; ++i ) {
		var element = elements[i];
		var name = element.name;
		var value = element.value;
		if( name ) {
			obj[ name ] = value;
		}
	}
	return obj;
}