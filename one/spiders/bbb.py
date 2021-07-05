# -*- coding: utf-8 -*-
import scrapy


class BbbSpider(scrapy.Spider):
    name = 'bbb'
    allowed_domains = ['sg.search.yahoo.com']
    start_urls = ['http://sg.search.yahoo.com/']

    def parse(self, response):
        print('bbb')
        
