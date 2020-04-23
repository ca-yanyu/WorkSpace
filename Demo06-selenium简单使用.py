'''
需求：
    - 使用selenium爬取药监总局中前三页的企业名称
'''

import time
from selenium import webdriver
from lxml import etree

# 开启浏览器
bro = webdriver.Chrome(executable_path='./chromedriver')
url = 'http://125.35.6.84:81/xk'
bro.get(url)

# 爬取前三页数据
time.sleep(2)

# 获取当前页面的加载数据
page_text = bro.page_source

all_page_text = [page_text]
for i in range(3):
    # 使用点击属性,对下一页按钮的定位进行点击
    a_tag = bro.find_element_by_xpath('//*[@id="pageIto_next"]')
    a_tag.click()
    time.sleep(1)
    all_page_text.append(bro.page_source)

for page_text in all_page_text:
    # 对加载的数据进行解析
    tree = etree.HTML(page_text)

    li_list = tree.xpath('//*[@id="gzlist"]/li')

    for li in li_list:
        name = li.xpath('./dl/@title')[0]
        print(name)

time.sleep(1)
# 关闭浏览器
bro.quit()
