function notifToHTML(data) {
	var html = '<div class="notif segment">'
	html += '<h1>' + data.title +  '</h1>'
    html += '<p>' + data.content + '</p>'
    html += '<h2>' + data.poster + '</h2>'
    html += '<h3>' + moment(data.post_date).format('hh:mm') + '</h3></div>'
    return html
}

function notifFeedToHTML() {
	var notifFeedHTML
	jQuery.ajaxSetup({async: false})
	$.getJSON('/notifications/all', function (notifs) {
		if(notifs.length == 0)
			notifFeedHTML = ''
		else if(notifs.length == 1)
			notifFeedHTML = notifToHTML(notifs[0])
		else {
			var notifsHTML = $.map(notifs, notifToHTML)
			notifFeedHTML = notifsHTML.reduce(function (prev, curr, index, array) {
				return prev + curr
			})
		}
	})
	return notifFeedHTML
}

function adminNotifEntry() {
	var html = ''
	html += '<h1>New Notification</h1>'
    html += '<div class="notif creation">'
    html += '<textarea type="text" class="short-text" id="notif-title" placeholder="The notification\'s title"></textarea>'
    html += '<textarea type="text" class="short-text" id="notif-name" placeholder="Admin"></textarea>'
    html += '<textarea type="text" class="long-text" id="notif-body" placeholder="Describe the notification here"></textarea>'
    html += '<div class="button post" id="notif-button">Post</div></div>'
	return html
}

function addNotifications(element) {
	if(authenticated) {
		$(element).html(adminNotifEntry() + notifFeedToHTML())
		$('#notif-button').click(function() {
			$.post('/notifications/new/', {
				"title": $('textarea#notif-title').val(),
				"poster": $('textarea#notif-name').val(),
				"content": $('textarea#notif-body').val(),
				"tweet_this": true,
			}, function (response) {
				console.log(response)
				addNotifications('#notif-pane')
			})
		})
	}
	else $(element).html(notifFeedToHTML())
}