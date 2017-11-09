#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import logging

logging.basicConfig(level=logging.INFO)

class Url_Downloader(object):

    def download(self, new_url):
        if new_url is None or not isinstance(new_url,str):
            raise TypeError("url can only be str type and cann't be empty")
        response = urllib.request.urlopen(new_url)
        if response.getcode() == 200:
            return response.read()
        else:
            logging.info("download url failed")
