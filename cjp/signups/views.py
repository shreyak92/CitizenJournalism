from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse
# Create your views here.

from .forms import SignUpForm

def home(request):

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        return HttpResponseRedirect('/signup-success/')

    return render_to_response("homepage.html", locals(), context_instance=RequestContext(request))


def thankyou(request):

    return render_to_response("signupsuccess.html", locals(), context_instance=RequestContext(request))

def about(request):

    return render_to_response("aboutus.html", locals(), context_instance=RequestContext(request))

def login(request):

    c = {}
    c.update(csrf(request))
    return render_to_response("homepage.html", c)

def authentication(request):
    email_address = request.POST.get('email_address', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(email_address=email_address, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/logged-in/')
    else:
        return HttpResponseRedirect('/authentication-failed/')#

def invalid_login(request):

    return render_to_response("authfail.html", locals(), context_instance=RequestContext(request))

def logged(request):

    return render_to_response("loggedin.html", locals(), context_instance=RequestContext(request))

#def language(request, language='en-us'):
 #   response = HttpResponse("setting language to %s" % language)
  #  response.set_cookie('lang', language)
   # return response