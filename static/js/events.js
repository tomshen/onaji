function eventToHTML(data) {
	var html = ''
	var date = moment(data.date)
	
	html += '<h1>' + date.format('dddd') + '</h1>'
	html += '<div class="event"><div class="event-head">'
	html += '<h2>' + data.name + '</h2>'
	html += '<h3>' + date.format('hh:mm') + '</h3>'
	html += '<h4>' + data.location + '</h4>'
	html += '<div class="edit small icon"></div> \
             <div class="delete small icon"></div> \
			 </div><div class="event-body"><p>'
    html += data.description + '</p></div></div>'
	return html
}

function scheduleToHTML() {
	var scheduleHTML
	jQuery.ajaxSetup({async: false})
	$.getJSON('/events/all', function (events) {
		if(events.length == 0)
			scheduleHTML = ''
	    else if(events.length == 1)
			scheduleHTML = eventToHTML(events[0])
		else {
			var eventsHTML = $.map(events, eventToHTML)
			scheduleHTML = eventsHTML.reduce(function (prev, curr, index, array) {
				if(prev.indexOf(curr.substring(curr.indexOf('<h1>')+4, curr.indexOf('</h1>'))) != -1)
				    return prev + curr.substring(curr.indexOf('</h1>')+5)
				else
					return prev + curr
			})
		}
	})
	return scheduleHTML
}

function adminEventEntry() {
    return '<h1><div class="add small static-icon"></div>New Event</h1> \
      <div class="event new">\
        <div class="event-head">\
          <textarea type="text" placeholder="Event Name" class="fit-text" id="event-name" ></textarea>\
          <textarea type="text" placeholder="Date" class="date-text" id="date"></textarea>\
          <textarea type="text" placeholder="location" class="fit-text" id="event-location" ></textarea>\
        </div>\
        <div class="event-body">\
          <textarea type="text" placeholder="event description" class="long-text" id="event-description" ></textarea>\
		  <div class="button post" id="event-button">Post</div> \
        </div> \
      </div>'
}

function addSchedule(element) {
	$("#schedule-pane").html("");
	if(authenticated) {
		$(element).html(adminEventEntry() + scheduleToHTML())
		$('#date').datetimepicker({
			timeFormat: 'h:mmtt',
			stepHour: 1,
			stepMinute: 15,
			addSliderAccess: true,
			sliderAccessArgs: { touchonly: false }
		})
		$('#event-button').click(function() {
			//var date_raw = moment().format('YYYY') + '-' + $('textarea#event-month').val() + '-' + $('textarea#event-day').val()
			//var time_raw = $('textarea#event-hour').val()  + ':' + $('textarea#event-minute').val()
			var datetime_raw = $('textarea#date').val()
			var date = moment(datetime_raw, "MM/D/YYYY h:ma")
			$.post('/events/new/', {
				"name": $('textarea#event-name').val(),
				"location": $('textarea#event-location').val(),
				"description": $('textarea#event-description').val(),
				"date": date.format(),
			}, function (response) {
				console.log(response)
				addSchedule('#schedule-pane')
			})
		})
	}
	else $(element).html(scheduleToHTML())
}