import requests 

url = 'http://stock.gtimg.cn/data/index.php?appn=detail&action=download&c=sh600887&d=20201204'
r = requests.get(url) 
with open("1.xlsx", 'wb') as f:
    f.write(r.content)
