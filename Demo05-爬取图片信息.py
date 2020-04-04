'''
需求：
    - 爬取图片数据和名称保存到本地
分析：
    - url： http://pic.netbian.com/4kmeinv/index.html
    - 第一页： http://pic.netbian.com/4kmeinv/index.html
    - 第二页： http://pic.netbian.com/4kmeinv/index_2.html
'''
from lxml import etree
import requests
import os

dirName = 'img_girl'
if not os.path.exists(dirName):
    os.mkdir(dirName)

url = 'http://pic.netbian.com/4kmeinv/index_%d.html'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
}

for page in range(1, 3):
    if page == 1:
        new_url = 'http://pic.netbian.com/4kmeinv/index.html'
    else:
        new_url = format(url % page)
    response = requests.get(url=new_url, headers=headers)
    response.encoding = 'gbk'
    page_text = response.text

    # 数据解析，分析图片信息
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    # 获取所有li 标签
    for li in li_list:
        # 局部数据解析
        img_src = "http://pic.netbian.com" + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        img_data = requests.get(url=img_src, headers=headers).content

        filePath = dirName + "/" + img_name
        with open(filePath, 'wb') as fp:
            fp.write(img_data)
        print(img_name, "下载成功！")
