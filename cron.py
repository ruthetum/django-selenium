import os
import subprocess
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webscraping.settings")
django.setup()
from scrap.models import Notice

def updateNotice():
    # 40개 먼저 크롤링
    cw = os.getcwd()
    if (cw):
        os.system('python manage.py crwal')

    # 이후 40개 삭제
    notices = Notice.objects.all()[:40]
    for notice in notices:
        notice.delete()

updateNotice()