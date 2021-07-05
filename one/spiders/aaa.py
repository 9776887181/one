# -*- coding: utf-8 -*-
import scrapy


class AaaSpider(scrapy.Spider):
    name = 'aaa'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print('666')
        print('aaa')
