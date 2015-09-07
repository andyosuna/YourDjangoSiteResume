"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name': 'Andy Gonzalez',
    'bio': 'Software Engineer',
    'email': 'info@andyosuna.com',
    'twitter_username': 'andiosuna',  # No @ symbol, just the handle.
    'github_username': "andyosuna",
    'headshot_url': 'https://avatars2.githubusercontent.com/u/3093129',
}


def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance=RequestContext(request, {
            'attendee': YOUR_INFO,
            'year': datetime.now().year,
        })
    )
