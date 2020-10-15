import os
from selenium import webdriver
from bs4 import BeautifulSoup
from scrap.models import Notice

os.chdir('scraper/driver/windows')

def comedu():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://comedu.skku.edu/comedu/notice.do?mode=list&srCategoryId1=&srSearchKey=&srSearchVal=')
    driver.implicitly_wait(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for i in range (1,11):
        conPath = '#jwxe_main_content > div > div > div > ul > li:nth-child(' + str(i) + ') > dl > dt > a'
        contents = soup.select(conPath)
        for c in contents:
            link = 'https://comedu.skku.edu/comedu/notice.do' + c['href']
            title = c.text.strip()
        notice = Notice(title=title, link=link, date="1")
        notice.save()
    driver.quit()

def cs():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://cs.skku.edu/news/recruit/list')
    driver.implicitly_wait(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for i in range (1,11):
        numPath = '#boardList > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(1)'
        titlePath = '#boardList > tbody > tr:nth-child(' + str(i) + ') > td.education.col-md-7.col-xs-8'
        nums = soup.select(numPath)
        titles = soup.select(titlePath)
        for n in nums:
            link = 'https://cs.skku.edu/news/recruit/view/' + n.text.strip()
        for t in titles:
            title = t.text.strip()
        notice = Notice(title=title, link=link, date="1")
        notice.save()
    driver.quit()

def coe():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://coe.skku.edu/coe/community/under_notice.do')
    driver.implicitly_wait(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for i in range (1,11):
        conPath = '#jwxe_main_content > div > div > div > ul > li:nth-child(' + str(i) + ') > dl > dt > a'
        contents = soup.select(conPath)
        for c in contents:
            link = 'https://coe.skku.edu/coe/community/under_notice.do' + c['href']
            title = c.text.strip()
        notice = Notice(title=title, link=link, date="1")
        notice.save()
    driver.quit()

def skku():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.skku.edu/skku/campus/skk_comm/notice01.do')
    driver.implicitly_wait(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for i in range (1,11):
        conPath = '#jwxe_main_content > div > div > div.container > div.board-wrap.board-qa.table_scrollWrap > table > tbody > tr:nth-child(' + str(i) + ') > td.left > a'
        contents = soup.select(conPath)
        for c in contents:
            link = 'https://www.skku.edu/skku/campus/skk_comm/notice01.do' + c['href']
            title = c.text.strip()
        notice = Notice(title=title, link=link, date="1")
        notice.save()
    driver.quit()

"""
comdue
https://comedu.skku.edu/comedu/notice.do?mode=list&srCategoryId1=&srSearchKey=&srSearchVal=

cs
https://cs.skku.edu/news/recruit/list

coe
https://coe.skku.edu/coe/community/under_notice.do


skku
https://www.skku.edu/skku/campus/skk_comm/notice01.do
"""