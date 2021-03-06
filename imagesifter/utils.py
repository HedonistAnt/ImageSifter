#!/usr/bin/env python
# -*- coding: utf-8 -*-
from future.standard_library import install_aliases
from . import exceptions
install_aliases()
from lxml import html
import requests
from urllib.parse import urljoin
from past.utils import old_div
import os
import re
from image_scraper.exceptions import *
from urllib import urlopen


class ImageSifter(object):
    url = None
    format_list = []
    download_path = "images"
    use_ghost = False
    page_html = None
    page_url = None
    images = None
    size_limit = None
    count_limit = None
    proxy_url = None
    proxies = {}

    def __init__(self):
        self.url = None
        self.format_list = ["jpeg", "jpg"]
        self.download_path = "images"
        self.use_ghost = False
        self.images = None
        self.size_limit = 100000000
        self.proxy_url = None
        self.proxies = {}
        self.count_limit = None
        self.page_html = None
        self.page_url = None

    def get_html(self):

        page = requests.get(self.url)

        if self.use_ghost:

            self.url = urljoin("http://", self.url)
            import selenium
            import selenium.webdriver
            driver = selenium.webdriver.PhantomJS(
                service_log_path=os.path.devnull)
            driver.get(self.url)
            page_html = driver.page_source
            page_url = driver.current_url

            driver.quit()

        else:

            try:

                if page.status_code != 200:
                    raise PageLoadError(page.status_code)
            except requests.exceptions.MissingSchema:
                self.url = "http://" + self.url
                page = requests.get(self.url, proxies=self.proxies)
                if page.status_code != 200:
                    raise PageLoadError(page.status_code)
            finally:
                page_html = page.text
                page_url = page.url

        self.page_html = page_html
        self.page_url = page_url
        return (self.page_html, self.page_url)

    def get_img_list(self):

        tree = html.fromstring(self.page_html)

        imghtml = tree.xpath('//img/@src')

        srcjs = re.findall(r'src=[\'].*[\']', self.page_html)
        imgjs = map(lambda s: re.split(r'\'', str(s))[-2], srcjs)

        htmlsplit = re.split(r'\s*', self.page_html)
        htmlstr = map(lambda s: s.encode('utf-8'), htmlsplit)

        srcext = map(lambda ext: list(
            filter(lambda x: x != None, map(lambda s: re.search('http[s]*://.*[\.]' + re.escape(ext), s), htmlstr))),
                     self.format_list)[0]  # searching for links ending in .<ext> (extensions from format_list)
        srcext = map(lambda x: x.group(0), srcext)  # getting string result

        img_list = self.process_links(imghtml) + self.process_links(imgjs) + self.process_links(srcext)
        images = img_list

        if self.count_limit != None and self.count_limit < len(images):
            self.images = images[0:self.count_limit]
        else:
            self.images = images

        return self.images

    def process_download_path(self):
        if os.path.exists(self.download_path):
            if not os.access(self.download_path, os.W_OK):
                raise DirectoryAccessError
        elif os.access(os.path.dirname(self.download_path), os.W_OK):
            os.makedirs(self.download_path)
        else:
            raise DirectoryCreateError
        return True

    def download_image(self):
        url_list = self.images
        forbidden_symbols = ['*', '|', ':', '"', '<', '>', '?', '=', '-']
        catname = self.download_path

        for url in url_list:
            try:
                page = urlopen(url, proxies=self.proxies)

            except:

                continue
            extension = (urlopen(url).headers['content-type'].split('/')[-1])
            size = urlopen(url).info().getheaders('Content-Length')[0]

            if extension not in self.format_list:
                continue

            if self.size_limit != None and int(self.size_limit) < int(size):
                continue
            name = url.split('/')[-1] + '.' + extension

            for s in forbidden_symbols:
                name = name.replace(s, '')

            path = os.path.join(catname, name)
            with open(path, "wb") as fh:
                fh.write(page.read())

    def process_links(self, links):
        x = map(lambda u: urljoin('http://', u), links)
        return x


