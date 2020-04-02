'''
分析：
    - 获取肯德基门店位置信息
    - 数据为动态加载数据
    - 请求方式：post
    - URL:http://www.kfc.com.cn/kfccda/storelist/index.aspx
    - UA:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
'''
import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
}
data = {
    "cname": "北京",
    "pid": "",
    "pageIndex": "1",
    "pageSize": "10",
}

response = requests.post(url=url, headers=headers, data=data)

# 获取店铺json格式数据
page_text = response.json()

for dic in page_text['Table1']:
    add = dic['addressDetail']
    print('店铺地址为： ', add)