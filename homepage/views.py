from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import login as login_view
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def index(request):
    '''
    Handles index request (Panel).
    '''
#     if request.POST or not request.user.is_authenticated():
#         return login(request)

    context = {}
    return render_to_response('homepage/dashboard.html', {}, context_instance=RequestContext(request, context))
