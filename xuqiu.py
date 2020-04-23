"""
使用cookie
"""

import requests
sess = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
}
sess.get("https://xueqiu.com/", headers=headers)

url = 'https://stock.xueqiu.com/v5/stock/realtime/quotec.json?symbol=SH000001,SZ399001,SZ399006&_=1585985805696'

json_data = sess.get(url=url, headers=headers).json()

print(json_data)