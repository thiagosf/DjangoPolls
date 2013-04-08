# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from polls2.models import Poll, Choice
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse

def home(request):
    return render(request, 'home.html')