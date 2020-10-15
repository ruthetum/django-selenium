from django.core.management.base import BaseCommand
from scrapy_splash import SplashRequest
from scraper.scraper.spider.Spider import ComeduSpider, CsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        # process.crawl(CsSpider)
        process.crawl(ComeduSpider)
        process.start()