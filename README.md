### 开发环境介绍

- anaconda:
  - 基于数据分析和机器学习的集成环境
- jupyter:
  - ancaonda提供的一个基于浏览器的可视化开发工具

### jupyter的基本使用

- 在终端输入jupyter notebook 的指令启动
- jupyetr notebook 的指令录入对应的默认的目录结构就是终端对应的目录结构
- new 一个新的文件
- cell 是可以分为两种不同的模式
  - code: 用来编写和执行代码
  - markdown：编写笔记
- 快捷键的使用：
  - 插入cell：a, b
  - 删除cell：x
  - 执行cell：shift+enter 
  - 切换cell模式：
    - y：将markdown模式切换到code模式
    - m：将code模式转换为markdown模式
  - 打开帮助文档：
    - shift+tab

### 爬虫的相关概念

- 爬虫：就是通过编写程序，让其模拟浏览器上网，然后去互联网上抓取数据的过程
  - 模拟：浏览器就是一款天然的爬虫工具
  - 抓取：抓取一整张数据，抓取一整张数据中的部分数据
- 爬虫的分类
  - 通用爬虫：（数据的爬取）
    - 抓取一整张页面源码数据
  - 聚焦爬虫：（数据分析）
    - 抓取局部的指定的数据。是建立在通用爬虫基础之上的
  - 增量式爬虫：（数据的更新）
    - 监测网站数据更新的情况，抓取网站最新更新出来的数据
  - 分布式爬虫：
- 反爬机制
  - 一些网站后台会设定相关机制阻止爬虫程序进行数据爬取
- 反反爬策略
  - 爬虫需要制定相关策略破解反爬机制，从而爬取到网站的数据
- 第一个反爬机制
  - robots协议：存在于网站服务器的一个文本协议。指明了该网站中哪些数据可以爬取，哪些不能爬取

#### 图片爬取技巧

- 反爬机制：图片懒加载，只有当图片数据显示在可视化范围内，则图片才会被 加载出来
  - 伪属性：src2，阻止图片加载的。只有当伪属性变成真正的src属性图片才会被加载出来
- 分析：
  - 图片数据是否为动态加载
    - 除了可以在response选项卡中进行局部搜索，也可以在preview选项卡中看到
    - 发现preview中只显示图片的名称，并没有显示图片数据

#### 正则、bs4、xpath

#### bs4解析

- 为什么在爬虫中使用数据解析
  - 就是为了实现聚焦爬虫
- 数据解析的通用原理是什么？（解析的数据只会存在于标签之间和属性中）
  - html是用来数据展示
  - 原理流程
    - 标签定位
    - 数据的提取
- bs4数据解析的解析原理
  - 实例化一个BeautifulSoup的对象，且将等待被解析的数据加载到该对象中
    - 方式一：
      - BeautifulSoup(fp, "lxml"):解析本地存储的html文件
    - 方式二：
      - BeautifulSoup(page_text, "lxml"):解析互联网上请求到的页面数据
  - 调用BeautifulSoup对象中的相关方法和属性进行标签定位和数据的提取
- 环境安装
  - pip install bs4
  - pip install lxml
- 标签定位
  - soup.tagName:返回第一次出现的tagName标签
  - 属性定位：soup.find('tagName', attrName='value')
  - findAll和find的用法一样，但是返回值不一样
  - 选择器定位：
    - select('selector')
- 数据的提取
  - 提取标签中存在的数据
    - .string:取出标签直系的文本内容
    - .text:取出标签中所有的文本内容
  - 提取标签属性中存储的数据
    - tagName['attrName']

#### xpath解析

- html标签结构
  - 是一个树状结构
- xpath解析原理
  - 实例化一个etree对象，且将即将被解析的数据加载到该对象中
    - 解析本地的html文档
      - etree.parse('fileName')
    - 解析网上爬取的html文档
      - etree.HTML(page_text)
  - 使用etree对象中的xpath方法结合不同的xpath表达方式实现标签定位和数据提取

##### xpath表达式

```
from lxml import etree
tree = etree.parse('./test.html')
tree.xpath('./html/head')
tree.xpath('//head')
```

- 标签定位(tree.xpath('/html/head'))
  - 最左侧的/:必须要从标签的根标签开始逐层的定位目标标签
  - 最左侧的//:可以从任意位置定义目标标签
  - 属性定位：//tagName[@attrName='value']
  - 索引定位：//tagName[index] 下标从1开始
- 数据提取
  - 取标签中的数据
    - /text()：直系文本内容
    - //text()：所有的文本内容
  - 取属性中的数据
    - tagName/@attrName