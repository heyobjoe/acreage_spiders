# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from acreage_price_data.items import ProductItem



class HcSpider(scrapy.Spider):
    name = 'hc_spider'

    def start_requests(self):

        urls = [

            'http://www.thehealingcorner.com/product-category/flowers/',
            'http://www.thehealingcorner.com/product-category/vapes/',
            'http://www.thehealingcorner.com/product-category/concentrates/',
            'http://www.thehealingcorner.com/product-category/capsules/',
            'http://www.thehealingcorner.com/product-category/medibles/',
            'http://www.thehealingcorner.com/product-category/oral/',
            'http://www.thehealingcorner.com/product-category/topicals/',

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page_results = response.css('ul.products > li')

        for product in page_results:
            product_loader = ItemLoader(item=ProductItem(), selector=product)

            product_loader.default_output_processor = TakeFirst()

            product_loader.add_css('title', '.woocommerce-loop-product__title > a::text')
            product_loader.add_css('price', '.woocommerce-Price-amount::text')
            product_loader.add_css('link', '.woocommerce-loop-product__title > a::attr(href)')
            product_loader.add_css('size', '.productexcerpt::text')

            yield product_loader.load_item()
