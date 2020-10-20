import requests
import json
import time
import os
import re
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class TongHua(object):
    def __init__(self):
        self.url = 'http://www.10jqka.com.cn/'
        self.m_news = requests.get(self.url, headers=headers)
        self.m_news.encoding = 'GBK'

    def get_Topnews(self):
        print("TopNews_搜索结果".center(20, '*'))
        soup = BeautifulSoup(self.m_news.text, 'html.parser')
        datalist = soup.find_all(class_="item_txt")
        print(datalist, '\n')

        print(datalist['href'])
        for news in datalist:
            type_a = news.select('a')
            if len(type_a) > 0:
                try:
                    href = type_a[0]['href']
                    print(href)
                except Exception:
                    print("herf = NULL")
                try:
                    title = type_a[0]['title']
                    print(title)
                except Exception:
                    print("title = NULL")
                try:
                    news_id = type_a[0]['id']
                    print(news_id)
                except Exception:
                    print("news_id = NULL")


    def get_Chance(self):
        print("投资机会_News".center(20, '*'))
        data = self.soup.find_all(class_='tab-container')
        print(data)


if __name__ == '__main__':
    TH = TongHua()
    if not os.path.exists("./TongHuaShun_news"):
        os.mkdir("./TongHuaShun_news")
    TH.get_Topnews()
    """
    try:
        #TH.get_Chance()
    except:
        print("获取失败, 请重试")
    """

