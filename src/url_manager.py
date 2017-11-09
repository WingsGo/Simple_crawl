#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Url_Manager(object):
    def __init__(self):
        self.__new_urls = set()
        self.__old_urls = set()

    def add_new_url(self, url):
        if url is None or not isinstance(url,str):
            raise TypeError("url can only be str type and cann't be empty")
        if url not in self.__old_urls and url not in self.__new_urls:
            self.__new_urls.add(url)

    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for new_url in new_urls:
            self.add_new_url(new_url)

    def has_new_url(self):
        return self.__new_urls is not None or len(self.__new_urls) != 0

    def get_new_url(self):
        new_url = self.__new_urls.pop()
        self.__old_urls.add(new_url)
        return new_url



