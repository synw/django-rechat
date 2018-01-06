if (event_class == '__chat_message__') {
	var msgtime = getClockTime(true);
	msg = '<a name="'+timestamp+'"></a>'+msgtime+' <strong>'+data['username']+'</strong>: '+message+'<br />';
	var chatbox = document.getElementById("chatbox");
	chatbox.innerHTML = chatbox.innerHTML + msg;
	chatbox.scrollTop = chatbox.scrollHeight;
}