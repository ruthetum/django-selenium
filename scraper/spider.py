import scrapy
from scrapy_splash import SplashRequest
from scraper.items import NoticeItem
from scrap.models import Notice

class ComeduSpider(scrapy.Spider):
    name = 'comedu'
    starts_urls = ['https://comedu.skku.edu/comedu/notice.do?mode=list&srCategoryId1=&srSearchKey=&srSearchVal=']

    def start_requests(self):
        urls = ['https://comedu.skku.edu/comedu/notice.do?mode=list&srCategoryId1=&srSearchKey=&srSearchVal=']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        datas = response.css("#jwxe_main_content > div > div > div > ul > li")
        for data in datas:
            item = NoticeItem()
            content_list = data.css('dl > dt > a').extract()
            content = content_list[0]
            item["link"] = "https://comedu.skku.edu/comedu/notice.do" + content[content.find('?'):content.find('title')-2]
            item["title"] = content[content.find('보기">')+4:content.rfind('</a')].strip()

            date_list = data.css('dl > dd > ul > li:nth-child(3)').extract()
            date = date_list[0]
            item["date"] = date[date.find('<li>')+4:date.find('</li>')]

            # item.save()
            print(item)
            yield item

class CsSpider(scrapy.Spider):
    name = 'cs'
    starts_urls = ['https://cs.skku.edu/news/recruit/list']

    def start_requests(self):
        urls = ['https://cs.skku.edu/news/recruit/list']
        for url in urls:
            yield SplashRequest(url=url, callback=self.parse, args={"wait":2})

    def parse(self, response):
        datas = response.xpath('//*[@id="boardList"]/tbody')
        for data in datas:
            item = NoticeItem()
            num = data.css('td:nth-child(1)').extract_first()
            title = data.css('td.education.col-md-7.col-xs-8').extract_first()
        
            item["link"] = num
            item["title"] = title
            item["date"] = '1'
            
            yield item
        

"""
https://www.youtube.com/watch?v=VvFC93vAB7U
cs
- url : https://cs.skku.edu/news/recruit/list
//*[@id="boardList"]/tbody/tr[2]
link : //*[@id="boardList"]/tbody/tr[1]/td[1] //*[@id="boardList"]/tbody/tr[2]/td[1]
title : //*[@id="boardList"]/tbody/tr[1]/td[2]
#boardList > tbody > tr:nth-child(1) > td:nth-child(1)
#boardList > tbody > tr:nth-child(2) > td:nth-child(1)
#boardList > tbody > tr:nth-child(2) > td.education.col-md-7.col-xs-8
#boardList > tbody > tr:nth-child(1) > td.education.col-md-7.col-xs-8
date
"https://cs.skku.edu/news/recruit/view/" + 
coe
- url : https://coe.skku.edu/coe/community/under_notice.do


skku
- url : https://www.skku.edu/skku/campus/skk_comm/notice01.do
#boardList > tbody > tr:nth-child(1)
#boardList > tbody > tr:nth-child(1) > td:nth-child(1)
#boardList > tbody > tr:nth-child(1) > td.education.col-md-7.col-xs-8
#boardList > tbody > tr:nth-child(2) > td:nth-child(1)
"""