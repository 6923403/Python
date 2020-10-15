import requests
import json

def main():
    host='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    word = host
    endpoint = "post"
    url=''.join([host, endpoint])

    m_data={
        "i": "晚安",
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "16027840699404",
    "sign": "3049c9ec63fc27774b93f384a0497330",
    "lts": "1602784069940",
    "bv": "0c00cda0db2530a31944351caf80d8b0",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION"
}
    response=requests.post(url,m_data)
    # 将Json格式字符串转字典
    content=json.loads(response.text)
#    print(content['translateResult'][0][0]['tgt'])
    print(content)

if __name__ == '__main__':
    main()

