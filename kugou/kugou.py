import requests
import os
import json
import re
import time


class Ku_Gou(object):
    def __init__ (self):
        pass

    def download(self):
        while True:
            songname = input("\n input Songname>>").strip()
            if songname == '':
            	print("输入为空,重新输入")
                continue
            url = "http://songsearch.kugou.com/song_search_v2?callback=jQuery112407470964083509348_1534929985284&keyword={}&" \
                  "page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filte" \
                  "r=0&_=1534929985286".format(songname)
            try:
                res = requests.get(url).text
                js = json.loads(res[res.index('(') + 1:-2])
                data = js['data']['lists']
            except TimeoutError:
                print("\n超时")
                break
            except:
                print("未找到歌曲")
                break

            print("搜索结果".center(20, '*'))
            print("{:6}{:30}".format("序号", "歌手  -  歌名"))
            try:
                for i in range(10):
                    print(str(i + 1) + "    " + str(data[i]['FileName']).replace('<em>', '').replace('</em>', ''))
                song_num = int(input("\n 输入歌曲序号"))
                if song_num <= 0:
                    print("请检查输入是否有误")
                    break
                try:
                    name = str(data[song_num - 1]['FileName']).replace('<em>', '').replace('</em>', '')
                    fhash = re.findall('"FileHash":"(.*?)"', res)[song_num - 1]
                    ID = data[song_num]['AlbumID']
                    downurl = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery191006287980471670584_1584780452839&hash={0}&album_id={1}&dfid=3dTk9E0IfcV50gyRKr3OGZey&mid=0407f15d60c01b0ccb16bf2323d904b2&platid=4&_=1584780452841'.format(fhash, ID)
                    hash_content = requests.get(downurl)
                    play_url = ''.join(re.findall('"play_url":"(.*?)"', hash_content.text))
                    real_download_url = play_url.replace("\\", "")
                except TimeoutError:
                    print("下载超时")
                    break
                try:
                    save_path = "D:\\PyProject\\un3\\musicdownload\\" + name + ".mp3"
                    true_path = os.path.abspath(save_path)
                    print("下载中.....")
                    song_file = open("D:\\PyProject\\un3\\musicdownload\\" + name + ".mp3", "wb+")
                    song_file.write(requests.get(real_download_url).content)
                    song_file.close()
                    print("{}已保存至{}".format(name, true_path))
                except:
                    print("下载或写入文件出错")
            except:
                print("异常错误，请重新下载")


if __name__ == '__main__':
    K_API = Ku_Gou()
    if not os.path.exists("./musicdownload"):
        os.mkdir("./musicdownload/")
    while True:
        try:
            K_API.download()
        except:
            print("下载出错")

