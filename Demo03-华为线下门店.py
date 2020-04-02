'''
需求：
    - 获取华为线下门店详情信息
分析：
    - url: https://m.vmall.com/help/huaweistoreaddr.htm
    - 是否为动态加载数据: 是
    - 详情页url : https://openapi.vmall.com/mcp/offlineshop/getShopById
    - 请求参数：  portal: 2
                version: 10
                country: CN
                shopId: 212032
                lang: zh-CN
    - 结论： 获取每家的 shopId 可以捕获所有店铺详情信息
    - 捕获每家店铺的 Id
    - url: https://openapi.vmall.com/mcp/offlineshop/getShopList
    - 请求方式： post
    - 请求参数： {"portal":2,"lang":"zh-CN","country":"CN","brand":2,"province":"广东","city":"广州","pageNo":1,"pageSize":20}:

'''
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
}

data = {
    "portal": 2,
    "lang": "zh-CN",
    "country": "CN",
    "brand": 2,
    "province": "广东",
    "city": "广州",
    "pageNo": 1,
    "pageSize": 20,
}

# 捕获每家店铺的id
url = 'https://openapi.vmall.com/mcp/offlineshop/getShopList'

json_data_id = requests.post(url=url, headers=headers, json=data).json()
for dic in json_data_id['shopInfos']:
    _id = dic['id']
    # print(_id)
    detail_url = 'https://openapi.vmall.com/mcp/offlineshop/getShopById'

    params = {
        "portal": "2",
        "version": "10",
        "country": "CN",
        "shopId": _id,
        "lang": "zh-CN",
    }
    shop_detail = requests.get(url=detail_url, headers=headers, params=params).json()
    # 获取店铺名字和地址
    # print((shop_detail))
    shopName = shop_detail['shopInfo']['name']
    shopAddr = shop_detail['shopInfo']['address']
    print('店铺名字： %s 店铺地址： %s' %(shopName, shopAddr))