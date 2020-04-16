#coding=utf-8
import requests
import json
import parsel
import time
 
def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False  
 
def down():
    time.sleep(3)  # 程序等待时间，这里等待1s，参数的基本单位是秒
    print("正在访问：请稍等。。。")
    url = 'https://api.ixiaowai.cn/mcapi/mcapi.php?return=json'
#    url = "https://api.ixiaowai.cn/api/api.php?return=json"
    html = requests.get(url).text
    strJson = json.loads(html.encode('utf-8'))
    imgUrl = strJson['imgurl']
    rul = requests.get(imgUrl).content
    file_nam = imgUrl.split('/')[-1]
    with open('img/' + file_nam, 'wb') as f:
        print('now dowlond: ', file_nam)
        f.write(rul)
 
if __name__ =="__main__":  
    flag = mkdir("img")#创建文件夹
    if(flag == False):
        print('目录已存在,无需创建,开始下载！')
    else:
        print('目录创建成功,开始下载！')
    strCount = input('请输入你需要下载的次数(默认999次):')
    count = 999;        
    if(strCount != ''):
        count = int(strCount)
    index = 1
    while(1):
        if(index == count + 1):
            break;
        print('正在下载' + str(index) + '张......')
        down() #下载
        index = index + 1;
    print("下载完成！")
   
