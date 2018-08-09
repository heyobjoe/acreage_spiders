# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from acreage_price_data.items import ProductItem

class BpSpider(scrapy.Spider):
    name = 'bp_spider'
    allowed_domains = ['https://www.bluepointwellnessct.com/current-inverntory/']
    start_urls = ['http://https://www.bluepointwellnessct.com/current-inverntory//']

    def parse(self, response):
        pass
