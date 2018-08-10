# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from acreage_price_data.items import ProductItem


class AacSpider(CrawlSpider):
    name = 'aac_spider'
    allowed_domains = ['www.arrowalternativecare.com']
    start_urls = [
        'https://www.arrowalternativecare.com/medical-marijuana/product-catalog-and-online-ordering/hartford-location/',
        'https://www.arrowalternativecare.com/medical-marijuana/product-catalog-and-online-ordering/milford-location/',
    ]


    rules = (
        Rule(LinkExtractor(allow=(),
                                restrict_xpaths=('//*[@id="djcatalog"]/div[7]/ul/li[13]',)),
                                callback="parse_page", follow=True),
    )


    def parse_page(self, response):
        print('*****************************Page hit**********************************************')
        page_results = response.css('div.djc_item_in')

        for product in page_results:
            product_loader = ItemLoader(item=ProductItem(), selector=product)

            product_loader.default_output_processor = TakeFirst()

            product_loader.add_css('title', '.djc_title > h3 > a::text')
            product_loader.add_css('price', '.djc_price > span::text')
            product_loader.add_css('link', '.djc_title > h3 > a::attr(href)')
            product_loader.add_css('size', '.djc_attributes > table > tr > td.djc_value::text')

            yield product_loader.load_item()

