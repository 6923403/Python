import time
import requests
import gb

headers = {
    'User-Agent' : 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; huawei mla-al10 Build/HUAWEIMLA-AL10) AppleWebKit/533.1',
}

def get_info():
    result = ''
    url = 'https://h.huajiao.com/api/getUserInfo?callback=__jp0'
    try:
        req = requests.get(url, headers=headers)
        if 'uid' in req.text and 'nickname' in req.text:
            result = req.text
            result = gb.unicodetrans(result)
    except Exception as e:
        gb.log_info('get live huajiao error: %s' % str(e))
    return result

def getphone_num():
    result = ''
    url = 'https://passport.huajiao.com/user/getBinds?'
    try:
        req.requests.get(url, headers=headers)
        if 'errmsg' in req.text and 'rid' in req.text:
            result = req.text
    except Exception as e:
        gb.log_info('get phone_num error: %s' % str(e))
    return result


def start(uid, cookie, mac):
    headers['Cookie'] = cookie
    info = get_info()
    if info != '':
        phone_num = getphone_num()
        file_name = ('live_huajiao' + '_' + str(time.time()).replace('.', '')[:14] + '.json')
        gb.out_file(file_name, info + '\1\n' + phone_num + '\1\n')


if __name__ == '__main__':
    uid = '213285813'
    cookie = 'token=ZWUMtnu1XnK_WwbWdw--cYOamkSTvVPm7b3d'
    mac = '00000000'
    start(uid, cookie, mac)



