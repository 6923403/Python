import requests
import os
import re
from Crypto.Cipher import AES #pip install pycryptodome
from copy import deepcopy
import time

"""
https://v.pinimg.com/videos/mc/hls/38/20/a0/3820a0682a5312c71c0bd9a831cfcc7c_480w_20200426T074057_00001.ts
https://v.pinimg.com/videos/mc/hls/38/20/a0/3820a0682a5312c71c0bd9a831cfcc7c.m3u8
"""

def main():
    path = r"N:\codes\m3"
    file_dirlist = os.listdir(path)  # 读目录
    for m3u8file in file_dirlist:
        if len(m3u8file.strip().split(".")) > 1:
           if m3u8file.strip().split(".")[-1] == "m3u8":
               name = m3u8file.strip().split(".")[0].strip().replace(",", "").replace(" ", "")

#Wait build

if __name__ == '__main__':
    main()
    print("Over .")

"""
mu38 
open .mu38
ts and key use ffmpeg
"""
