from scrapy_djangoitem import DjangoItem
from scrap.models import Notice

class NoticeItem(DjangoItem):
    django_model = Notice