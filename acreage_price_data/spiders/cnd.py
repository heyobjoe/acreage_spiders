# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from acreage_price_data.items import ProductItem

filename = "products.txt"

class CndSpider(scrapy.Spider):
    name = 'cnd_spider'

    def start_requests(self):

        urls = [

            'http://www.caringnaturedispensary.com/product-category/topicals/',
            'http://www.caringnaturedispensary.com/product-category/flower/',
            'http://www.caringnaturedispensary.com/product-category/vape-cartridges/',
            'http://www.caringnaturedispensary.com/product-category/edibles/',
            'http://www.caringnaturedispensary.com/product-category/oral-meds/',
            'http://www.caringnaturedispensary.com/product-category/concentrates/',

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

       page_results = response.css('ul.products > li')

       for product in page_results:

           product_loader = ItemLoader(item=ProductItem(), selector=product)

           product_loader.default_output_processor = TakeFirst()

           product_loader.add_css('title', 'h3::text')
           product_loader.add_css('price', '.woocommerce-Price-amount::text')
           product_loader.add_css('link', 'a.woocommerce-LoopProduct-link::attr(href)')

           yield product_loader.load_item()

