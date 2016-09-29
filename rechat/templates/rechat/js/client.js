{% load i18n rechat_tags %}

var rechat_callbacks = {
    "message": function(dataset) {
    	if (debug === true) { console.log('CHAT: '+JSON.stringify(dataset));};
    	res = unpack_data(dataset);
    	var message = res['message']
    	var event_class = res['event_class']
    	var data = res['data']
    	var timestamp = res['timestamp']
    	// handlers
    	if (event_class == '__chat_message__') {
    		var msgtime = getClockTime(true);
    		$('#chatbox').append('<a name="'+timestamp+'"></a>'+msgtime+' <strong>'+data['username']+'</strong>: '+message+'<br />');
    		$('#chatbox').scrollTop($("#chatbox")[0].scrollHeight);
    	}
    },
    {% include "instant/js/join_events.js" %}
}

var subscription = centrifuge.subscribe("{% chatchannel %}", rechat_callbacks);