if (event_class == '__chat_message__') {
	var msgtime = getClockTime(true);
	$('#chatbox').append('<a name="'+timestamp+'"></a>'+msgtime+' <strong>'+data['username']+'</strong>: '+message+'<br />');
	$('#chatbox').scrollTop($("#chatbox")[0].scrollHeight);
	return false
}