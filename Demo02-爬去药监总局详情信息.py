'''
需求：
    - 爬取药监总局中的企业详情数据
分析：
    - url:http://125.35.6.84:81/xk/
    - 发现为动态加载数据
    - 详情页url:http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById
    - 请求参数: id: ff83aff95c5541cdab5ca6e847514f88
    - 从首页可以获取id
'''
# 获取每家企业的id
import requests

url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
}
data = {
    "on": "true",
    "page": "1",
    "pageSize": "15",
    "productName": "",
    "conditionType": "1",
    "applyname": "",
    "applysn": "",
}

response = requests.post(url=url, headers=headers, data=data)
all_company_list = response.json()['list']

for dic in all_company_list:
    _id = dic['ID']
    # print(_id)
    # 将id作为详情页url参数请求
    detail_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'

    data = {
        "id":_id,
    }
    response = requests.post(url=detail_url, headers=headers, data=data)
    company_detail = response.json()

    companyName = company_detail['epsName']
    companyAddr = company_detail['epsAddress']

    print('公司名称： %s 公司地址： %s'%(companyName, companyAddr))




