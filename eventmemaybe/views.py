from django.shortcuts import render_to_response

def home(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', {'auth': 'true'})
    else:
        return render_to_response('index.html', {'auth': 'false'})