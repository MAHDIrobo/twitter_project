from django.shortcuts import render
from django.http import HttpResponse
from .models import post 
mypost=post.objects.all()


def index(request):
    ret='<body>'
    all_posts= mypost
    for post in all_posts:
        ret = ret+'<p>' + post.text + '</p>'
    ret=ret + '</body>'

    return HttpResponse(ret)
