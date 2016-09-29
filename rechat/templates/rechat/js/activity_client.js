{% load i18n rechat_tags %}

var num_msgs = 0;
var ts = new TimeSeries();

var i = 1;
setInterval(function() {
	var t = new Date().getTime();
	var x = 0;
	if ( num_msgs != 0 ) {
		var x = num_msgs * 10000;
	}
	console.log(t+' / '+x);
	ts.append(t, x);
	if (i > 1) {
		num_msgs = 0;
		i = 0;
	}
	else {
		i++;
	}
}, 1000);
 
function createTimeline() {
   var chart = new SmoothieChart({
			   millisPerPixel:85,
			   maxValueScale:1,
			   grid:{millisPerLine:4000},
			   minValue:-3000,
			   labels:{disabled:true},
			});
   chart.addTimeSeries(ts, 
   		//{ strokeStyle: 'rgba(0, 255, 0, 1)', fillStyle: 'rgba(0, 255, 0, 0.2)', lineWidth: 2 }
		   { strokeStyle: 'rgba(0, 255, 0, 1)', lineWidth: 2 }
   );
   chart.streamTo(document.getElementById("chart"), 1000);
 }
 createTimeline()

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
    		// activity
    		num_msgs += 1;
    		
    	}
    },
    {% include "instant/js/join_events.js" %}
}

var subscription = centrifuge.subscribe("{% chatchannel %}", rechat_callbacks);