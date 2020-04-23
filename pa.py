# from lxml.html import fromstring
#
# with open('index.html', 'r', encoding='utf-8') as fp:
#     data = fp.read()
#
# selector = fromstring(data)
#
# h1 = selector.xpath('/html/body/h1/text()')
# print(h1)

import requests
import asyncio
import time


# 特殊的函数
async def get_request(url):
    print('get-request被调用！')
    page_text = requests.get(url).text

    return page_text


if __name__ == '__main__':
    # 返回一个协程
    c = get_request('www.baidu.com')

    # 创建一个任务对象
    task = asyncio.ensure_future(c)

    # 创建一个事件循环
    loop = asyncio.get_event_loop()
    # 将task写到eventloop中且启动该对象
    loop.run_until_complete(task)
