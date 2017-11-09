#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re,urllib.request
import logging;logging.basicConfig(level=logging.INFO)

class Url_Paraser(object):

    def parse(self,url,html_content):
        if url is None or html_content is None:
            logging.info("url or html_content is None")
            return
        soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
        new_urls = self.get_new_urls(url,soup)
        new_datas = self.get_new_datas(url,soup)
        return new_urls,new_datas

    def get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/item/[\\%\\w]+'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.request.urljoin(url,new_url)
            new_urls.add(new_full_url)
        return new_urls



    def get_new_datas(self, url, soup):
        new_datas = {}

        new_datas['url'] = url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        new_datas['title'] = title_node.get_text()

        # <div class="lemma-summary">
        summary_node = soup.find('div', class_="lemma-summary")
        new_datas['summary'] = summary_node.get_text()

        return new_datas



