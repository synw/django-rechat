if (event_class == '__chat_message__') {
	var hours = timestamp.getHours();
	if (hours.length==1) {
		hours = "0"+hours;
	}
	var minutes = "0" + timestamp.getMinutes();
	var msgtime = hours + ':' + minutes.substr(-2);
	$('#chatbox').append('<a name="'+timestamp+'"></a>'+msgtime+' <strong>'+data['username']+'</strong>: '+message+'<br />');
	$('#chatbox').scrollTop($("#chatbox")[0].scrollHeight);
	return false
}