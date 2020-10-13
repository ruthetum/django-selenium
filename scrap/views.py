from django.shortcuts import render
from .models import Notice

def home(req):
    notices = Notice.objects.all()
    for notice in notices:
        rep = notice.link.replace('&amp;', '&')
        notice.link = rep
        notice.save()
    return render(req, 'home.html', {'notices': notices})
