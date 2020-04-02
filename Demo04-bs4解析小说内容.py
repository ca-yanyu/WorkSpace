'''
需求：
    - 使用bs4爬取三国演义正片小说内容
    - url: http://shicimingju.com/book/sanguoyanyi.html
分析：
    - 从首页解析出章节标题和详情页url

'''
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
}
fp = open("./sanguo.txt", 'w', encoding='utf-8')

url = 'http://shicimingju.com/book/sanguoyanyi.html'

# 获取首页章节内容
page_text = requests.get(url=url, headers=headers).text

soup = BeautifulSoup(page_text, 'lxml')
# 定位到所有标题的a标签
a_list = soup.select('.book-mulu a')
for a in a_list:
    title = a.string
    detail_url = 'http://shicimingju.com' + a['href']

    # 解析提取详情内容
    page_text_detail = requests.get(url=detail_url, headers=headers).text

    # 解析详情页的章节内容
    soup = BeautifulSoup(page_text_detail, 'lxml')
    content = soup.find('div', class_='chapter_content').text

    # 写入文件
    fp.write(title + ':' + content + '\n')
    print(title, "下载成功！")
