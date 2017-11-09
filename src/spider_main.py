#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.url_downloader import Url_Downloader
from src.url_manager import Url_Manager
from src.url_outputer import Url_Outputer
from src.url_paraser import Url_Paraser

__author__ = "WingC"

import logging
logging.basicConfig(level=logging.INFO)

root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"

class Spider(object):
    def __init__(self):
        self.url_manager = Url_Manager()
        self.url_downloader = Url_Downloader()
        self.url_paraser = Url_Paraser()
        self.url_outputer = Url_Outputer()


    def crawl(self,url):
        count = 1
        self.url_manager.add_new_url(url)
        while self.url_manager.has_new_url():
            try:
                new_url = self.url_manager.get_new_url()
                logging.info("crawl %d : %s" % (count,new_url))
                html_content = self.url_downloader.download(new_url)
                new_urls,new_data = self.url_paraser.parse(new_url,html_content)
                self.url_manager.add_new_urls(new_urls)
                self.url_outputer.collect_data(new_data)
                count = count +1

                #爬取前10条记录
                if count == 10:
                    break
            except:
                logging.info("crawl failed")

        self.url_outputer.output_html()

if __name__ == '__main__':
    spider = Spider()
    spider.crawl(root_url)






