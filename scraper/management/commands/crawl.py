from django.core.management.base import BaseCommand
from scrapy.utils.project import get_project_settings
from scraper.selenium.target import comedu, cs, coe, skku

class Command(BaseCommand):
    def handle(self, *args, **options):
        comedu()
        cs()
        coe()
        skku()