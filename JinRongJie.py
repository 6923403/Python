import requests
import os
from bs4 import BeautifulSoup
import re
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class JinRongJie(object):

    def __init__(self):
        self.url = 'http://www.jrj.com.cn/'
        self.m_news = requests.get(self.url, headers=headers)

        self.hkurl = 'http://hk.jrj.com.cn/list/hgxw.shtml'
        self.hk_news = requests.get(self.hkurl, headers=headers)

    def getNews(self):
        print("getNews \n")
        soup = BeautifulSoup(self.m_news.text, 'html.parser')
        datalist = soup.find_all(class_="test-s1")
        #print(datalist)

        for news in datalist:
            News = news.select('p')
            if len(News) > 0:
                try:
                    href = News[0]['href']
                    print(href)
                except Exception:
                    print("href = NULL")

    def getHongkongNews(self):
        print("hkNews搜索结果 \n")
        soup = BeautifulSoup(self.hk_news.text, 'html.parser')
        data = soup.select("ul.jrj-l1")

        for news in data.find_all():
            print(news)


if __name__ == '__main__':
    jR = JinRongJie()
    if not os.path.exists("./JinRongJie"):
        os.mkdir("./JinRongJie")
    try:
        print('\n')
        #jR.getNews()
    except Exception:
        print("获取失败")
    try:
        jR.getHongkongNews()
    except Exception:
        print("hkNews获取失败")


