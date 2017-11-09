# Simple_crawl

* url_manager：管理url，负责加入解析过程中新增的url以及移除已爬取的url
* url_downloader：下载url的内容，使用最简单的urlopen函数，不带cookie的爬取网页内容
* url_paraser:解析url，解析百度百科的标题等内容，利用BeautifulSoupde查找元素并返回内容
* url_outputer:保存解析的内容并写入html文档中

# 基本思路
首先爬取root_url的内容，解析该url，如果发现有新的url，则加入待爬取的url列表中，将爬取的内容加入 url\_outputer中并写入html文档，直到url列表中没有待爬取的url时或者达到设定的爬取数量，则停止爬取