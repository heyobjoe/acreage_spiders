# -*- coding: utf-8 -*-
import scrapy


class TvrSpider(scrapy.Spider):
    name = 'tvr'
    allowed_domains = ['https://www.thamesvalleyrelief.com/']
    start_urls = ['http://https://www.thamesvalleyrelief.com/']

    def parse(self, response):
        pass
