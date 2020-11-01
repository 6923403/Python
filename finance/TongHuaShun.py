import requests
from bs4 import BeautifulSoup
import os
import xlrd
import xlwt
from xlutils.copy import copy
import json
import time

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class TongHua():
    def __init__(self):
        self.url = 'http://www.10jqka.com.cn/'
        self.data = requests.get(self.url, headers=headers)


def main():
    Ths = TongHua()
    try:
        Ths.
