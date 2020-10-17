import requests
import re
import time
from bs4 import BeautifulSoup

proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080",
}

def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    }
    url = 'http://www.cntour.cn'
    response = requests.get(url, headers=headers)
    print(response)

    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
    print(data)
    for item in data:
        result = {
            'title': item.get_text(),
            'link': item.get('href')
        }
    print(result)

    #\d匹配数字 +匹配前一个字符1次或多次
    for item in data:
        result = {
            "title": item.get_text(),
            "link": item.get('href'),
            'ID': re.findall('\d+', item.get('href'))
        }
    print(result)

if __name__ == '__main__':
    main()
