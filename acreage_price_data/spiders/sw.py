# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from acreage_price_data.items import ProductItem


class SwSpider(CrawlSpider):
    name = 'sw_spider'

    start_urls = [

        'https://www.soctwellness.com/product-category/flowers/',
        'https://www.soctwellness.com/product-category/vape-oils/',
        'https://www.soctwellness.com/product-category/concentrates/',
        'https://www.soctwellness.com/product-category/medibles/',
        'https://www.soctwellness.com/product-category/capsules/',
        'https://www.soctwellness.com/product-category/oral-syringes-sprays-slips-tinctures/',
        'https://www.soctwellness.com/product-category/oral-solution/',
        'https://www.soctwellness.com/product-category/topicals/',

    ]

    rules = (
        Rule(LinkExtractor(allow=(),
                           restrict_xpaths=('//*[@class="next page-numbers"]',)),
             callback="parse_page", follow=True),
    )

    def parse_page(self, response):
        print('*****************************Page hit**********************************************')
        page_results = response.css('ul.products > li')

        for product in page_results:

            product_loader = ItemLoader(item=ProductItem(), selector=product)

            product_loader.default_output_processor = TakeFirst()

            product_loader.add_css('title', '.product-title > a::text')
            product_loader.add_css('price', '.woocommerce-Price-amount::text')
            product_loader.add_css('link', '.product-title > a::attr(href)')
            product_loader.add_css('size', '.size > .attribute-value::text')

            yield product_loader.load_item()




