from django.shortcuts import render
from .models import Notice

def home(req):
    notices = Notice.objects.all()
    for notice in notices:
        rep = notice.link.replace('&amp;', '&')
        notice.link = rep
        notice.save()

    notices1 = Notice.objects.all()[:10]
    notices2 = Notice.objects.all()[10:20]
    notices3 = Notice.objects.all()[20:30]
    notices4 = Notice.objects.all()[30:]

    content = {'notices1': notices1, 'notices2': notices2, 'notices3': notices3, 'notices4': notices4,}
    return render(req, 'home.html', content)
